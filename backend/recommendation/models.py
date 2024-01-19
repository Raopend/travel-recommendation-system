from django.db import models


class Tours(models.Model):
    location_id = models.IntegerField()
    display_name = models.CharField(max_length=255)
    url = models.URLField()
    cover_image = models.URLField()
    reviews_count = models.IntegerField()
    tags_desc = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    review_rating = models.FloatField()
    feature_reviews = models.TextField()

    class Meta:
        verbose_name = "tours"
