# encoding: utf-8

from remo_request import RemoRequest


class _BaseAirconRequest(RemoRequest):
    def __init__(self, config):
        super(_BaseAirconRequest, self).__init__(config)
        self._aircon_id = config.aircon_id
        if self._aircon_id is None or len(self._aircon_id) == 0:
            raise ValueError('must need to set aircon_id')

    def path(self):
        return 'appliances/{0}/aircon_settings'.format(self._aircon_id)

    def method(self):
        return 'POST'


class ChangeTemperatureRequest(_BaseAirconRequest):
    def __init__(self, config, temperature):
        super(ChangeTemperatureRequest, self).__init__(config)
        self._temperature = temperature

    def param(self):
        return {'temperature': self._temperature}


class PowerOnRequest(_BaseAirconRequest):
    def __init__(self, config):
        super(PowerOnRequest, self).__init__(config)

    def param(self):
        return {'button': ''}


class PowerOffRequest(_BaseAirconRequest):
    def __init__(self, config):
        super(PowerOffRequest, self).__init__(config)

    def param(self):
        return {'button': 'power-off'}


class ChangeModeToCoolRequest(_BaseAirconRequest):
    def __init__(self, config):
        super(ChangeModeToCoolRequest, self).__init__(config)

    def param(self):
        return {'mode': 'cool'}


class ChangeModeToWarmRequest(_BaseAirconRequest):
    def __init__(self, config):
        super(ChangeModeToWarmRequest, self).__init__(config)

    def param(self):
        return {'mode': 'warm'}

