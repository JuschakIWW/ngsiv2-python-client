# openapi_client.AttributesApi

All URIs are relative to *http://orion.lab.fiware.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attribute_data**](AttributesApi.md#get_attribute_data) | **GET** /v2/entities/{entityId}/attrs/{attrName} | Get attribute data
[**remove_a_single_attribute**](AttributesApi.md#remove_a_single_attribute) | **DELETE** /v2/entities/{entityId}/attrs/{attrName} | Remove a Single Attribute
[**update_attribute_data**](AttributesApi.md#update_attribute_data) | **PUT** /v2/entities/{entityId}/attrs/{attrName} | Update Attribute Data


# **get_attribute_data**
> GetAttributeDataResponse get_attribute_data(entity_id, attr_name)

Get attribute data

Returns a JSON object with the attribute data of the attribute. The object follows the JSON representation for attributes (described in \"JSON Attribute Representation\" section). Response: * Successful operation uses 200 OK. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import attributes_api
from openapi_client.model.get_attribute_data_response import GetAttributeDataResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    entity_id = "entityId_example" # str | Id of the entity
    attr_name = "attrName_example" # str | Name of the attribute to be retrieved.
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)
    metadata = "metadata_example" # str | A list of metadata names to include in the response. See \"Filtering out attributes and metadata\" section for more detail. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get attribute data
        api_response = api_instance.get_attribute_data(entity_id, attr_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttributesApi->get_attribute_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get attribute data
        api_response = api_instance.get_attribute_data(entity_id, attr_name, type=type, metadata=metadata)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttributesApi->get_attribute_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity |
 **attr_name** | **str**| Name of the attribute to be retrieved. |
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional]
 **metadata** | **str**| A list of metadata names to include in the response. See \&quot;Filtering out attributes and metadata\&quot; section for more detail. | [optional]

### Return type

[**GetAttributeDataResponse**](GetAttributeDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_a_single_attribute**
> remove_a_single_attribute(entity_id, attr_name)

Remove a Single Attribute

Removes an entity attribute. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import attributes_api
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    entity_id = "entityId_example" # str | Id of the entity.
    attr_name = "attrName_example" # str | Attribute name.
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a Single Attribute
        api_instance.remove_a_single_attribute(entity_id, attr_name)
    except openapi_client.ApiException as e:
        print("Exception when calling AttributesApi->remove_a_single_attribute: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a Single Attribute
        api_instance.remove_a_single_attribute(entity_id, attr_name, type=type)
    except openapi_client.ApiException as e:
        print("Exception when calling AttributesApi->remove_a_single_attribute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity. |
 **attr_name** | **str**| Attribute name. |
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_data**
> update_attribute_data(entity_id, attr_name, content_type, body)

Update Attribute Data

The request payload is an object representing the new attribute data. Previous attribute data is replaced by the one in the request. The object follows the JSON representation for attributes (described in \"JSON Attribute Representation\" section). Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import attributes_api
from openapi_client.model.update_attribute_data_request import UpdateAttributeDataRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)
    entity_id = "entityId_example" # str | Id of the entity to update
    attr_name = "attrName_example" # str | Attribute name
    content_type = "Content-Type_example" # str | 
    body = UpdateAttributeDataRequest(
        value=25.0,
        metadata={},
    ) # UpdateAttributeDataRequest | 
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Attribute Data
        api_instance.update_attribute_data(entity_id, attr_name, content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling AttributesApi->update_attribute_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Attribute Data
        api_instance.update_attribute_data(entity_id, attr_name, content_type, body, type=type)
    except openapi_client.ApiException as e:
        print("Exception when calling AttributesApi->update_attribute_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to update |
 **attr_name** | **str**| Attribute name |
 **content_type** | **str**|  |
 **body** | [**UpdateAttributeDataRequest**](UpdateAttributeDataRequest.md)|  |
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional]

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

