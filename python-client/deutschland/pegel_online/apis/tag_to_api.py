import typing_extensions
from deutschland.pegel_online.apis.tags import TagValues
from deutschland.pegel_online.apis.tags.measurement_api import MeasurementApi
from deutschland.pegel_online.apis.tags.station_api import StationApi
from deutschland.pegel_online.apis.tags.water_api import WaterApi

TagToApi = typing_extensions.TypedDict(
    "TagToApi",
    {
        TagValues.STATION: StationApi,
        TagValues.MEASUREMENT: MeasurementApi,
        TagValues.WATER: WaterApi,
    },
)

tag_to_api = TagToApi(
    {
        TagValues.STATION: StationApi,
        TagValues.MEASUREMENT: MeasurementApi,
        TagValues.WATER: WaterApi,
    }
)
