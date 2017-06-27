from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from events.models import Event

from .forms import SignUpForm


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            form.save()

            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )

            login(request, user)

            return redirect('/')


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user

        user.hosted_events = Event.objects.filter(host=user)
        user.events_going = Event.objects.filter(people_going__in=[user])

        return render(request, self.template_name, {'user': user})
