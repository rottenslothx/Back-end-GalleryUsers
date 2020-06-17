from django.db import models

# Create your models here.
from untitled1 import settings


class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(blank=False, null=False)
    avg_rating = models.FloatField(default=0)
    review_count = models.IntegerField(default=0)
    user_uploaded = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      related_name='user_uploaded', null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Review (models.Model):
    post = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=100, blank=True, default='')
    rating = models.PositiveIntegerField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user', null=True, blank=True)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = [
            'user', 'post'
        ]

    def __str__(self):
        return self.review_text

