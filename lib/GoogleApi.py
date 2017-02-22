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

    def delete_agency(self, agency_id):
        url = 'https://lineparty-api.line-apps-rc.com/v1/agency/{_id}'.format(_id=agency_id)

        return self.request.delete(url)

    def delete_beacon(self, beacon_id):
        url = 'https://lineparty-api.line-apps-rc.com/v1/beacon/{_id}'.format(_id=beacon_id)

        return self.request.delete(url)
