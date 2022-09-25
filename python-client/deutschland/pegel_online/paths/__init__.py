# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from deutschland.pegel_online.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    STATIONS_JSON = "/stations.json"
    STATIONS_STATION_JSON = "/stations/{station}.json"
    STATIONS_STATION_TIMESERIES_MEASUREMENTS_JSON = (
        "/stations/{station}/{timeseries}/measurements.json"
    )
    STATIONS_STATION_TIMESERIES_MEASUREMENTS_PNG = (
        "/stations/{station}/{timeseries}/measurements.png"
    )
    WATERS_JSON = "/waters.json"
    STATIONS_STATION_TIMESERIES_JSON = "/stations/{station}/{timeseries}.json"
