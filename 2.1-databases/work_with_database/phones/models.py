from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    price = models.IntegerField()
    release_date = models.CharField(max_length=50)
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs) - models






    # id = models.CharField(max_length=50, primary_key=True)
    # name = models.CharField(max_length=50)
    # price = models.PositiveIntegerField
    # image = models.URLField(max_length=200)
    # release_date = models.TimeField(max_length=50)
    # lte_exists = models.BooleanField
    # slug = models.SlugField(max_length=50, db_column=name, unique=True)

