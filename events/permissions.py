from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class LoginRequired(LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'next'


class IsEventHost(PermissionRequiredMixin):
    permission_required = 'event.is_host'
