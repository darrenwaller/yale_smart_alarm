"""Base class for yale_smart_alarm entity."""

from homeassistant.helpers.entity import DeviceInfo, Entity
from homeassistant.const import CONF_USERNAME
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MANUFACTURER, MODEL
from .coordinator import YaleDataUpdateCoordinator


class YaleEntity(CoordinatorEntity, Entity):
    """Base implementation for Yale device."""

    def __init__(self, coordinator: YaleDataUpdateCoordinator, data: dict) -> None:
        """Initialize an Yale device."""
        super().__init__(coordinator)
        self._coordinator = coordinator
        self._attr_name = data["name"]
        self._attr_unique_id = data["address"]
        self._attr_device_info = DeviceInfo(
            name=self._attr_name,
            manufacturer=MANUFACTURER,
            model=MODEL,
            identifiers={(DOMAIN, data["address"])},
            via_device=(DOMAIN, self._coordinator.entry.data[CONF_USERNAME]),
        )
