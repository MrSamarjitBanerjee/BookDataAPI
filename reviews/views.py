from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from .models import Book, Review, Genre
from .serializers import BookReviewSerializer,BookSerializer, ReviewSerializer, GenreSerializer , BookCreateSerializer, ReviewCreateSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated , IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3 
    page_size_query_param = 'page_size'
    max_page_size = 10

class CustomAnonRateThrottle(AnonRateThrottle):
    rate = '10/min'

class CustomUserRateThrottle(UserRateThrottle):
    rate = '15/min'


class BookReviewsView(generics.ListAPIView):
    serializer_class = BookReviewSerializer
    throttle_classes = [CustomAnonRateThrottle]

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book__id=book_id)

    def list(self, request, *args, **kwargs):
        book_id = self.kwargs['book_id']
        book = get_object_or_404(Book, id=book_id)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'reviews': serializer.data  
        }, status= status.HTTP_200_OK)


# LIST OF BOOKS (ANYONE CAN VIEW)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all().order_by('avg_rating')
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author', 'genres__name') 
    pagination_class = StandardResultsSetPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [CustomAnonRateThrottle,CustomUserRateThrottle]
     


      

  # Create New Book (Only Admin)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

# Search a Book by ID (ANYONE CAN VIEW)
class BookDetailView(generics.RetrieveAPIView):
    throttle_classes = [AnonRateThrottle]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [CustomAnonRateThrottle,CustomUserRateThrottle]

# SEE REVIEWS(ANYONE CAN)
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [CustomAnonRateThrottle,CustomUserRateThrottle]
  

# ALL AUTHENTICATED USER CAN POST REVIEW
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [CustomAnonRateThrottle,CustomUserRateThrottle]

# Search Review By ID (ANYONE CAN)
class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [CustomAnonRateThrottle,CustomUserRateThrottle]

# ADMIN CAN SEE OR CREATE NEW GENRE
class GenreCRUDViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer  # Using create serializer for update as well
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]  # Only admin can update or delete

# Review Update and Delete View (Only Admin)
class ReviewUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer  # Using create serializer for update as well
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser] 


