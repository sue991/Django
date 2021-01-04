from django.db import models

# Create your models here.


class Blog(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length = 200)

    pub_date = models.DateTimeField('date_published')

    body = models.TextField()

    def summary(self):
        return self.body[:100]
