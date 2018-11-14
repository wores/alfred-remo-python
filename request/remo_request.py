# encoding: utf-8

import urllib2, urllib
from abc import ABCMeta, abstractmethod
import os

from workflow import Workflow
class RemoRequest(object):
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self._token = config.access_token
        self._baseUrl = 'https://api.nature.global/'
        self._api_version = 1

    def _make_url(self, path):
        url = '%s%d/' % (self._baseUrl, self._api_version)
        url = os.path.join(url, path)
        return url

    def _encode_param(self, param_dic={}):
        return urllib.urlencode(param_dic)

    def _add_common_header(self, req):
        req.add_header("Authorization", "Bearer " + self._token)
        req.add_header("accept", "application/json")
        req.add_header("User-Agent", "py-workflow-remo")
        return req

    def build_request(self):
        url = self._make_url(self.path())
        encoded_param = None

        if self.param() is not None:
            encoded_param = self._encode_param(self.param())

        req = None
        if self.method() == 'GET':
            if encoded_param is not None:
                url += '?{0}'.format(encoded_param)
            req = urllib2.Request(url)
        else:
            req = urllib2.Request(url)
            req.add_data(encoded_param)

        req = self._add_common_header(req)
        return req

    def param(self):
        return None

    @abstractmethod
    def method(self):
        raise NotImplementedError

    @abstractmethod
    def path(self):
        raise NotImplementedError
