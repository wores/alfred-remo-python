# encoding: utf-8

from remo_request import RemoRequest


class ListRequest(RemoRequest):

    def __init__(self, config):
        super(DeviceList, self).__init__(config)

    def method(self):
        return 'GET'

    def path(self):
        return 'devices'
