import logging
import requests
import json


class Request():

    def post(self, url, headers, payload, cookies):
        self._log_payload(payload)
        res = requests.post(url, headers=headers,
                            json=payload, cookies=cookies)
        return self._validate_response(res)

    def get(self, url, headers, payload, cookies):
        self._log_payload(payload)
        res = requests.get(url, headers=headers,
                           params=payload, cookies=cookies)
        return self._validate_response(res)

    def delete(self, url):
        self._log_payload(url)
        res = requests.delete(url)
        return self._validate_response(res)

    def _validate_response(self, res):
        self._check_response_statuscode(res)
        return self._get_response(res)

    def _log_payload(self, payload):
        logging.log('Payload: {payload}'.format(payload=payload))

    def _check_response_statuscode(self, res):
        if str(res.status_code)[:2] != '20':
            logging.log(str(res.status_code)[:2])
            log_message = 'Request URL: {url}\nHeader: {header}\nCookies: {cookies}'.format(
                url=res.url, header=res.headers, cookies=res.cookies)
            logging.log(log_message)
            raise AssertionError('Response code is not 200, response:\n' + res.text + '\nResopnse code: ' + str(res.status_code))

    def _get_response(self, res):
        if res:
            try:
                return res.json()
            except:
                logging.log('Response is not JSON format, response: {res}'.format(res=res.text))
