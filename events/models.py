from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Event(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=50)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=100000, blank=True)
    from_ts = models.DateTimeField()
    to_ts = models.DateTimeField()
    tickets_url = models.URLField(blank=True)
    photo = models.ImageField(upload_to='static/event_photos/')
    people_going = models.ManyToManyField(User, related_name='going')


    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} by {}'.format(self.title, self.host)
