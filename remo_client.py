# encoding: utf-8

import os, json
import urllib2

from workflow import Workflow


class RemoClient:

    @classmethod
    def call(self, remo_request):
        req = remo_request.build_request()
        res = urllib2.urlopen(req)
        text = res.read()
        dic = json.loads(text)
        return dic
