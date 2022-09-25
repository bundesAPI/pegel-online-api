import typing_extensions
from deutschland.pegel_online.apis.paths.stations_json import StationsJson
from deutschland.pegel_online.apis.paths.stations_station_json import (
    StationsStationJson,
)
from deutschland.pegel_online.apis.paths.stations_station_timeseries_json import (
    StationsStationTimeseriesJson,
)
from deutschland.pegel_online.apis.paths.stations_station_timeseries_measurements_json import (
    StationsStationTimeseriesMeasurementsJson,
)
from deutschland.pegel_online.apis.paths.stations_station_timeseries_measurements_png import (
    StationsStationTimeseriesMeasurementsPng,
)
from deutschland.pegel_online.apis.paths.waters_json import WatersJson
from deutschland.pegel_online.paths import PathValues

PathToApi = typing_extensions.TypedDict(
    "PathToApi",
    {
        PathValues.STATIONS_JSON: StationsJson,
        PathValues.STATIONS_STATION_JSON: StationsStationJson,
        PathValues.STATIONS_STATION_TIMESERIES_MEASUREMENTS_JSON: StationsStationTimeseriesMeasurementsJson,
        PathValues.STATIONS_STATION_TIMESERIES_MEASUREMENTS_PNG: StationsStationTimeseriesMeasurementsPng,
        PathValues.WATERS_JSON: WatersJson,
        PathValues.STATIONS_STATION_TIMESERIES_JSON: StationsStationTimeseriesJson,
    },
)

path_to_api = PathToApi(
    {
        PathValues.STATIONS_JSON: StationsJson,
        PathValues.STATIONS_STATION_JSON: StationsStationJson,
        PathValues.STATIONS_STATION_TIMESERIES_MEASUREMENTS_JSON: StationsStationTimeseriesMeasurementsJson,
        PathValues.STATIONS_STATION_TIMESERIES_MEASUREMENTS_PNG: StationsStationTimeseriesMeasurementsPng,
        PathValues.WATERS_JSON: WatersJson,
        PathValues.STATIONS_STATION_TIMESERIES_JSON: StationsStationTimeseriesJson,
    }
)
