from django.db import models

# Create your models here.

class About(models.Model):
    
    title = models.CharField(max_length=30)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Blog Admin: {self.title} - about Section"