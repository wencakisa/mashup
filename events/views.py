from datetime import datetime

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, reverse

from .models import Event


class EventList(ListView):
    model = Event


class EventDetail(DetailView):
    model = Event
    

class EventCreate(CreateView):
    model = Event
    fields = ['title', 'description', 'from_ts', 'to_ts', 'photo']

    def post(self, request, *args, **kwargs):
        data = request.POST

        ts_format = '%d %B, %Y %I:%M%p'

        from_date = data.get('from_date')
        from_time = data.get('from_time')
        from_ts_str = '{} {}'.format(from_date, from_time)

        from_ts = datetime.strptime(from_ts_str, ts_format)

        to_date = data.get('to_date')
        to_time = data.get('to_time')
        to_ts_str = '{} {}'.format(to_date, to_time)

        to_ts = datetime.strptime(to_ts_str, ts_format)

        event = Event.objects.create(
            title=data.get('title'),
            host=request.user,
            description=data.get('description', ''),
            from_ts=from_ts,
            to_ts=to_ts,
            photo=request.FILES.get('photo')
        )

        return redirect(reverse('events:event-list'))
