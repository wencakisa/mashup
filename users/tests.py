from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User


class SignUpViewTestCase(TestCase):
    def setUp(self):
        self.app_name = 'users'
        self.view_name = 'signup'
        self.url_name = '{}:{}'.format(self.app_name, self.view_name)
        self.url = reverse(self.url_name)

        self.template_name = 'users/signup.html'

        self.user = User.objects.create_user(username='user', password='123456')
        self.user_creation_dict = {
            'username': 'test_user',
            'first_name': 'foobar',
            'last_name': 'barfoo',
            'email': 'foo@bar.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }

    def test_sign_up_template_rendered_on_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(self.template_name)

    def test_sign_up_with_existing_username(self):
        self.user_creation_dict['username'] = self.user.username

        response = self.client.post(self.url, self.user_creation_dict)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'].errors)
        self.assertEqual(
            response.context['form'].errors['username'],
            ['A user with that username already exists.']
        )

    def test_sign_up_with_non_matching_passwords(self):
        self.user_creation_dict['password2'] = 'somethingdifferent321'

        response = self.client.post(self.url, self.user_creation_dict)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'].errors)
        self.assertEqual(
            response.context['form'].errors['password2'],
            ['The two password fields didn\'t match.']
        )

    def test_sign_up_with_valid_credentials(self):
        response = self.client.post(self.url, self.user_creation_dict, follow=True)

        self.assertRedirects(response, expected_url='/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated())


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.app_name = 'users'
        self.view_name = 'login'
        self.url_name = '{}:{}'.format(self.app_name, self.view_name)
        self.url = reverse(self.url_name)

        self.template_name = 'users/login.html'

        self.user = User.objects.create_user(
            username='test',
            first_name='foo',
            last_name='bar',
            password='123456'
        )
        self.user_login_dict = {
            'username': self.user.username,
            'password': '123456'
        }

    def test_login_template_rendered_on_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(self.template_name)

    def test_login_with_invalid_username_password_combination(self):
        self.user_login_dict['username'] = 'foobar'

        response = self.client.post(self.url, self.user_login_dict, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(self.template_name)
        self.assertIsNotNone(response.context['form'].errors)
        self.assertFalse(response.context['user'].is_authenticated())

    def test_login_with_valid_credentials(self):
        response = self.client.post(self.url, self.user_login_dict, follow=True)

        self.assertRedirects(response, expected_url='/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated())


class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.app_name = 'users'
        self.view_name = 'logout'
        self.url_name = '{}:{}'.format(self.app_name, self.view_name)
        self.url = reverse(self.url_name)

        self.user = User.objects.create_user(
            username='test',
            first_name='foo',
            last_name='bar',
            password='123456'
        )

    def test_logout(self):
        self.client.force_login(self.user)

        response = self.client.post(self.url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, expected_url='/')
        self.assertFalse(response.context['user'].is_authenticated())


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.app_name = 'users'
        self.view_name = 'profile'
        self.url_name = '{}:{}'.format(self.app_name, self.view_name)

        self.user = User.objects.create_user(
            username='test',
            first_name='foo',
            last_name='bar',
            password='123456'
        )

    def test_profile_with_invalid_user_id(self):
        pass

    def test_profile_with_valid_user_id(self):
        pass
