# pegel_online.model.station.Station

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uuid** | str,  | str,  | Eindeutige unveränderliche ID | [optional] 
**number** | str,  | str,  | Pegelnummer | [optional] 
**shortname** | str,  | str,  | Pegelname (max. 40 Zeichen) | [optional] 
**longname** | str,  | str,  | Pegelname (max. 255 Zeichen) | [optional] 
**km** | decimal.Decimal, int, float,  | decimal.Decimal,  | Flusskilometer | [optional] value must be a 32 bit float
**agency** | str,  | str,  | Wasserstraßen- und Schifffahrtsamt | [optional] 
**longitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | Längengrad in WGS84 Dezimalnotation | [optional] value must be a 32 bit float
**latitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | Breitengrad in WGS84 Dezimalnotation | [optional] value must be a 32 bit float
**[water](#water)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Angaben zum Gewässer | [optional] 
**[timeseries](#timeseries)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# water

Angaben zum Gewässer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Angaben zum Gewässer | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**shortname** | str,  | str,  |  | [optional] 
**longname** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# timeseries

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Timeseries**](Timeseries.md) | [**Timeseries**](Timeseries.md) | [**Timeseries**](Timeseries.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

