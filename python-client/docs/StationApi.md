# pegel_online.StationApi

All URIs are relative to *https://www.pegelonline.wsv.de/webservices/rest-api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stations**](StationApi.md#get_stations) | **GET** /stations.json | Übersicht über alle Stationen (Pegel)
[**get_stations_by_id**](StationApi.md#get_stations_by_id) | **GET** /stations/{station}.json | Zugriff auf eine bestimmte Station (Pegel)


# **get_stations**
> StationOverviewResult get_stations()

Übersicht über alle Stationen (Pegel)

Stationen (Pegel) sortiert nach Gewässername und Messstellenname.

### Example


```python
import time
from deutschland import pegel_online
from deutschland.pegel_online.api import station_api
from deutschland.pegel_online.model.station_overview_result import StationOverviewResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)


# Enter a context with an instance of the API client
with pegel_online.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = station_api.StationApi(api_client)
    include_timeseries = True # bool | Informationen zu den Zeitreihen (optional)
    include_current_measurement = True # bool | Aktuell gemessener Wert (optional)
    include_characteristic_values = True # bool | kennzeichnende Wasserstände (optional)
    waters = [] # [str] | Gewässer, filtert Stationen für bestimmte Gewässer (optional)
    ids = [
        "ids_example",
    ] # [str] | Filter nach Stationen, möglich sind der Pegelname, Pegelnummer oder die UUID (optional)
    timeseries = "" # str | Filter nach ausgewählten Zeitreihen (optional)
    fuzzy_id = "" # str |  (optional)
    latitude = 3.14 # float | Breitengrad einer geografischen Position (WGS84 in Dezimalnotation) (optional)
    longitude = 3.14 # float | Längengrad einer geografischen Position (WGS84 in Dezimalnotation) (optional)
    km = 3.14 # float | Flusskilometer, die Angabe eines Gewässers (waters) ist notwendig (optional)
    radius = 3.14 # float | Suchradius für Stationen um die geografische Position oder den angegebenen Flusskilometer. Longitude und / oder Latitude oder km sind notwendig. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Übersicht über alle Stationen (Pegel)
        api_response = api_instance.get_stations(include_timeseries=include_timeseries, include_current_measurement=include_current_measurement, include_characteristic_values=include_characteristic_values, waters=waters, ids=ids, timeseries=timeseries, fuzzy_id=fuzzy_id, latitude=latitude, longitude=longitude, km=km, radius=radius)
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling StationApi->get_stations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_timeseries** | **bool**| Informationen zu den Zeitreihen | [optional]
 **include_current_measurement** | **bool**| Aktuell gemessener Wert | [optional]
 **include_characteristic_values** | **bool**| kennzeichnende Wasserstände | [optional]
 **waters** | **[str]**| Gewässer, filtert Stationen für bestimmte Gewässer | [optional]
 **ids** | **[str]**| Filter nach Stationen, möglich sind der Pegelname, Pegelnummer oder die UUID | [optional]
 **timeseries** | **str**| Filter nach ausgewählten Zeitreihen | [optional]
 **fuzzy_id** | **str**|  | [optional]
 **latitude** | **float**| Breitengrad einer geografischen Position (WGS84 in Dezimalnotation) | [optional]
 **longitude** | **float**| Längengrad einer geografischen Position (WGS84 in Dezimalnotation) | [optional]
 **km** | **float**| Flusskilometer, die Angabe eines Gewässers (waters) ist notwendig | [optional]
 **radius** | **float**| Suchradius für Stationen um die geografische Position oder den angegebenen Flusskilometer. Longitude und / oder Latitude oder km sind notwendig. | [optional]

### Return type

[**StationOverviewResult**](StationOverviewResult.md)

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

# **get_stations_by_id**
> Station get_stations_by_id(station)

Zugriff auf eine bestimmte Station (Pegel)

Zugriff auf eine Station (Pegel) ist mittels des Namens, der Pegelnummer sowie der UUID möglich. Es wird die Verwendung der UUID empfohlen.

### Example


```python
import time
from deutschland import pegel_online
from deutschland.pegel_online.api import station_api
from deutschland.pegel_online.model.station import Station
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)


# Enter a context with an instance of the API client
with pegel_online.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = station_api.StationApi(api_client)
    station = "593647aa-9fea-43ec-a7d6-6476a76ae868" # str | UUID / Name / Pegelnummer der Station.
    include_timeseries = True # bool | Informationen zu den Zeitreihen (optional)
    include_current_measurement = True # bool | Aktuell gemessener Wert (optional)
    include_characteristic_values = True # bool | kennzeichnende Wasserstände (optional)

    # example passing only required values which don't have defaults set
    try:
        # Zugriff auf eine bestimmte Station (Pegel)
        api_response = api_instance.get_stations_by_id(station)
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling StationApi->get_stations_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Zugriff auf eine bestimmte Station (Pegel)
        api_response = api_instance.get_stations_by_id(station, include_timeseries=include_timeseries, include_current_measurement=include_current_measurement, include_characteristic_values=include_characteristic_values)
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling StationApi->get_stations_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station** | **str**| UUID / Name / Pegelnummer der Station. |
 **include_timeseries** | **bool**| Informationen zu den Zeitreihen | [optional]
 **include_current_measurement** | **bool**| Aktuell gemessener Wert | [optional]
 **include_characteristic_values** | **bool**| kennzeichnende Wasserstände | [optional]

### Return type

[**Station**](Station.md)

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

