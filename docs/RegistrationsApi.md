# openapi_client.RegistrationsApi

All URIs are relative to *http://orion.lab.fiware.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_registration**](RegistrationsApi.md#create_registration) | **POST** /v2/registrations | Create Registration
[**delete_registration**](RegistrationsApi.md#delete_registration) | **DELETE** /v2/registrations/{registrationId} | Delete Registration
[**list_registrations**](RegistrationsApi.md#list_registrations) | **GET** /v2/registrations | List Registrations
[**retrieve_registration**](RegistrationsApi.md#retrieve_registration) | **GET** /v2/registrations/{registrationId} | Retrieve Registration
[**update_registration**](RegistrationsApi.md#update_registration) | **PATCH** /v2/registrations/{registrationId} | Update Registration


# **create_registration**
> create_registration(content_type, body)

Create Registration

Creates a new context provider registration. This is typically used for binding context sources as providers of certain data. The registration is represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 201 Created * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import registrations_api
from openapi_client.model.create_registration_request import CreateRegistrationRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = registrations_api.RegistrationsApi(api_client)
    content_type = "Content-Type_example" # str | 
    body = CreateRegistrationRequest(
        description="Relative Humidity Context Source",
        data_provided={},
        provider={},
    ) # CreateRegistrationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Registration
        api_instance.create_registration(content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistrationsApi->create_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  |
 **body** | [**CreateRegistrationRequest**](CreateRegistrationRequest.md)|  |

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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration**
> delete_registration(registration_id)

Delete Registration

Cancels a context provider registration. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import registrations_api
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = registrations_api.RegistrationsApi(api_client)
    registration_id = "registrationId_example" # str | registration Id.

    # example passing only required values which don't have defaults set
    try:
        # Delete Registration
        api_instance.delete_registration(registration_id)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistrationsApi->delete_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| registration Id. |

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

# **list_registrations**
> [ListRegistrationsResponse] list_registrations()

List Registrations

Lists all the context provider registrations present in the system.

### Example


```python
import time
import openapi_client
from openapi_client.api import registrations_api
from openapi_client.model.list_registrations_response import ListRegistrationsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = registrations_api.RegistrationsApi(api_client)
    limit = 3.14 # float | Limit the number of registrations to be retrieved (optional)
    offset = 3.14 # float | Skip a number of registrations (optional)
    options = "count" # str | Options dictionary (optional) if omitted the server will use the default value of "count"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Registrations
        api_response = api_instance.list_registrations(limit=limit, offset=offset, options=options)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistrationsApi->list_registrations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Limit the number of registrations to be retrieved | [optional]
 **offset** | **float**| Skip a number of registrations | [optional]
 **options** | **str**| Options dictionary | [optional] if omitted the server will use the default value of "count"

### Return type

[**[ListRegistrationsResponse]**](ListRegistrationsResponse.md)

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

# **retrieve_registration**
> RetrieveRegistrationResponse retrieve_registration(registration_id)

Retrieve Registration

The response is the registration represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import registrations_api
from openapi_client.model.retrieve_registration_response import RetrieveRegistrationResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = registrations_api.RegistrationsApi(api_client)
    registration_id = "registrationId_example" # str | registration Id.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Registration
        api_response = api_instance.retrieve_registration(registration_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistrationsApi->retrieve_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| registration Id. |

### Return type

[**RetrieveRegistrationResponse**](RetrieveRegistrationResponse.md)

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

# **update_registration**
> update_registration(registration_id, content_type, body)

Update Registration

Only the fields included in the request are updated in the registration. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import registrations_api
from openapi_client.model.update_registration_request import UpdateRegistrationRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = registrations_api.RegistrationsApi(api_client)
    registration_id = "registrationId_example" # str | registration Id.
    content_type = "Content-Type_example" # str | 
    body = UpdateRegistrationRequest(
        expires="10/4/2017 12:00:00 AM",
    ) # UpdateRegistrationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update Registration
        api_instance.update_registration(registration_id, content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistrationsApi->update_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| registration Id. |
 **content_type** | **str**|  |
 **body** | [**UpdateRegistrationRequest**](UpdateRegistrationRequest.md)|  |

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

