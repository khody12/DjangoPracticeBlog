from django.db import models

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.caption}"
class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=500)
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(default="",null=False,db_index=True)

    content = models.TextField(max_length=10000)

    caption = models.ManyToManyField(Tag)

    

    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name="posts")

    def __str__(self):
        return f"{self.title} {self.author}"

    
class Comment(models.Model):
    comment = models.CharField(max_length=300)

    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="all_comments")