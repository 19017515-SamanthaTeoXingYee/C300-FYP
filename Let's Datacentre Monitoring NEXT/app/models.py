from django.db import models

# Create your models here.
class App(models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return str(self.item)

class Post(models.Model):
   post_heading = models.CharField(max_length=200)
   post_text = models.TextField()
   
   def __str__(self):
      return unicode(self.post_heading)