<a name="__pageTop"></a>
# pegel_online.apis.tags.station_api.StationApi

All URIs are relative to *https://www.pegelonline.wsv.de/webservices/rest-api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stations**](#get_stations) | **get** /stations.json | Übersicht über alle Stationen (Pegel)
[**get_stations_by_id**](#get_stations_by_id) | **get** /stations/{station}.json | Zugriff auf eine bestimmte Station (Pegel)

# **get_stations**
<a name="get_stations"></a>
> StationOverviewResult get_stations()

Übersicht über alle Stationen (Pegel)

Stationen (Pegel) sortiert nach Gewässername und Messstellenname.

### Example

```python
from deutschland import pegel_online
from deutschland.pegel_online.apis.tags import station_api
from deutschland.pegel_online.model.station_overview_result import StationOverviewResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)

# Enter a context with an instance of the API client
with pegel_online.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = station_api.StationApi(api_client)

    # example passing only optional values
    query_params = {
        'includeTimeseries': True,
        'includeCurrentMeasurement': True,
        'includeCharacteristicValues': True,
        'waters': [],
        'ids': [
        "ids_example"
    ],
        'timeseries': "",
        'fuzzyId': "",
        'latitude': 3.14,
        'longitude': 3.14,
        'km': 3.14,
        'radius': 3.14,
    }
    try:
        # Übersicht über alle Stationen (Pegel)
        api_response = api_instance.get_stations(
            query_params=query_params,
        )
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling StationApi->get_stations: %s\n" % e)
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
includeTimeseries | IncludeTimeseriesSchema | | optional
includeCurrentMeasurement | IncludeCurrentMeasurementSchema | | optional
includeCharacteristicValues | IncludeCharacteristicValuesSchema | | optional
waters | WatersSchema | | optional
ids | IdsSchema | | optional
timeseries | TimeseriesSchema | | optional
fuzzyId | FuzzyIdSchema | | optional
latitude | LatitudeSchema | | optional
longitude | LongitudeSchema | | optional
km | KmSchema | | optional
radius | RadiusSchema | | optional


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

# WatersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TimeseriesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FuzzyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LatitudeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 32 bit float

# LongitudeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 32 bit float

# KmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 32 bit float

# RadiusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 32 bit float

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_stations.ApiResponseFor200) | OK

#### get_stations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StationOverviewResult**](../../models/StationOverviewResult.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_stations_by_id**
<a name="get_stations_by_id"></a>
> Station get_stations_by_id(station)

Zugriff auf eine bestimmte Station (Pegel)

Zugriff auf eine Station (Pegel) ist mittels des Namens, der Pegelnummer sowie der UUID möglich. Es wird die Verwendung der UUID empfohlen.

### Example

```python
from deutschland import pegel_online
from deutschland.pegel_online.apis.tags import station_api
from deutschland.pegel_online.model.station import Station
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)

# Enter a context with an instance of the API client
with pegel_online.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = station_api.StationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'station': "593647aa-9fea-43ec-a7d6-6476a76ae868",
    }
    query_params = {
    }
    try:
        # Zugriff auf eine bestimmte Station (Pegel)
        api_response = api_instance.get_stations_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling StationApi->get_stations_by_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'station': "593647aa-9fea-43ec-a7d6-6476a76ae868",
    }
    query_params = {
        'includeTimeseries': True,
        'includeCurrentMeasurement': True,
        'includeCharacteristicValues': True,
    }
    try:
        # Zugriff auf eine bestimmte Station (Pegel)
        api_response = api_instance.get_stations_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling StationApi->get_stations_by_id: %s\n" % e)
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
includeTimeseries | IncludeTimeseriesSchema | | optional
includeCurrentMeasurement | IncludeCurrentMeasurementSchema | | optional
includeCharacteristicValues | IncludeCharacteristicValuesSchema | | optional


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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
station | StationSchema | | 

# StationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_stations_by_id.ApiResponseFor200) | OK

#### get_stations_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Station**](../../models/Station.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

