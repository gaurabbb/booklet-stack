from django.contrib.auth.models import User
from django.db import models

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email, self.user.first_name
