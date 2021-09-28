import requests
import json
import logging
import urllib3
import os, sys

sys.path.append(os.path.dirname(os.getcwd()))
print(sys.path)
from exceptions.http_exceptions import HTTPServerError, HTTPClientError

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(name)s - %(message)s')

class httpOperation():
    """A simple class that does the HTTP CRUD operation(GET, POST, PUT, DELETE, )"""
    log = logging.getLogger('httpOperation')

    def __init__(self, baseUrl, token):
        self.baseUrl = baseUrl
        self.token = token

    def httpGet(self, getUrlPath, **kwargs):

        """
        Implemented HTTP GET request with try/catch block
        Try: This block will test the excepted error to occur
        Except:  Here you can handle the error
        Else: If there is no exception then this block will be executed
        Finally: Finally block always gets executed either exception is generated or not
        """
        headers = {}
        headers['Authorization'] = 'Bearer {}'.format(self.token)
        headers['Content-Type'] = 'application/json'
        self.log.debug(headers)

        httpGetUrl = self.baseUrl + '/' + getUrlPath
        self.log.debug(httpGetUrl)
        try:
            resp = requests.get(httpGetUrl, headers=headers)
            resp.raise_for_status()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as connErr:
            self.log.error(connErr)
        except requests.exceptions.HTTPError:
            if str(resp.status_code).startswith('5'):
                self.log.error("Server Error: %s \n%s", resp.status_code, resp.headers)
                raise HTTPServerError from Exception

            self.log.error("Client Error: %s \n%s", resp.status_code, resp.headers)
            raise HTTPClientError from Exception
        else:
            self.log.info("Request completed successfully: %s %s", resp.status_code, resp.headers)
            return resp.text
        return None
