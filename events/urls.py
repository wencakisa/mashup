from django.conf.urls import url

from .views import (
    EventList, EventDetail, EventCreate, EventUpdate, EventDelete, EventGoing, EventNotGoing
)


urlpatterns = [
    url(r'^$', EventList.as_view(), name='event-list'),
    url(r'^(?P<pk>\d+)/$', EventDetail.as_view(), name='event-detail'),
    url(r'^add/$', EventCreate.as_view(), name='event-create'),
    url(r'^(?P<pk>\d+)/edit/$', EventUpdate.as_view(), name='event-edit'),
    url(r'^(?P<pk>\d+)/delete/$', EventDelete.as_view(), name='event-delete'),
    url(r'^(?P<pk>\d+)/going/$', EventGoing.as_view(), name='event-going'),
    url(r'^(?P<pk>\d+)/notGoing/$', EventNotGoing.as_view(), name='event-not-going'),
]
