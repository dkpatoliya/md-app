from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    # def __getitem__(self, item):
    #     return getattr(self, item)
    def __str__(self):
        return self.text[0:50]
