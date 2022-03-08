# pegel_online.MeasurementApi

All URIs are relative to *https://www.pegelonline.wsv.de/webservices/rest-api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stations_station_timeseries_measurements_json_get**](MeasurementApi.md#stations_station_timeseries_measurements_json_get) | **GET** /stations/{station}/{timeseries}/measurements.json | Zugriff auf die Ressource Measurement
[**stations_station_timeseries_measurements_png_get**](MeasurementApi.md#stations_station_timeseries_measurements_png_get) | **GET** /stations/{station}/{timeseries}/measurements.png | Zugriff auf die Ressource Measurement - Rückgabe als Diagramm (PNG)


# **stations_station_timeseries_measurements_json_get**
> MeasurementResult stations_station_timeseries_measurements_json_get(station, timeseries)

Zugriff auf die Ressource Measurement

Es handeln sich dabei um die gemessenen Rohwerte. Es können maximal Werte der letzten 31 Tage bezogen werden.

### Example


```python
import time
from deutschland import pegel_online
from deutschland.pegel_online.api import measurement_api
from deutschland.pegel_online.model.measurement_result import MeasurementResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)


# Enter a context with an instance of the API client
with pegel_online.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = measurement_api.MeasurementApi(api_client)
    station = "593647aa-9fea-43ec-a7d6-6476a76ae868" # str | UUID / Name / Pegelnummer der Station.
    timeseries = "" # str | timeseries shortname
    start = "2022-02-06T09:00:00+01:00" # str | Zeitpunkt codiert im [ISO_8601](https://de.wikipedia.org/wiki/ISO_8601) Format. Angabe eines Datums oder einer Period (_P_, z.B. \"P8D\" für die Messwerte der letzten 8 Tage) sind möglich. (optional)
    end = "" # str | Endzeitpunkt codiert im [ISO_8601](https://de.wikipedia.org/wiki/ISO_8601) Format. Kann auch leer gelassen werden, dann wird automatisch der aktuelle Zeitstempel verwendet. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Zugriff auf die Ressource Measurement
        api_response = api_instance.stations_station_timeseries_measurements_json_get(station, timeseries)
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling MeasurementApi->stations_station_timeseries_measurements_json_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Zugriff auf die Ressource Measurement
        api_response = api_instance.stations_station_timeseries_measurements_json_get(station, timeseries, start=start, end=end)
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling MeasurementApi->stations_station_timeseries_measurements_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station** | **str**| UUID / Name / Pegelnummer der Station. |
 **timeseries** | **str**| timeseries shortname |
 **start** | **str**| Zeitpunkt codiert im [ISO_8601](https://de.wikipedia.org/wiki/ISO_8601) Format. Angabe eines Datums oder einer Period (_P_, z.B. \&quot;P8D\&quot; für die Messwerte der letzten 8 Tage) sind möglich. | [optional]
 **end** | **str**| Endzeitpunkt codiert im [ISO_8601](https://de.wikipedia.org/wiki/ISO_8601) Format. Kann auch leer gelassen werden, dann wird automatisch der aktuelle Zeitstempel verwendet. | [optional]

### Return type

[**MeasurementResult**](MeasurementResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stations_station_timeseries_measurements_png_get**
> file_type stations_station_timeseries_measurements_png_get(station, timeseries)

Zugriff auf die Ressource Measurement - Rückgabe als Diagramm (PNG)

Es handelt sich dabei um die gemessenen Rohwerte. Es können maximal Werte der letzten 31 Tage bezogen werden.

### Example


```python
import time
from deutschland import pegel_online
from deutschland.pegel_online.api import measurement_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)


# Enter a context with an instance of the API client
with pegel_online.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = measurement_api.MeasurementApi(api_client)
    station = "593647aa-9fea-43ec-a7d6-6476a76ae868" # str | UUID / Name / Pegelnummer der Station.
    timeseries = "" # str | timeseries shortname
    start = "2022-02-06T09:00:00+01:00" # str | Zeitpunkt codiert im [ISO_8601](https://de.wikipedia.org/wiki/ISO_8601) Format. Angabe eines Datums oder einer Period (_P_, z.B. \"P8D\" für die Messwerte der letzten 8 Tage) sind möglich. (optional)
    end = "" # str | Endzeitpunkt codiert im [ISO_8601](https://de.wikipedia.org/wiki/ISO_8601) Format. Kann auch leer gelassen werden, dann wird automatisch der aktuelle Zeitstempel verwendet. (optional)
    width = 900 # float | Breite der grafischen Darstellung (optional)
    height = 400 # float | Höhe der grafischen Darstellung (optional)
    enable_secondary_y_axis = True # bool | Aktivierung einer zweiten Y-Achse auf der rechten Seite (optional)

    # example passing only required values which don't have defaults set
    try:
        # Zugriff auf die Ressource Measurement - Rückgabe als Diagramm (PNG)
        api_response = api_instance.stations_station_timeseries_measurements_png_get(station, timeseries)
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling MeasurementApi->stations_station_timeseries_measurements_png_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Zugriff auf die Ressource Measurement - Rückgabe als Diagramm (PNG)
        api_response = api_instance.stations_station_timeseries_measurements_png_get(station, timeseries, start=start, end=end, width=width, height=height, enable_secondary_y_axis=enable_secondary_y_axis)
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling MeasurementApi->stations_station_timeseries_measurements_png_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station** | **str**| UUID / Name / Pegelnummer der Station. |
 **timeseries** | **str**| timeseries shortname |
 **start** | **str**| Zeitpunkt codiert im [ISO_8601](https://de.wikipedia.org/wiki/ISO_8601) Format. Angabe eines Datums oder einer Period (_P_, z.B. \&quot;P8D\&quot; für die Messwerte der letzten 8 Tage) sind möglich. | [optional]
 **end** | **str**| Endzeitpunkt codiert im [ISO_8601](https://de.wikipedia.org/wiki/ISO_8601) Format. Kann auch leer gelassen werden, dann wird automatisch der aktuelle Zeitstempel verwendet. | [optional]
 **width** | **float**| Breite der grafischen Darstellung | [optional]
 **height** | **float**| Höhe der grafischen Darstellung | [optional]
 **enable_secondary_y_axis** | **bool**| Aktivierung einer zweiten Y-Achse auf der rechten Seite | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

