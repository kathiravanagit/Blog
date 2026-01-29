from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from google.cloud import firestore

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100, default='Anonymous')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image_url = models.URLField(max_length=500, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
    content = models.TextField()
    
    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"
    
    def __str__(self):
        return "About Us"

# Firebase sync signals
@receiver(post_save, sender=AboutUs)
def sync_aboutus_to_firebase(sender, instance, **kwargs):
    from myapp.firebase_config import get_db
    db = get_db()
    db.collection('aboutus').document('content').set({
        'content': instance.content,
        'updated_at': firestore.SERVER_TIMESTAMP
    })

@receiver(post_save, sender=Category)
def sync_category_to_firebase(sender, instance, **kwargs):
    from myapp.firebase_config import get_db
    db = get_db()
    db.collection('categories').document(str(instance.id)).set({
        'name': instance.name,
        'description': instance.description,
        'created_at': instance.created_at.isoformat() if instance.created_at else None
    })

@receiver(post_delete, sender=Category)
def delete_category_from_firebase(sender, instance, **kwargs):
    from myapp.firebase_config import get_db
    db = get_db()
    db.collection('categories').document(str(instance.id)).delete()
     