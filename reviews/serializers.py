from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Book, Review, Genre
from django.contrib.auth.models import User

class BookBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id' , 'title'] 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username'] 

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ReviewSerializer(serializers.ModelSerializer):
    book = BookBriefSerializer() 
    user = UserSerializer()   
    class Meta:
        model = Review
        fields = ['book', 'user', 'rating', 'comment', 'created_at']



class ReviewCreateSerializer(serializers.ModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(source='book', queryset=Book.objects.all(), write_only=True)  # Accepts book ID
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Review
        fields = ['id', 'book_id', 'user', 'rating', 'comment', 'created_at']

    def create(self, validated_data):
        review = Review.objects.create(**validated_data)
        return review
    


class BookSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'genres', 'release_date', 'avg_rating','review_count']
    
    def get_review_count(self, obj):
        return obj.reviews.count() 
    
    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]
   
class BookReviewSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='book.title', read_only=True)  
    user = UserSerializer()
    class Meta:
        model = Review
        fields = ['user','id', 'book_name', 'rating', 'comment']

class BookCreateSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'genres', 'release_date', 'avg_rating']

  