import os
import sys
from ApiTester.request import Request

GOOGLE_KEY = os.environ.get('GOOGLE_KEY', '')
GOOGLE_CX = os.environ.get('GOOGLE_CX', '')


class GoogleApi():

    def __init__(self):
        self.request = Request()

    def search_api(self, keyword):
        url = 'https://www.googleapis.com/customsearch/v1'
        payload = {
            'key': GOOGLE_KEY,
            'cx': GOOGLE_CX,
            'q': keyword
        }
        return self.request.get(url, None, payload, None)

    def return_url(self):
        url = 'https://www.googleapis.com/customsearch/v1'

        return url
