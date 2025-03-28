from django.db import models

# Create your models here.
class students(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.title