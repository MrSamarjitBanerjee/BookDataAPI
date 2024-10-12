from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from Auth.api.views import RegistrationView,LogoutView

urlpatterns = [
    # JWT login endpoint
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', RegistrationView, name='Register'),
    path('logout/', LogoutView, name='logout'),


]