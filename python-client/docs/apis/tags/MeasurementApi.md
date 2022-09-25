<a name="__pageTop"></a>
# pegel_online.apis.tags.measurement_api.MeasurementApi

All URIs are relative to *https://www.pegelonline.wsv.de/webservices/rest-api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_measurement_by_station**](#get_measurement_by_station) | **get** /stations/{station}/{timeseries}/measurements.json | Zugriff auf die Ressource Measurement
[**get_measurement_diagram_by_station**](#get_measurement_diagram_by_station) | **get** /stations/{station}/{timeseries}/measurements.png | Zugriff auf die Ressource Measurement - Rückgabe als Diagramm (PNG)

# **get_measurement_by_station**
<a name="get_measurement_by_station"></a>
> MeasurementResult get_measurement_by_station(stationtimeseries)

Zugriff auf die Ressource Measurement

Es handeln sich dabei um die gemessenen Rohwerte. Es können maximal Werte der letzten 31 Tage bezogen werden.

### Example

```python
from deutschland import pegel_online
from deutschland.pegel_online.apis.tags import measurement_api
from deutschland.pegel_online.model.timeseries_not_found import TimeseriesNotFound
from deutschland.pegel_online.model.measurement_result import MeasurementResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)

# Enter a context with an instance of the API client
with pegel_online.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = measurement_api.MeasurementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'station': "593647aa-9fea-43ec-a7d6-6476a76ae868",
        'timeseries': "W",
    }
    query_params = {
    }
    try:
        # Zugriff auf die Ressource Measurement
        api_response = api_instance.get_measurement_by_station(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling MeasurementApi->get_measurement_by_station: %s\n" % e)

    # example passing only optional values
    path_params = {
        'station': "593647aa-9fea-43ec-a7d6-6476a76ae868",
        'timeseries': "W",
    }
    query_params = {
        'start': "2022-02-06T09:00:00+01:00",
        'end': "",
    }
    try:
        # Zugriff auf die Ressource Measurement
        api_response = api_instance.get_measurement_by_station(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling MeasurementApi->get_measurement_by_station: %s\n" % e)
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
start | StartSchema | | optional
end | EndSchema | | optional


# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#get_measurement_by_station.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_measurement_by_station.ApiResponseFor404) | OK

#### get_measurement_by_station.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MeasurementResult**](../../models/MeasurementResult.md) |  | 


#### get_measurement_by_station.ApiResponseFor404
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

# **get_measurement_diagram_by_station**
<a name="get_measurement_diagram_by_station"></a>
> file_type get_measurement_diagram_by_station(stationtimeseries)

Zugriff auf die Ressource Measurement - Rückgabe als Diagramm (PNG)

Es handelt sich dabei um die gemessenen Rohwerte. Es können maximal Werte der letzten 31 Tage bezogen werden.

### Example

```python
from deutschland import pegel_online
from deutschland.pegel_online.apis.tags import measurement_api
from deutschland.pegel_online.model.timeseries_not_found import TimeseriesNotFound
from pprint import pprint
# Defining the host is optional and defaults to https://www.pegelonline.wsv.de/webservices/rest-api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pegel_online.Configuration(
    host = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"
)

# Enter a context with an instance of the API client
with pegel_online.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = measurement_api.MeasurementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'station': "593647aa-9fea-43ec-a7d6-6476a76ae868",
        'timeseries': "W",
    }
    query_params = {
    }
    try:
        # Zugriff auf die Ressource Measurement - Rückgabe als Diagramm (PNG)
        api_response = api_instance.get_measurement_diagram_by_station(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling MeasurementApi->get_measurement_diagram_by_station: %s\n" % e)

    # example passing only optional values
    path_params = {
        'station': "593647aa-9fea-43ec-a7d6-6476a76ae868",
        'timeseries': "W",
    }
    query_params = {
        'start': "2022-02-06T09:00:00+01:00",
        'end': "",
        'width': 900,
        'height': 400,
        'enableSecondaryYAxis': True,
    }
    try:
        # Zugriff auf die Ressource Measurement - Rückgabe als Diagramm (PNG)
        api_response = api_instance.get_measurement_diagram_by_station(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pegel_online.ApiException as e:
        print("Exception when calling MeasurementApi->get_measurement_diagram_by_station: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('image/png', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
start | StartSchema | | optional
end | EndSchema | | optional
width | WidthSchema | | optional
height | HeightSchema | | optional
enableSecondaryYAxis | EnableSecondaryYAxisSchema | | optional


# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# WidthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# HeightSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# EnableSecondaryYAxisSchema

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
200 | [ApiResponseFor200](#get_measurement_diagram_by_station.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_measurement_diagram_by_station.ApiResponseFor404) | OK

#### get_measurement_diagram_by_station.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyImagePng, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyImagePng

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### get_measurement_diagram_by_station.ApiResponseFor404
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

