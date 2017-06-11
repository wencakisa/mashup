from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(unique=True, max_length=50)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=100000, blank=True)
    from_ts = models.DateTimeField()
    to_ts = models.DateTimeField()
    photo = models.ImageField(upload_to='static/event_photos/')
    tickets_url = models.URLField(blank=True)
    # place = ... (GeoDjango)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{} by {}'.format(self.title, self.host)
