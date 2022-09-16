from django.db import models

class Asset(models.Model):
    assetName = models.CharField(max_length=200)
    assetCategory = models.CharField(max_length=200)
    assetQuantity = models.FloatField(max_length=200)
    assetPrice = models.FloatField(max_length=200)
    assetTotal = models.FloatField(max_length=200)
    assetDetails = models.CharField(max_length=500)

    def __str__(self):
        return self.assetName + ' ' + self.assetCategory