from django.db import models


GENRE_CHOICES = (
    ("Fantasy", "Fantasy"),
    ("Literary", "Literary"),
    ("Mystery", "Mystery"),
    ("Non-Fiction", "Non-Fiction"),
    ("Science Fiction", "Science Fiction"),
    ("Thriller", "Thriller"),
    
)

class Ebook(models.Model):
  Title = models.TextField(blank=False,null=False)
  Author = models.TextField(blank=False,null=False)
  Genre =  models.CharField(max_length = 20,choices = GENRE_CHOICES,default = 'Fantasy',blank=False,null=False)
  Review = models.IntegerField(blank=False,null=False)
  Favorite = models.BooleanField(default=True, blank=False,null=False)
      
  def __str__(self):
    return self.Title








 




