"""
    Pegel-Online API

    API für das bundesweite Messstellennetz der Wasserstraßen- und Schifffahrtsverwaltung des Bundes.  Die API stellt drei verschiedene Ressourcen zur Verfügung: __Station__, __Measurement__, __Water__. ### Authentifizierung / Autorisierung / API Limitierung Es ist keine Authentifizierung oder Autorisierung notwendig. Aktuell besteht keine API Limitierung. ### Allgemeine Query-Parameter Zusätzlich zu den angegebenen Parametern sind ebenfalls allgemeine Parameter für alle Schnittstellen verfügbar ([Dokumentation](https://www.pegelonline.wsv.de/webservice/dokuRestapi;jsessionid=A294589CCEF6630142D2589F49BFA2EC#urlParameter)). - `charset`: Gibt die Kodierung der Response an. Standard ist hier _UTF-8_. Möglich ist z.B. auch _ISO-8859-1_. - `prettyprint`: Kann die zur besseren Lesbarkeit standardmäßig aktivierte Teilung der Response in mehreren Zeilen deaktivieren: _prettyprint=false_. Diese Einstellung wird für den produktiven Einsatz empfohlen. - `limit/offset`: Einschränkung der Anzahl der Ergebnisse. Hiermit kann 'Pagination' realisiert werden. `limit` gibt dabei die Anzahl der zurückgegebenen Elemente an. `offset` ermöglicht einen Offset vom Startwert. Beispiel: _limit=10&offset=20_ bedeutet, dass 10 Elemente beginnend mit dem 21. Element zurückgegeben werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.pegel_online.api_client import ApiClient
from deutschland.pegel_online.api_client import Endpoint as _Endpoint
from deutschland.pegel_online.model.timeseries import Timeseries
from deutschland.pegel_online.model.timeseries_not_found import TimeseriesNotFound
from deutschland.pegel_online.model.water_result import WaterResult
from deutschland.pegel_online.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class WaterApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_current_measurment_by_station_endpoint = _Endpoint(
            settings={
                "response_type": (Timeseries,),
                "auth": [],
                "endpoint_path": "/stations/{station}/{timeseries}.json",
                "operation_id": "get_current_measurment_by_station",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "station",
                    "timeseries",
                    "include_current_measurement",
                    "include_characteristic_values",
                ],
                "required": [
                    "station",
                    "timeseries",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "station": (str,),
                    "timeseries": (str,),
                    "include_current_measurement": (bool,),
                    "include_characteristic_values": (bool,),
                },
                "attribute_map": {
                    "station": "station",
                    "timeseries": "timeseries",
                    "include_current_measurement": "includeCurrentMeasurement",
                    "include_characteristic_values": "includeCharacteristicValues",
                },
                "location_map": {
                    "station": "path",
                    "timeseries": "path",
                    "include_current_measurement": "query",
                    "include_characteristic_values": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_waters_endpoint = _Endpoint(
            settings={
                "response_type": (WaterResult,),
                "auth": [],
                "endpoint_path": "/waters.json",
                "operation_id": "get_waters",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "ids",
                    "stations",
                    "include_stations",
                    "include_timeseries",
                    "include_current_measurement",
                    "include_characteristic_values",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "ids": ([str],),
                    "stations": (str,),
                    "include_stations": (bool,),
                    "include_timeseries": (bool,),
                    "include_current_measurement": (bool,),
                    "include_characteristic_values": (bool,),
                },
                "attribute_map": {
                    "ids": "ids",
                    "stations": "stations",
                    "include_stations": "includeStations",
                    "include_timeseries": "includeTimeseries",
                    "include_current_measurement": "includeCurrentMeasurement",
                    "include_characteristic_values": "includeCharacteristicValues",
                },
                "location_map": {
                    "ids": "query",
                    "stations": "query",
                    "include_stations": "query",
                    "include_timeseries": "query",
                    "include_current_measurement": "query",
                    "include_characteristic_values": "query",
                },
                "collection_format_map": {
                    "ids": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def get_current_measurment_by_station(self, station, timeseries, **kwargs):
        """Zugriff auf eine Timeseries  # noqa: E501

        Liefert den aktuellen Wert der Station (Pegel). Kann auch als Unterressource von Timeseries angefordert werden.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_current_measurment_by_station(station, timeseries, async_req=True)
        >>> result = thread.get()

        Args:
            station (str): UUID / Name / Pegelnummer der Station.
            timeseries (str): timeseries shortname

        Keyword Args:
            include_current_measurement (bool): Aktuell gemessener Wert. [optional]
            include_characteristic_values (bool): kennzeichnende Wasserstände. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Timeseries
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["station"] = station
        kwargs["timeseries"] = timeseries
        return self.get_current_measurment_by_station_endpoint.call_with_http_info(
            **kwargs
        )

    def get_waters(self, **kwargs):
        """Zugriff auf die Ressource Water  # noqa: E501

        Alle Gewässer  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_waters(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            ids ([str]): Beschränkung auf ausgewählte Gewässer IDs. [optional]
            stations (str): Beschränkung auf ausgewählte Stationen (Pegel). [optional]
            include_stations (bool): Stationen mit zurückgeben. [optional]
            include_timeseries (bool): Informationen zu den Zeitreihen. [optional]
            include_current_measurement (bool): Aktuell gemessener Wert. [optional]
            include_characteristic_values (bool): kennzeichnende Wasserstände. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            WaterResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        return self.get_waters_endpoint.call_with_http_info(**kwargs)
