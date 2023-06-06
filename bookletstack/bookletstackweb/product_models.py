from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from .user_models import *

class Book(models.Model):
    
    CATEGORY_CHOICES = [
        ('money', 'Money'),
        ('business', 'Business'),
        ('coding', 'Coding'),
        ('skills', 'Skills'),
        ('case_studies', 'Case Studies'),
        # Add more categories as needed
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    cover = models.ImageField(upload_to='book_covers/')
    pdf = models.FileField(upload_to='books/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    description = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    price = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
    
    def update_average_rating(self):
        total_ratings = self.comments.exclude(rated=0).count()
        if total_ratings > 0:
            average_rating = self.comments.exclude(rated=0).aggregate(models.Avg('rated'))['rated__avg']
            self.rating = round(average_rating, 2)
        else:
            self.rating = 0
        self.save()
    
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rated = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    
    def __str__(self):
        return f"Comment by {self.buyer.username} on {self.book.name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.update_average_rating()