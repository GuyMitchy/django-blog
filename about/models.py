from django.db import models

# Create your models here.

class About(models.Model):
    
    title = models.CharField(max_length=30)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Blog Admin: {self.title} - about Section"
    
class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"    