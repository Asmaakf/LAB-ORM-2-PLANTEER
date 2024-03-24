from django.db import models

# Create your models here.
class Plant(models.Model):
    categories = models.TextChoices("Category", ["fruit", "aromatic", "flowers"])
    
    name = models.CharField(max_length=2000)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=64)
    native_to = models.CharField(max_length=2000) 
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    #string representation
    def __str__(self):
        return self.name