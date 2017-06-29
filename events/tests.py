from datetime import datetime

from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Event


class EventDefaultTestCase(TestCase):
    def setUp(self):
        self.app_name = 'events'

        self.user = User.objects.create_user(username='user', password='123456')

        now = datetime.now()
        self.event = Event.objects.create(
            title='myevent',
            host=self.user,
            from_ts=now,
            to_ts=now,
            photo=SimpleUploadedFile(
                name='mashup_logo.jpg',
                content=open('static/images/mashup_logo.jpg', 'rb').read(),
                content_type='image/jpeg'
            )
        )

    def get_full_url(self, view_name, *args, **kwargs):
        return reverse('{}:{}'.format(self.app_name, view_name), kwargs=kwargs.get('kwargs'))

    def get_full_template_name(self, template_name):
        return '{}/{}'.format(self.app_name, template_name)


class EventListViewTestCase(EventDefaultTestCase):
    def setUp(self):
        super().setUp()

        self.url = self.get_full_url('event-list')
        self.template_name = self.get_full_template_name('list.html')

    def test_event_list_with_non_authenticated_user(self):
        response = self.client.get(self.url, follow=True)

        self.assertRedirects(response, expected_url='/login/?next=%2Fevents%2F')
        self.assertTemplateNotUsed(self.template_name)
        self.assertEqual(response.status_code, 200)

    def test_event_list_with_authenticated_user(self):
        self.client.force_login(self.user)

        response = self.client.get(self.url)

        self.assertIn(self.event, response.context['event_list'])
        self.assertTemplateUsed(self.template_name)
        self.assertEqual(response.status_code, 200)


class EventDetailViewTestCase(EventDefaultTestCase):
    def setUp(self):
        super().setUp()

        self.url_name = 'event-detail'
        self.template_name = self.get_full_template_name('detail.html')

    def test_event_detail_with_non_authenticated_user(self):
        response = self.client.get(
            self.get_full_url(self.url_name, kwargs={'pk': self.event.id}),
            follow=True
        )

        self.assertRedirects(response, expected_url='/login/?next=%2Fevents%2F1%2F')
        self.assertEqual(response.status_code, 200)

    def test_event_detail_with_invalid_event_id(self):
        self.client.force_login(self.user)

        response = self.client.get(
            self.get_full_url(self.url_name, kwargs={'pk': self.event.id + 1})
        )

        self.assertEqual(response.status_code, 404)

    def test_event_detail_with_valid_event_id(self):
        self.client.force_login(self.user)

        response = self.client.get(
            self.get_full_url(self.url_name, kwargs={'pk': self.event.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.event.title, response.context['event'].title)
