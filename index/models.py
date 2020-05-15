from django.db import models

class Topic(models.Model):
    header = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.header}::({self.link})::{self.description}"