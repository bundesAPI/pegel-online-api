# pegel_online.model.timeseries.Timeseries

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**shortname** | str,  | str,  | Kurzbezeichnung | [optional] 
**longname** | str,  | str,  | Langbezeichnung | [optional] 
**unit** | str,  | str,  | Maßeinheit | [optional] 
**equidistance** | decimal.Decimal, int, float,  | decimal.Decimal,  | Abstand der Messwerte in Minuten. | [optional] value must be a 32 bit float
**currrentMeasurement** | [**CurrentMeasurement**](CurrentMeasurement.md) | [**CurrentMeasurement**](CurrentMeasurement.md) |  | [optional] 
**[gaugeZero](#gaugeZero)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[characteristicValues](#characteristicValues)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# gaugeZero

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**unit** | str,  | str,  | Einheit des Pegelnullpunkts (immer in Metern über einem Normalhöhennull ([Dokumentation](https://www.pegelonline.wsv.de/gast/hilfe#hilfe_hoehensystem)) | [optional] 
**value** | decimal.Decimal, int, float,  | decimal.Decimal,  | Höhe als Dezimalwert | [optional] value must be a 32 bit float
**validFrom** | str, date,  | str,  | Beginn der Gültigkeit. [ISO_8601](https://de.wikipedia.org/wiki/ISO_8601) Datum. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# characteristicValues

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Diese Beschreibungen variieren. | 

# items

Diese Beschreibungen variieren.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Diese Beschreibungen variieren. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

