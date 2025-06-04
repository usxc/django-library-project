from django.contrib import admin
from .models import Book, Rental

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('author', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rental_date', 'return_due_date', 'is_returned', 'returned_at')
    search_fields = ('book__title', 'user__username', 'user__student_id')
    list_filter = ('is_returned', 'user', 'book', 'rental_date')
    autocomplete_fields = ['book', 'user']
    readonly_fields = ('id', 'created_at', 'updated_at', 'rental_date', 'returned_at')