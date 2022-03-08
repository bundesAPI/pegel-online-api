# pegel_online.WaterApi

All URIs are relative to *https://www.pegelonline.wsv.de/webservices/rest-api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stations_station_timeseries_json_get**](WaterApi.md#stations_station_timeseries_json_get) | **GET** /stations/{station}/{timeseries}.json | Zugriff auf CurrentMeasurment
[**waters_json_get**](WaterApi.md#waters_json_get) | **GET** /waters.json | Zugriff auf die Ressource Water


# **stations_station_timeseries_json_get**
> WaterResult stations_station_timeseries_json_get(station, timeseries)

Zugriff auf CurrentMeasurment

Liefert den aktuellen Wert der Station (Pegel). Kann auch als Unterressource von Timeseries angefordert werden.

### Example


```python
import time
from deutschland import pegel_online
from deutschland.pegel_online.api import water_api
from deutschland.pegel_online.model.water_result import WaterResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)


# Enter a context with an instance of the API client
with pegel_online.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    station = "593647aa-9fea-43ec-a7d6-6476a76ae868" # str | UUID / Name / Pegelnummer der Station.
    timeseries = "" # str | timeseries shortname

    # example passing only required values which don't have defaults set
    try:
        # Zugriff auf CurrentMeasurment
        api_response = api_instance.stations_station_timeseries_json_get(station, timeseries)
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling WaterApi->stations_station_timeseries_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station** | **str**| UUID / Name / Pegelnummer der Station. |
 **timeseries** | **str**| timeseries shortname |

### Return type

[**WaterResult**](WaterResult.md)

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

# **waters_json_get**
> WaterResult waters_json_get()

Zugriff auf die Ressource Water

Alle Gewässer

### Example


```python
import time
from deutschland import pegel_online
from deutschland.pegel_online.api import water_api
from deutschland.pegel_online.model.water_result import WaterResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)


# Enter a context with an instance of the API client
with pegel_online.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    ids = [
        "ids_example",
    ] # [str] | Beschränkung auf ausgewählte Gewässer IDs (optional)
    stations = "stations_example" # str | Beschränkung auf ausgewählte Stationen (Pegel) (optional)
    include_stations = True # bool | Stationen mit zurückgeben (optional)
    include_timeseries = True # bool | Informationen zu den Zeitreihen (optional)
    include_current_measurement = True # bool | Aktuell gemessener Wert (optional)
    include_characteristic_values = True # bool | kennzeichnende Wasserstände (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Zugriff auf die Ressource Water
        api_response = api_instance.waters_json_get(ids=ids, stations=stations, include_stations=include_stations, include_timeseries=include_timeseries, include_current_measurement=include_current_measurement, include_characteristic_values=include_characteristic_values)
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling WaterApi->waters_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| Beschränkung auf ausgewählte Gewässer IDs | [optional]
 **stations** | **str**| Beschränkung auf ausgewählte Stationen (Pegel) | [optional]
 **include_stations** | **bool**| Stationen mit zurückgeben | [optional]
 **include_timeseries** | **bool**| Informationen zu den Zeitreihen | [optional]
 **include_current_measurement** | **bool**| Aktuell gemessener Wert | [optional]
 **include_characteristic_values** | **bool**| kennzeichnende Wasserstände | [optional]

### Return type

[**WaterResult**](WaterResult.md)

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

