# openapi_client.APIEntryPointApi

All URIs are relative to *http://orion.lab.fiware.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_api_resources**](APIEntryPointApi.md#retrieve_api_resources) | **GET** /v2 | Retrieve API Resources


# **retrieve_api_resources**
> RetrieveApiResourcesResponse retrieve_api_resources()

Retrieve API Resources

This resource does not have any attributes. Instead it offers the initial API affordances in the form of the links in the JSON body. It is recommended to follow the “url” link values, [Link](https://tools.ietf.org/html/rfc5988) or Location headers where applicable to retrieve resources. Instead of constructing your own URLs, to keep your client decoupled from implementation details.

### Example


```python
import time
import openapi_client
from openapi_client.api import api_entry_point_api
from openapi_client.model.retrieve_api_resources_response import RetrieveApiResourcesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_entry_point_api.APIEntryPointApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve API Resources
        api_response = api_instance.retrieve_api_resources()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling APIEntryPointApi->retrieve_api_resources: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RetrieveApiResourcesResponse**](RetrieveApiResourcesResponse.md)

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

