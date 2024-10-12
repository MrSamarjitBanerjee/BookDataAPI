from django.contrib import admin
from .models import Genre, Book, Review

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)  

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at') 
    search_fields = ('user__username', 'book__title') 

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_date', 'avg_rating') 
    search_fields = ('title', 'author') 
    list_filter = ('genres',) 
    filter_horizontal = ('genres',)  

admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
