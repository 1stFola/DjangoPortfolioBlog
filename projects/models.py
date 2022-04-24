from pyexpat import model
from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.TextField(
        default="https://files.realpython.com/media/13-Python-Projects-for-Intermediate-Developers_Watermarked.bb98d44bdb10.jpg"
        )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
