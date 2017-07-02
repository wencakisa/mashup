from datetime import datetime

from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.shortcuts import redirect, reverse, get_object_or_404
from django.urls import reverse_lazy

from .models import Event
from .forms import EventForm
from .permissions import LoginRequired, IsEventHost


class EventList(LoginRequired, ListView):
    model = Event


class EventDetail(LoginRequired, DetailView):
    model = Event


class EventCreate(LoginRequired, FormView):
    template_name = 'events/event_form.html'
    form_class = EventForm

    def get_datetime(self, date, time):
        datetime_format = '%d %B, %Y %I:%M%p'
        datetime_str = '{} {}'.format(date, time)

        return datetime.strptime(datetime_str, datetime_format)

    def post(self, request, *args, **kwargs):
        data = request.POST

        event = Event.objects.create(
            title=data.get('title'),
            host=request.user,
            description=data.get('description', ''),
            from_ts=self.get_datetime(data.get('from_date'), data.get('from_time')),
            to_ts=self.get_datetime(data.get('to_date'), data.get('to_time')),
            photo=request.FILES.get('photo'),
            tickets_url=data.get('tickets_url', '')
        )

        return redirect(reverse('events:event-detail', kwargs={'pk': event.id}))


class EventUpdate(IsEventHost, LoginRequired, UpdateView):
    model = Event
    fields = ['title', 'description', 'tickets_url', 'photo']
    template_name_suffix = '_update_form'


class EventDelete(IsEventHost, LoginRequired, DeleteView):
    model = Event
    success_url = reverse_lazy('events:event-list')


class EventGoingAbstract(LoginRequired, UpdateView):
    model = Event
    fields = ['people_going']

    def do_action(self, request, event):
        raise NotImplementedError()

    def post(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=kwargs['pk'])
        self.do_action(request, event)
        event.save()

        return redirect(reverse('events:event-detail', kwargs={'pk': kwargs['pk']}))


class EventGoing(EventGoingAbstract):
    def do_action(self, request, event):
        event.people_going.add(request.user)


class EventNotGoing(EventGoingAbstract):
    def do_action(self, request, event):
        event.people_going.remove(request.user)
