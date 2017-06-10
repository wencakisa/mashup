from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='website/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='website/about.html'), name='about')
]