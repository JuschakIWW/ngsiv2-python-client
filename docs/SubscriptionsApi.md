# openapi_client.SubscriptionsApi

All URIs are relative to *http://orion.lab.fiware.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /v2/subscriptions | Create Subscription
[**delete_subscription**](SubscriptionsApi.md#delete_subscription) | **DELETE** /v2/subscriptions/{subscriptionId} | Delete subscription
[**list_subscriptions**](SubscriptionsApi.md#list_subscriptions) | **GET** /v2/subscriptions | List Subscriptions
[**retrieve_subscription**](SubscriptionsApi.md#retrieve_subscription) | **GET** /v2/subscriptions/{subscriptionId} | Retrieve Subscription
[**update_subscription**](SubscriptionsApi.md#update_subscription) | **PATCH** /v2/subscriptions/{subscriptionId} | Update Subscription


# **create_subscription**
> create_subscription(content_type, body)

Create Subscription

Creates a new subscription. The subscription is represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 201 Created * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import subscriptions_api
from openapi_client.model.create_subscription_request import CreateSubscriptionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    content_type = "Content-Type_example" # str | 
    body = CreateSubscriptionRequest(
        description="One subscription to rule them all",
        subject={},
        notification={},
        expires="4/5/2016 2:00:00 PM",
        throttling=5,
    ) # CreateSubscriptionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Subscription
        api_instance.create_subscription(content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling SubscriptionsApi->create_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  |
 **body** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)|  |

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

# **delete_subscription**
> delete_subscription(subscription_id)

Delete subscription

Cancels subscription. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import subscriptions_api
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    subscription_id = "subscriptionId_example" # str | subscription Id.

    # example passing only required values which don't have defaults set
    try:
        # Delete subscription
        api_instance.delete_subscription(subscription_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SubscriptionsApi->delete_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription Id. |

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

# **list_subscriptions**
> [ListSubscriptionsResponse] list_subscriptions()

List Subscriptions

Returns a list of all the subscriptions present in the system. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import subscriptions_api
from openapi_client.model.list_subscriptions_response import ListSubscriptionsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    limit = 3.14 # float | Limit the number of subscriptions to be retrieved (optional)
    offset = 3.14 # float | Skip a number of subscriptions (optional)
    options = "count" # str | Options dictionary (optional) if omitted the server will use the default value of "count"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Subscriptions
        api_response = api_instance.list_subscriptions(limit=limit, offset=offset, options=options)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubscriptionsApi->list_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Limit the number of subscriptions to be retrieved | [optional]
 **offset** | **float**| Skip a number of subscriptions | [optional]
 **options** | **str**| Options dictionary | [optional] if omitted the server will use the default value of "count"

### Return type

[**[ListSubscriptionsResponse]**](ListSubscriptionsResponse.md)

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

# **retrieve_subscription**
> bool, date, datetime, dict, float, int, list, str, none_type retrieve_subscription(subscription_id)

Retrieve Subscription

The response is the subscription represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import subscriptions_api
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    subscription_id = "subscriptionId_example" # str | subscription Id.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Subscription
        api_response = api_instance.retrieve_subscription(subscription_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubscriptionsApi->retrieve_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription Id. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **update_subscription**
> update_subscription(subscription_id, content_type, body)

Update Subscription

Only the fields included in the request are updated in the subscription. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import subscriptions_api
from openapi_client.model.update_subscription_request import UpdateSubscriptionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    subscription_id = "subscriptionId_example" # str | subscription Id.
    content_type = "Content-Type_example" # str | 
    body = UpdateSubscriptionRequest(
        expires="4/5/2016 2:00:00 PM",
    ) # UpdateSubscriptionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update Subscription
        api_instance.update_subscription(subscription_id, content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling SubscriptionsApi->update_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription Id. |
 **content_type** | **str**|  |
 **body** | [**UpdateSubscriptionRequest**](UpdateSubscriptionRequest.md)|  |

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

