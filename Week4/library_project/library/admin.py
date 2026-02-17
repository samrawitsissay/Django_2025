from django.contrib import admin

# Register your models here.
from .models import Author, Book, Member, Category, Loan


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "available_copies")
    list_filter = ("author", "categories")
    search_fields = ("title", "isbn")


admin.site.register(Author)
admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Loan)
