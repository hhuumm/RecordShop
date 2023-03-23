from django.db import models

class Listing(models.Model):
    listing_id = models.IntegerField()
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    catno = models.CharField(max_length=100)
    format = models.CharField(max_length=100)
    release_id = models.IntegerField()
    status = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    listed = models.DateTimeField()
    comments = models.TextField()
    media_condition = models.CharField(max_length=20)
    sleeve_condition = models.CharField(max_length=20)
    accept_offer = models.BooleanField()
    external_id = models.CharField(max_length=100)
    weight = models.IntegerField()
    format_quantity = models.IntegerField()
    location = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title