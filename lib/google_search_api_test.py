import os
import sys
from ApiTester.request import Request

GOOGLE_KEY = os.environ.get('GOOGLE_KEY', '')
GOOGLE_CX = os.environ.get('GOOGLE_CX', '')

request = Request()


def search_api(keyword):

    url = 'https://www.googleapis.com/customsearch/v1'
    payload = {
        'key': GOOGLE_KEY,
        'cx': GOOGLE_CX,
        'q': keyword
    }
    return request.get(url, None, payload, None)
