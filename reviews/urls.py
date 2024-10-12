from django.urls import path
from .views import ( 
    BookCreateView,GenreCRUDViewSet,BookListView, BookDetailView, ReviewCreateView , 
    ReviewDetailView , ReviewListView, BookReviewsView,  BookUpdateDeleteView , ReviewUpdateDeleteView
)
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'genres', GenreCRUDViewSet, basename='genre')
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'), # List of all Books
    path('books/<int:book_id>/reviews/', BookReviewsView.as_view(), name='book-reviews'), # All Reviews of particular book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # particular book detail By Book Id 
    path('books/create/', BookCreateView.as_view() , name='BookCreate'), # Create New Book
    path('reviews/', ReviewListView.as_view(), name='review-list'), # List all reviews
    path('books/<int:pk>/edit/', BookUpdateDeleteView.as_view(), name='book-update-delete'), # Update,delete a Book (adminonly)
    path('reviews/<int:pk>/edit/', ReviewUpdateDeleteView.as_view(), name='review-update-delete'), #Update,delete review (adminOnly)
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'), # See Particular Review
    path('reviews/create/',ReviewCreateView.as_view() , name = 'review-create'), # Create a Review
    

]
urlpatterns += router.urls