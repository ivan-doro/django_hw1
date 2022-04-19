from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=50, default='')

    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Phone, self).save(*args, **kwargs)


