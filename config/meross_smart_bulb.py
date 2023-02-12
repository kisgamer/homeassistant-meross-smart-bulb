import logging
import meross_iot

from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    ATTR_COLOR_TEMP,
    ATTR_HS_COLOR,
    Light,
)
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_USERNAME

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    host = config.get(CONF_HOST)
    username = config.get(CONF_USERNAME)
    password = config.get(CONF_PASSWORD)

    client = meross_iot.MerossHttpClient(http_username=username, http_password=password)
    client.start()

    devices = client.list_supported_devices()
    lights = [device for device in devices if isinstance(device, meross_iot.light.MerossLight)]

    add_devices(MerossSmartBulb(light) for light in lights)

class MerossSmartBulb(Light):
    def __init__(self, device):
        self._device = device
        self._brightness = None
        self._color_temp = None
        self._hs_color = None
        self._state = None

    @property
    def name(self):
        return self._device.name

    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        self._device.turn_on()
        self._state = True

        if ATTR_BRIGHTNESS in kw
