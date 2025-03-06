from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class DiaryEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy 😊'),
        ('sad', 'Sad 😢'),
        ('angry', 'Angry 😠'),
        ('excited', 'Excited 🎉'),
        ('neutral', 'Neutral 😐'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title