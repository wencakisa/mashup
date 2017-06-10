from django.conf.urls import url

from .views import EventList, EventDetail, EventCreate


urlpatterns = [
    url(r'^$', EventList.as_view(), name='event-list'),
    url(r'^(?P<pk>\d+)/$', EventDetail.as_view(), name='event-detail'),
    url(r'^add/$', EventCreate.as_view(), name='event-create'),
]