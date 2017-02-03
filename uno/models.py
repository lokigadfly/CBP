from django.db import models

# Create your models here.
class Room(models.Model):
    Choice = (
        (1, u'直播'),
        (2, u'录播')
    )
    Category=(
        (1, u'艺术之光'),
        (2, u'文明之光'),
        (3, u'科技之光'),
        (4, u'产业之光'),
        (5, u'信仰的力量'),
    )
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description=models.TextField()
    creator = models.CharField(max_length=100)
    choice = models.PositiveIntegerField(choices=Choice)
    category=models.PositiveIntegerField(choices=Category)
    getsrs=models.CharField(max_length=500)

