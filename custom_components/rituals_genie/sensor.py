"""Sensor platform for Rituals Genie."""
from .const import DEFAULT_NAME
from .const import DOMAIN
from .const import ICON_FILL
from .const import ICON_PERFUME
from .const import ICON_WIFI
from .entity import RitualsGenieEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        [
            RitualsGeniePerfumeSensor(coordinator, entry, "perfume"),
            RitualsGenieFillSensor(coordinator, entry, "fill"),
            RitualsGenieWifiSensor(coordinator, entry, "wifi"),
        ]
    )


class RitualsGeniePerfumeSensor(RitualsGenieEntity):
    """rituals_genie Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME} {self.hub_name} Perfume"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("hub").get("sensors").get("rfidc").get("title")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON_PERFUME

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "rituals_genie__custom_device_class"


class RitualsGenieFillSensor(RitualsGenieEntity):
    """rituals_genie Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME} {self.hub_name} Fill"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("hub").get("sensors").get("fillc").get("title")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON_FILL

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "rituals_genie__custom_device_class"


class RitualsGenieWifiSensor(RitualsGenieEntity):
    """rituals_genie Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME} {self.hub_name} Wifi"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("hub").get("sensors").get("wific").get("title")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON_WIFI

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "rituals_genie__custom_device_class"
