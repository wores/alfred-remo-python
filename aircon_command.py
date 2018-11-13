# encoding: utf-8

import sys
import inspect

from workflow import Workflow, notify

from config import create_config
import request.aircon as aircon
import request.appliance as appliance
from remo_client import RemoClient


class AirconCommand:
    def show_status(self, wf):
        config = create_config()
        req = appliance.ListRequest(config)
        dicts = RemoClient.call(req)
        aircon = None
        for dic in dicts:
            if dic['id'] == config.aircon_id:
                aircon = dic['settings']
                break

        if aircon is None:
            text = u'エアコンが登録されてないっぽい'
            wf.add_item(title = text, icon='icon.png', arg = text, valid = False)
            wf.send_feedback()
            return

        power_state = aircon.get('button', '')
        aircon['button'] = 'ON' if len(power_state) == 0 else 'OFF'
        text = u"設定温度: {temp}度\\nモード: {mode}\\nvol: {vol}\\n電源: {button}".format(**aircon)
        notify.notify(u'エアコン設定', text)
        wf.add_item(title = text, icon='icon.png', arg = text, valid = True)
        wf.send_feedback()

    def power_on(self, wf):
        req = aircon.PowerOnRequest(create_config())
        dic = RemoClient.call(req)
        text = u'設定温度: {temp}度, モード: {mode}'.format(**dic)
        notify.notify(text, u'エアコンをつけたよ')


    def power_off(self, wf):
        req = aircon.PowerOffRequest(create_config())
        dic = RemoClient.call(req)
        # text = u'設定温度: {temp}度, モード: {mode}'.format(**dic)
        notify.notify(u'エアコンを消したよ', u'エアコンを消したよ')


    def change_temperature(self, wf):
        temperature = wf.args[0]
        req = aircon.ChangeTemperatureRequest(create_config(), temperature)
        dic = RemoClient.call(req)
        temperature = dic['temp']
        mode = dic['mode']
        text = u'{0}度({1})になったよ'.format(temperature, mode)
        notify.notify(text, u'エアコンの温度を変更')


COMMAND_DICT = {}
for func_name, func in inspect.getmembers(AirconCommand(), inspect.ismethod):
    COMMAND_DICT[func_name] = func


if __name__ == '__main__':
    key = sys.argv[1]
    wf = Workflow()
    sys.exit(wf.run(COMMAND_DICT[key]))
