# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from api import views
from .utils import TestUtils


class TestAuth(APITestCase):
    def setUp(self):
        self.uri = '/customers/'
        self.view = views.CustomerList.as_view()
        self.factory = APIRequestFactory()
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.superuser = self.setup_superuser()
        self.superuser_token = Token.objects.create(user=self.superuser)
        self.superuser_token.save()
        self.utils = TestUtils()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'user',
            email='testuser@test.com',
            password='test'
        )

    @staticmethod
    def setup_superuser():
        User = get_user_model()
        return User.objects.create_superuser(
            'superuser',
            email='superuser@test.com',
            password='test'
        )

    def test_should_return_unauthorized_when_request_has_no_authentication_credentials(self):
        request = self.factory.get(
            self.uri
        )

        response = self.view(request)

        expected_response_status_code = 401
        expected_response_body = {
            'detail': 'Authentication credentials were not provided.'
        }

        self.utils.assert_response(
            response,
            expected_response_status_code,
            expected_response_body
        )

    def test_should_return_unauthorized_when_request_has_invalid_authentication_credentials(self):
        request = self.factory.get(
            self.uri,
            HTTP_AUTHORIZATION='Token xxx'
        )

        response = self.view(request)

        expected_response_status_code = 401
        expected_response_body = {
            'detail': 'Invalid token.'
        }

        self.utils.assert_response(
            response,
            expected_response_status_code,
            expected_response_body
        )

    def test_should_return_forbidden_when_user_has_no_access_to_resource(self):
        request = self.factory.get(
            self.uri,
            HTTP_AUTHORIZATION='Token {}'.format(self.token.key)
        )

        request.user = self.user
        response = self.view(request)

        expected_response_status_code = 403
        expected_response_body = {
            'detail': 'You do not have permission to perform this action.'
        }

        self.utils.assert_response(
            response,
            expected_response_status_code,
            expected_response_body
        )

    def test_should_return_success_when_user_has_access_to_resource(self):
        request = self.factory.get(
            self.uri,
            HTTP_AUTHORIZATION='Token {}'.format(self.superuser_token.key)
        )

        request.user = self.user
        response = self.view(request)

        expected_response_status_code = 200
        expected_response_body = {
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        }

        self.utils.assert_response(
            response,
            expected_response_status_code,
            expected_response_body
        )
