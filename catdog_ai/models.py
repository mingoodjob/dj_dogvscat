from django.db import models

class Pet(models.Model):
    PET_CHOICES = (
        ('cat', 'cat'),
        ('dog', 'dog'),
    )

    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    classification = models.CharField(max_length=10, choices=PET_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.classification