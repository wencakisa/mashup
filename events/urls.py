from django.conf.urls import url

from .views import EventList, EventDetail, EventCreate, EventUpdate, EventDelete


urlpatterns = [
    url(r'^$', EventList.as_view(), name='event-list'),
    url(r'^(?P<pk>\d+)/$', EventDetail.as_view(), name='event-detail'),
    url(r'^add/$', EventCreate.as_view(), name='event-create'),
    url(r'^edit/(?P<pk>\d+)/$', EventUpdate.as_view(), name='event-edit'),
    url(r'^delete/(?P<pk>\d+)/$', EventDelete.as_view(), name='event-delete'),
]
