# encoding: utf-8

import inspect
import sys

from workflow import Workflow
from workflow.notify import notify

import config
import request.appliance as appliance
from remo_client import RemoClient
import utils


class RegisterCommand:

    def register_access_token(self, wf):
        access_token = wf.args[1]
        config.update_access_token(access_token)
        message = u'アクセストークンを登録したで'
        notify(message, access_token)


    def register_aircon_id(self, wf):
        aircon_id = wf.args[1]
        config.update_aircon_id(aircon_id)
        message = u'エアコンIDを登録したで'
        notify(message, aircon_id)

    def show_remocon_list(self, wf):
        conf = config.create_config()
        req = appliance.ListRequest(conf)
        dic_array = RemoClient.call(req)
        remo_cons = []
        for dic in dic_array:
            remo_con = {}
            remo_con['id'] = dic['id']
            remo_con['nickname'] = dic['nickname']
            remo_cons.append(remo_con)

        for remo_con in remo_cons:
            appliance_id = remo_con['id']
            nickname = remo_con['nickname']
            if appliance_id == conf.aircon_id:
                nickname += '(registered)'
            wf.add_item(title = nickname, subtitle=appliance_id, icon='icon.png', arg = appliance_id, valid = True)

        wf.send_feedback()


if __name__ == '__main__':
    func_dict = utils.create_instance_func_dict(RegisterCommand)
    key = sys.argv[1]
    wf = Workflow()
    sys.exit(wf.run(func_dict[key]))
