# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from deutschland.pegel_online.paths.stations_json import Api

from deutschland.pegel_online.paths import PathValues

path = PathValues.STATIONS_JSON
