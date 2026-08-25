from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Story(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='stories')
    content = models.TextField(help_text="Nội dung truyện")
    audio_url = models.URLField(blank=True, null=True, help_text="Link file âm thanh (nếu có)")
    cover_image_url = models.URLField(blank=True, null=True, help_text="Link ảnh bìa")
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Stories"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

