# encoding: utf-8

import sys, inspect

from workflow import Workflow, notify

from config import create_config
import request.device as device
from remo_client import RemoClient


class RemoCommand:
    def show_temperature_and_humidity(self, wf):
        req = device.ListRequest(create_config())
        dic = RemoClient.call(req)
        newest_events = dic[0]['newest_events']
        temp = newest_events['te']['val']
        humo = newest_events['hu']['val']
        text = u"室温: %0.2f度\\n湿度: %0.2f％" % (temp, humo)
        notify.notify(u'室温と湿度', text)
        wf.add_item(title = text, icon='icon.png', arg = text, valid = True)
        wf.send_feedback()


COMMAND_DICT = {}
for func_name, func in inspect.getmembers(RemoCommand(), inspect.ismethod):
    COMMAND_DICT[func_name] = func


if __name__ == '__main__':
    key = sys.argv[1]
    wf = Workflow()
    sys.exit(wf.run(COMMAND_DICT[key]))
