# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.measurement_api import MeasurementApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from deutschland.pegel_online.api.measurement_api import MeasurementApi
from deutschland.pegel_online.api.station_api import StationApi
from deutschland.pegel_online.api.water_api import WaterApi
