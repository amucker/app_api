from django.test import TestCase
from django.test import Client


class TestApi(TestCase):
    def setUp(self):
        self.client = Client()
        self.foo = 'hello'
        self.bar = 'world'

    def test_api(self):
        data = {
            'foo': self.foo,
            'bar': self.bar
        }
        response = self.client.post('/api/', data=data)
        self.assertEqual(response.status_code, 200)

        result = response.json()
        self.assertEqual(result['msg'], 'hello world')
