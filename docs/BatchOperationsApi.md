# openapi_client.BatchOperationsApi

All URIs are relative to *http://orion.lab.fiware.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notify**](BatchOperationsApi.md#notify) | **POST** /v2/op/notify | Notify
[**query**](BatchOperationsApi.md#query) | **POST** /v2/op/query | Query
[**update**](BatchOperationsApi.md#update) | **POST** /v2/op/update | Update


# **notify**
> notify(content_type, body)

Notify

This operation is intended to consume a notification payload so that all the entity data included by such notification is persisted, overwriting if necessary. This operation is useful when one NGSIv2 endpoint is subscribed to another NGSIv2 endpoint (federation scenarios).  The request payload must be an NGSIv2 notification payload.  The behaviour must be exactly the same as `POST /v2/op/update` with `actionType` equal to `append`. Response code: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import batch_operations_api
from openapi_client.model.notify_request import NotifyRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = batch_operations_api.BatchOperationsApi(api_client)
    content_type = "Content-Type_example" # str | 
    body = NotifyRequest(
        subscription_id="5aeb0ee97d4ef10a12a0262f",
        data=[{type=Room, id=DC_S1-D41, temperature={value=35.6, type=Number}}, {type=Room, id=Boe-Idearium, temperature={value=22.5, type=Number}}],
    ) # NotifyRequest | 
    options = "keyValues" # str | Options dictionary (optional) if omitted the server will use the default value of "keyValues"

    # example passing only required values which don't have defaults set
    try:
        # Notify
        api_instance.notify(content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling BatchOperationsApi->notify: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Notify
        api_instance.notify(content_type, body, options=options)
    except openapi_client.ApiException as e:
        print("Exception when calling BatchOperationsApi->notify: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  |
 **body** | [**NotifyRequest**](NotifyRequest.md)|  |
 **options** | **str**| Options dictionary | [optional] if omitted the server will use the default value of "keyValues"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query**
> [QueryResponse] query(content_type, body)

Query

The response payload is an Array containing one object per matching entity, or an empty array `[]` if  no entities are found. The entities follow the JSON entity representation format (described in the section \"JSON Entity Representation\"). The payload may contain the following elements (all of them optional): + `entities`: a list of entites to search for. Each element is represented by a JSON object with the   following elements:     + `id` or `idPattern`: Id or pattern of the affected entities. Both cannot be used at the same       time, but one of them must be present.     + `type` or `typePattern`: Type or type pattern of the entities to search for. Both cannot be used at       the same time. If omitted, it means \"any entity type\". + `attrs`: List of attributes to be provided (if not specified, all attributes). + `expression`: an expression composed of `q`, `mq`, `georel`, `geometry` and `coords` (see \"List    entities\" operation above about this field). + `metadata`: a list of metadata names to include in the response.    See \"Filtering out attributes and metadata\" section for more detail. Response code: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import batch_operations_api
from openapi_client.model.query_request import QueryRequest
from openapi_client.model.query_response import QueryResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = batch_operations_api.BatchOperationsApi(api_client)
    content_type = "Content-Type_example" # str | 
    body = QueryRequest(
        entities=[{idPattern=.*, type=Room}, {id=Car, type=P-9873-K}],
        attrs=[temperature, humidity],
        expression={},
        metadata=[accuracy, timestamp],
    ) # QueryRequest | 
    limit = 3.14 # float | Limit the number of entities to be retrieved. (optional)
    offset = 3.14 # float | Skip a number of records. (optional)
    order_by = "orderBy_example" # str | Criteria for ordering results. See \"Ordering Results\" section for details. (optional)
    options = "count" # str | Options dictionary (optional)

    # example passing only required values which don't have defaults set
    try:
        # Query
        api_response = api_instance.query(content_type, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BatchOperationsApi->query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query
        api_response = api_instance.query(content_type, body, limit=limit, offset=offset, order_by=order_by, options=options)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BatchOperationsApi->query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  |
 **body** | [**QueryRequest**](QueryRequest.md)|  |
 **limit** | **float**| Limit the number of entities to be retrieved. | [optional]
 **offset** | **float**| Skip a number of records. | [optional]
 **order_by** | **str**| Criteria for ordering results. See \&quot;Ordering Results\&quot; section for details. | [optional]
 **options** | **str**| Options dictionary | [optional]

### Return type

[**[QueryResponse]**](QueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(content_type, body)

Update

This operation allows to create, update and/or delete several entities in a single batch operation. The payload is an object with two properties: + `actionType`, to specify the kind of update action to do: either `append`, `appendStrict`, `update`,   `delete`, or `replace`. + `entities`, an array of entities, each entity specified using the JSON entity representation format   (described in the section \"JSON Entity Representation\"). This operation is split in as many individual operations as entities in the `entities` vector, so the `actionType` is executed for each one of them. Depending on the `actionType`, a mapping with regular non-batch operations can be done: * `append`: maps to `POST /v2/entities` (if the entity does not already exist) or `POST /v2/entities/<id>/attrs`   (if the entity already exists). * `appendStrict`: maps to `POST /v2/entities` (if the entity does not already exist) or   `POST /v2/entities/<id>/attrs?options=append` (if the entity already exists). * `update`: maps to `PATCH /v2/entities/<id>/attrs`. * `delete`: maps to `DELETE /v2/entities/<id>/attrs/<attrName>` on every attribute included in the entity or   to `DELETE /v2/entities/<id>` if no attribute were included in the entity. * `replace`: maps to `PUT /v2/entities/<id>/attrs`. Response: * Successful operation uses 204 No Content. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import batch_operations_api
from openapi_client.model.update_request import UpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = batch_operations_api.BatchOperationsApi(api_client)
    content_type = "Content-Type_example" # str | 
    body = UpdateRequest(
        action_type="append",
        entities=[{type=Room, id=Bcn-Welt, temperature={value=21.7}, humidity={value=60}}, {type=Room, id=Mad_Aud, temperature={value=22.9}, humidity={value=85}}],
    ) # UpdateRequest | 
    options = "keyValues" # str | Options dictionary (optional) if omitted the server will use the default value of "keyValues"

    # example passing only required values which don't have defaults set
    try:
        # Update
        api_instance.update(content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling BatchOperationsApi->update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update
        api_instance.update(content_type, body, options=options)
    except openapi_client.ApiException as e:
        print("Exception when calling BatchOperationsApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  |
 **body** | [**UpdateRequest**](UpdateRequest.md)|  |
 **options** | **str**| Options dictionary | [optional] if omitted the server will use the default value of "keyValues"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

