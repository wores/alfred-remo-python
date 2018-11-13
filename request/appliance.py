# encoding: utf-8

from remo_request import RemoRequest


class ListRequest(RemoRequest):
    u"""
    登録済みの機器一覧を取得する
    """

    def __init__(self, config):
        super(ListRequest, self).__init__(config)

    def method(self):
        return 'GET'

    def path(self):
        return 'appliances'

