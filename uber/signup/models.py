from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    mobile_verified = models.BooleanField()
    user_id = models.UUIDField()

    def __str__(self) -> str:
        return self.first_name
