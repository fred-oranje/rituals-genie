"""Constants for Rituals Genie."""
# Base component constants
NAME = "Rituals Genie"
MANUFACTURER = "Rituals"
MODEL = "Genie"
DOMAIN = "rituals_genie"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"

ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/fred-oranje/rituals-genie/issues"

# Icons
ICON = "mdi:format-quote-close"
ICON_WIFI = "mdi:wifi"
ICON_PERFUME = "mdi:nfc-variant"
ICON_FAN = "mdi:fan"
ICON_FILL = "mdi:format-color-fill"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [SENSOR, SWITCH]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_HUB_HASH = "hub_hash"
CONF_HUB_NAME = "hub_name"

# Defaults
DEFAULT_NAME = "Rituals Genie"


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
