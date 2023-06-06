from django.contrib import admin
from django import forms
from .models import Book, UserDetails
from django.core.files.storage import default_storage

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('rating',)

    def get_readonly_fields(self, request, obj=None):
        # Make rating field read-only for existing books
        if obj:
            return self.readonly_fields + ('rating',)
        return self.readonly_fields
    
    def delete_queryset(self, request, queryset):
        # Delete the associated PDF and cover files for each book in the queryset
        for book in queryset:
            # Delete the PDF file
            if book.pdf:
                path = book.pdf.path
                if default_storage.exists(path):
                    default_storage.delete(path)

            # Delete the cover image file
            if book.cover:
                path = book.cover.path
                if default_storage.exists(path):
                    default_storage.delete(path)

        # Call the parent method to perform the actual deletion of the queryset
        super().delete_queryset(request, queryset)
        
        
admin.site.register(Book, BookAdmin)
admin.site.register(UserDetails)