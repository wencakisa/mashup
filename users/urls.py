from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import SignUpView, ProfileView
from .forms import LogInForm


urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'users/login.html', 'authentication_form': LogInForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name='profile')
]
