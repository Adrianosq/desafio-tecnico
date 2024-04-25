from django.db import models
from users.models import User


class ToDo(models.Model):
    class Meta:
        ordering = ("id",)
    
    description = models.TextField()
    status = models.BooleanField(default=False)

    user = models.ForeignKey(
        "users.User", 
        on_delete=models.CASCADE,
        related_name="albums",
    )
