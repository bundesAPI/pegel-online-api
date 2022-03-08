# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.pegel_online.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.pegel_online.model.comment import Comment
from deutschland.pegel_online.model.current_measurement import CurrentMeasurement
from deutschland.pegel_online.model.measurement_result import MeasurementResult
from deutschland.pegel_online.model.station_overview_result import StationOverviewResult
from deutschland.pegel_online.model.timeseries import Timeseries
from deutschland.pegel_online.model.timeseries_gauge_zero import TimeseriesGaugeZero
from deutschland.pegel_online.model.water_result import WaterResult
