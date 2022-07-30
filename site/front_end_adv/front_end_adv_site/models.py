from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

CATEGORY = (
    (0, "General"),
    (1, "Web"),
    (2, "Desktop"),
    (3, "Mobile"),
    (4, "Cloud"),
    (5, "Design"),
    (6, "Architecture")
)

class Post(models.Model):
    """Model definition for MODELNAME."""

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    image: models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=CATEGORY, default=0)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'ADVENTURE POST'
        verbose_name_plural = 'ADVENTURES POSTS'
        ordering = ["-created_on"]

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.title
