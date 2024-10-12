from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from Auth.api.serializers import RegistrationSerializer
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

# AUTHENTICATION VIEW

@api_view(['POST'])
def RegistrationView(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            data = {
                'response': 'Registration Successful!',
                'username': account.username,
                'email': account.email,
                'token': {
                    'refresh': str(RefreshToken.for_user(account)),
                    'access': str(RefreshToken.for_user(account).access_token),
                }
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def LogoutView(request):
    try:
        # fetching the refresh token from the request body
        refresh_token = request.data.get('refresh')

   
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)


        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({'detail': 'Logout successful, token blacklisted.'}, status=status.HTTP_205_RESET_CONTENT)
    
    # Handling invalid or token already blacklisted
    except TokenError as e:
        return Response({'error': f'Invalid or expired token: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({'error': f'An error occurred during logout: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)