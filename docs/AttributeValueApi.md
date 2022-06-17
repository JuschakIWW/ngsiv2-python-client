# openapi_client.AttributeValueApi

All URIs are relative to *http://orion.lab.fiware.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attribute_value**](AttributeValueApi.md#get_attribute_value) | **GET** /v2/entities/{entityId}/attrs/{attrName}/value | Get Attribute Value
[**update_attribute_value**](AttributeValueApi.md#update_attribute_value) | **PUT** /v2/entities/{entityId}/attrs/{attrName}/value | Update Attribute Value


# **get_attribute_value**
> GetAttributeValueResponse get_attribute_value(entity_id, attr_name)

Get Attribute Value

This operation returns the `value` property with the value of the attribute. * If attribute value is JSON Array or Object:   * If `Accept` header can be expanded to `application/json` or `text/plain` return the value as a JSON with a     response type of application/json or text/plain (whichever is the first in `Accept` header or     `application/json` in case of `Accept: */*`).   * Else return a HTTP error \"406 Not Acceptable: accepted MIME types: application/json, text/plain\" * If attribute value is a string, number, null or boolean:   * If `Accept` header can be expanded to text/plain return the value as text. In case of a string, citation     marks are used at the begining and end.   * Else return a HTTP error \"406 Not Acceptable: accepted MIME types: text/plain\" Response: * Successful operation uses 200 OK. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import attribute_value_api
from openapi_client.model.get_attribute_value_response import GetAttributeValueResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = attribute_value_api.AttributeValueApi(api_client)
    entity_id = "entityId_example" # str | Id of the entity in question
    attr_name = "attrName_example" # str | Name of the attribute to be retrieved.
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Attribute Value
        api_response = api_instance.get_attribute_value(entity_id, attr_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttributeValueApi->get_attribute_value: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Attribute Value
        api_response = api_instance.get_attribute_value(entity_id, attr_name, type=type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttributeValueApi->get_attribute_value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity in question |
 **attr_name** | **str**| Name of the attribute to be retrieved. |
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional]

### Return type

[**GetAttributeValueResponse**](GetAttributeValueResponse.md)

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

# **update_attribute_value**
> update_attribute_value(entity_id, attr_name, content_type, body)

Update Attribute Value

The request payload is the new attribute value. * If the request payload MIME type is `application/json`, then the value of the attribute is set to   the JSON object or array coded in the payload (if the payload is not a valid JSON document,   then an error is returned). * If the request payload MIME type is `text/plain`, then the following algorithm is applied to the   payload:   * If the payload starts and ends with citation-marks (`\"`), the value is taken as a string     (the citation marks themselves are not considered part of the string)   * If `true` or `false`, the value is taken as a boolean.   * If `null`, the value is taken as null.   * If these first three tests 'fail', the text is interpreted as a number.   * If not a valid number, then an error is returned and the attribute's value is unchanged. The payload MIME type in the request is specified in the `Content-Type` HTTP header. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import attribute_value_api
from openapi_client.model.update_attribute_value_request import UpdateAttributeValueRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = attribute_value_api.AttributeValueApi(api_client)
    entity_id = "entityId_example" # str | Id of the entity to be updated.
    attr_name = "attrName_example" # str | Attribute name.
    content_type = "Content-Type_example" # str | 
    body = UpdateAttributeValueRequest(
        address="Ronda de la Comunicacion s/n",
        zip_code=28050,
        city="Madrid",
        country="Spain",
    ) # UpdateAttributeValueRequest | 
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Attribute Value
        api_instance.update_attribute_value(entity_id, attr_name, content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling AttributeValueApi->update_attribute_value: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Attribute Value
        api_instance.update_attribute_value(entity_id, attr_name, content_type, body, type=type)
    except openapi_client.ApiException as e:
        print("Exception when calling AttributeValueApi->update_attribute_value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to be updated. |
 **attr_name** | **str**| Attribute name. |
 **content_type** | **str**|  |
 **body** | [**UpdateAttributeValueRequest**](UpdateAttributeValueRequest.md)|  |
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

