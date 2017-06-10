from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import signup
from .forms import LogInForm


app_name = 'users'

urlpatterns = [
    url(r'^signup/', signup, name='signup'),
    url(r'^login/', login, {'template_name': 'users/login.html', 'authentication_form': LogInForm}, name='login'),
    url(r'^logout/', logout, {'next_page': '/'}, name='logout')
]
