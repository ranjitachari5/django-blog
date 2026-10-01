from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    class Meta:
        verbose_name_plural='categories'
    def __str__(self):
        return self.category_name
    