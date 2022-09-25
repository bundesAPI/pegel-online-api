<a name="__pageTop"></a>
# pegel_online.apis.tags.water_api.WaterApi

All URIs are relative to *https://www.pegelonline.wsv.de/webservices/rest-api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_measurment_by_station**](#get_current_measurment_by_station) | **get** /stations/{station}/{timeseries}.json | Zugriff auf eine Timeseries
[**get_waters**](#get_waters) | **get** /waters.json | Zugriff auf die Ressource Water

# **get_current_measurment_by_station**
<a name="get_current_measurment_by_station"></a>
> Timeseries get_current_measurment_by_station(stationtimeseries)

Zugriff auf eine Timeseries

Liefert den aktuellen Wert der Station (Pegel). Kann auch als Unterressource von Timeseries angefordert werden.

### Example

```python
from deutschland import pegel_online
from deutschland.pegel_online.apis.tags import water_api
from deutschland.pegel_online.model.timeseries_not_found import TimeseriesNotFound
from deutschland.pegel_online.model.timeseries import Timeseries
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)

# Enter a context with an instance of the API client
with pegel_online.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'station': "593647aa-9fea-43ec-a7d6-6476a76ae868",
        'timeseries': "W",
    }
    query_params = {
    }
    try:
        # Zugriff auf eine Timeseries
        api_response = api_instance.get_current_measurment_by_station(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling WaterApi->get_current_measurment_by_station: %s\n" % e)

    # example passing only optional values
    path_params = {
        'station': "593647aa-9fea-43ec-a7d6-6476a76ae868",
        'timeseries': "W",
    }
    query_params = {
        'includeCurrentMeasurement': True,
        'includeCharacteristicValues': True,
    }
    try:
        # Zugriff auf eine Timeseries
        api_response = api_instance.get_current_measurment_by_station(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling WaterApi->get_current_measurment_by_station: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
includeCurrentMeasurement | IncludeCurrentMeasurementSchema | | optional
includeCharacteristicValues | IncludeCharacteristicValuesSchema | | optional


# IncludeCurrentMeasurementSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IncludeCharacteristicValuesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
station | StationSchema | | 
timeseries | TimeseriesSchema | | 

# StationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeseriesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_current_measurment_by_station.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_current_measurment_by_station.ApiResponseFor404) | OK

#### get_current_measurment_by_station.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Timeseries**](../../models/Timeseries.md) |  | 


#### get_current_measurment_by_station.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TimeseriesNotFound**](../../models/TimeseriesNotFound.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_waters**
<a name="get_waters"></a>
> WaterResult get_waters()

Zugriff auf die Ressource Water

Alle Gewässer

### Example

```python
from deutschland import pegel_online
from deutschland.pegel_online.apis.tags import water_api
from deutschland.pegel_online.model.water_result import WaterResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)

# Enter a context with an instance of the API client
with pegel_online.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)

    # example passing only optional values
    query_params = {
        'ids': [
        "ids_example"
    ],
        'stations': "stations_example",
        'includeStations': True,
        'includeTimeseries': True,
        'includeCurrentMeasurement': True,
        'includeCharacteristicValues': True,
    }
    try:
        # Zugriff auf die Ressource Water
        api_response = api_instance.get_waters(
            query_params=query_params,
        )
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling WaterApi->get_waters: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ids | IdsSchema | | optional
stations | StationsSchema | | optional
includeStations | IncludeStationsSchema | | optional
includeTimeseries | IncludeTimeseriesSchema | | optional
includeCurrentMeasurement | IncludeCurrentMeasurementSchema | | optional
includeCharacteristicValues | IncludeCharacteristicValuesSchema | | optional


# IdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StationsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IncludeStationsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IncludeTimeseriesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IncludeCurrentMeasurementSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IncludeCharacteristicValuesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_waters.ApiResponseFor200) | OK

#### get_waters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WaterResult**](../../models/WaterResult.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

