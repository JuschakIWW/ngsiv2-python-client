# openapi_client.TypesApi

All URIs are relative to *http://orion.lab.fiware.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_entity_types**](TypesApi.md#list_entity_types) | **GET** /v2/types/ | List Entity Types
[**retrieve_entity_type**](TypesApi.md#retrieve_entity_type) | **GET** /v2/types/{entityType} | Retrieve entity type


# **list_entity_types**
> [ListEntityTypesResponse] list_entity_types()

List Entity Types

If the `values` option is not in use, this operation returns a JSON array with the entity types. Each element is a JSON object with information about the type: * `type` : the entity type name. * `attrs` : the set of attribute names along with all the entities of such type, represented in   a JSON object whose keys are the attribute names and whose values contain information of such   attributes (in particular a list of the types used by attributes with that name along with all the   entities). * `count` : the number of entities belonging to that type. If the `values` option is used, the operation returns a JSON array with a list of entity type names as strings. Results are ordered by entity `type` in alphabetical order. Response code: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import types_api
from openapi_client.model.list_entity_types_response import ListEntityTypesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types_api.TypesApi(api_client)
    limit = 3.14 # float | Limit the number of types to be retrieved. (optional)
    offset = 3.14 # float | Skip a number of records. (optional)
    options = "count" # str | Options dictionary. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Entity Types
        api_response = api_instance.list_entity_types(limit=limit, offset=offset, options=options)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesApi->list_entity_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Limit the number of types to be retrieved. | [optional]
 **offset** | **float**| Skip a number of records. | [optional]
 **options** | **str**| Options dictionary. | [optional]

### Return type

[**[ListEntityTypesResponse]**](ListEntityTypesResponse.md)

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

# **retrieve_entity_type**
> RetrieveEntityTypeResponse retrieve_entity_type(entity_type)

Retrieve entity type

This operation returns a JSON object with information about the type: * `attrs` : the set of attribute names along with all the entities of such type, represented in   a JSON object whose keys are the attribute names and whose values contain information of such   attributes (in particular a list of the types used by attributes with that name along with all the   entities). * `count` : the number of entities belonging to that type. Response code: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import types_api
from openapi_client.model.retrieve_entity_type_response import RetrieveEntityTypeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types_api.TypesApi(api_client)
    entity_type = "entityType_example" # str | Entity Type

    # example passing only required values which don't have defaults set
    try:
        # Retrieve entity type
        api_response = api_instance.retrieve_entity_type(entity_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TypesApi->retrieve_entity_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Entity Type |

### Return type

[**RetrieveEntityTypeResponse**](RetrieveEntityTypeResponse.md)

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

