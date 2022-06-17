# openapi_client.EntitiesApi

All URIs are relative to *http://orion.lab.fiware.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity**](EntitiesApi.md#create_entity) | **POST** /v2/entities | Create Entity
[**list_entities**](EntitiesApi.md#list_entities) | **GET** /v2/entities | List Entities
[**remove_entity**](EntitiesApi.md#remove_entity) | **DELETE** /v2/entities/{entityId} | Remove Entity
[**replace_all_entity_attributes**](EntitiesApi.md#replace_all_entity_attributes) | **PUT** /v2/entities/{entityId}/attrs | Replace all entity attributes
[**retrieve_entity**](EntitiesApi.md#retrieve_entity) | **GET** /v2/entities/{entityId} | Retrieve Entity
[**retrieve_entity_attributes**](EntitiesApi.md#retrieve_entity_attributes) | **GET** /v2/entities/{entityId}/attrs | Retrieve Entity Attributes
[**update_existing_entity_attributes**](EntitiesApi.md#update_existing_entity_attributes) | **PATCH** /v2/entities/{entityId}/attrs | Update Existing Entity Attributes
[**update_or_append_entity_attributes**](EntitiesApi.md#update_or_append_entity_attributes) | **POST** /v2/entities/{entityId}/attrs | Update or Append Entity Attributes


# **create_entity**
> create_entity(content_type, body)

Create Entity

The payload is an object representing the entity to be created. The object follows the JSON entity representation format (described in a \"JSON Entity Representation\" section). Response: * Successful operation uses 201 Created (if upsert option is not used) or 204 No Content (if   upsert option is used). Response includes a `Location` header with the URL of the   created entity. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import entities_api
from openapi_client.model.create_entity_request import CreateEntityRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    content_type = "Content-Type_example" # str | 
    body = CreateEntityRequest(
        type="Room",
        id="Bcn-Welt",
        temperature={},
        humidity={},
        location={},
    ) # CreateEntityRequest | 
    options = "keyValues" # str | Options dictionary (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Entity
        api_instance.create_entity(content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->create_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Entity
        api_instance.create_entity(content_type, body, options=options)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->create_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  |
 **body** | [**CreateEntityRequest**](CreateEntityRequest.md)|  |
 **options** | **str**| Options dictionary | [optional]

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

# **list_entities**
> [ListEntitiesResponse] list_entities()

List Entities

Retrieves a list of entities that match different criteria by id, type, pattern matching (either id or type) and/or those which match a query or geographical query (see [Simple Query Language](#simple_query_language) and  [Geographical Queries](#geographical_queries)). A given entity has to match all the criteria to be retrieved (i.e., the criteria is combined in a logical AND way). Note that pattern matching query parameters are incompatible (i.e. mutually exclusive) with their corresponding exact matching parameters, i.e. `idPattern` with `id` and `typePattern` with `type`. The response payload is an array containing one object per matching entity. Each entity follows the JSON entity representation format (described in \"JSON Entity Representation\" section). Response code: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import entities_api
from openapi_client.model.list_entities_response import ListEntitiesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    id = "id_example" # str | A comma-separated list of elements. Retrieve entities whose ID matches one of the elements in the list. Incompatible with `idPattern`. (optional)
    type = "type_example" # str | comma-separated list of elements. Retrieve entities whose type matches one of the elements in the list. Incompatible with `typePattern`. (optional)
    id_pattern = "idPattern_example" # str | A correctly formated regular expression. Retrieve entities whose ID matches the regular expression. Incompatible with `id`. (optional)
    type_pattern = "typePattern_example" # str | A correctly formated regular expression. Retrieve entities whose type matches the regular expression. Incompatible with `type`. (optional)
    q = "q_example" # str | A query expression, composed of a list of statements separated by `;`, i.e., q=statement1;statement2;statement3. See [Simple Query Language specification](#simple_query_language). (optional)
    mq = "mq_example" # str | A query expression for attribute metadata, composed of a list of statements separated by `;`, i.e., mq=statement1;statement2;statement3. See [Simple Query Language specification](#simple_query_language). (optional)
    georel = "georel_example" # str | Spatial relationship between matching entities and a reference shape. See [Geographical Queries](#geographical_queries). (optional)
    geometry = "geometry_example" # str | Geografical area to which the query is restricted. See [Geographical Queries](#geographical_queries). (optional)
    coords = "coords_example" # str | List of latitude-longitude pairs of coordinates separated by ';'. See [Geographical Queries](#geographical_queries). (optional)
    limit = 3.14 # float | Limits the number of entities to be retrieved (optional)
    offset = 3.14 # float | Establishes the offset from where entities are retrieved (optional)
    attrs = "attrs_example" # str | Comma-separated list of attribute names whose data are to be included in the response. The attributes are retrieved in the order specified by this parameter. If this parameter is not included, the attributes are retrieved in arbitrary order. See \"Filtering out attributes and metadata\" section for more detail. (optional)
    metadata = "metadata_example" # str | A list of metadata names to include in the response. See \"Filtering out attributes and metadata\" section for more detail. (optional)
    order_by = "orderBy_example" # str | Criteria for ordering results. See \"Ordering Results\" section for details. (optional)
    options = "count" # str | Options dictionary (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Entities
        api_response = api_instance.list_entities(id=id, type=type, id_pattern=id_pattern, type_pattern=type_pattern, q=q, mq=mq, georel=georel, geometry=geometry, coords=coords, limit=limit, offset=offset, attrs=attrs, metadata=metadata, order_by=order_by, options=options)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->list_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A comma-separated list of elements. Retrieve entities whose ID matches one of the elements in the list. Incompatible with &#x60;idPattern&#x60;. | [optional]
 **type** | **str**| comma-separated list of elements. Retrieve entities whose type matches one of the elements in the list. Incompatible with &#x60;typePattern&#x60;. | [optional]
 **id_pattern** | **str**| A correctly formated regular expression. Retrieve entities whose ID matches the regular expression. Incompatible with &#x60;id&#x60;. | [optional]
 **type_pattern** | **str**| A correctly formated regular expression. Retrieve entities whose type matches the regular expression. Incompatible with &#x60;type&#x60;. | [optional]
 **q** | **str**| A query expression, composed of a list of statements separated by &#x60;;&#x60;, i.e., q&#x3D;statement1;statement2;statement3. See [Simple Query Language specification](#simple_query_language). | [optional]
 **mq** | **str**| A query expression for attribute metadata, composed of a list of statements separated by &#x60;;&#x60;, i.e., mq&#x3D;statement1;statement2;statement3. See [Simple Query Language specification](#simple_query_language). | [optional]
 **georel** | **str**| Spatial relationship between matching entities and a reference shape. See [Geographical Queries](#geographical_queries). | [optional]
 **geometry** | **str**| Geografical area to which the query is restricted. See [Geographical Queries](#geographical_queries). | [optional]
 **coords** | **str**| List of latitude-longitude pairs of coordinates separated by &#39;;&#39;. See [Geographical Queries](#geographical_queries). | [optional]
 **limit** | **float**| Limits the number of entities to be retrieved | [optional]
 **offset** | **float**| Establishes the offset from where entities are retrieved | [optional]
 **attrs** | **str**| Comma-separated list of attribute names whose data are to be included in the response. The attributes are retrieved in the order specified by this parameter. If this parameter is not included, the attributes are retrieved in arbitrary order. See \&quot;Filtering out attributes and metadata\&quot; section for more detail. | [optional]
 **metadata** | **str**| A list of metadata names to include in the response. See \&quot;Filtering out attributes and metadata\&quot; section for more detail. | [optional]
 **order_by** | **str**| Criteria for ordering results. See \&quot;Ordering Results\&quot; section for details. | [optional]
 **options** | **str**| Options dictionary | [optional]

### Return type

[**[ListEntitiesResponse]**](ListEntitiesResponse.md)

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

# **remove_entity**
> remove_entity(entity_id)

Remove Entity

Delete the entity. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import entities_api
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    entity_id = "entityId_example" # str | Id of the entity to be deleted
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Entity
        api_instance.remove_entity(entity_id)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->remove_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Entity
        api_instance.remove_entity(entity_id, type=type)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->remove_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to be deleted |
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

# **replace_all_entity_attributes**
> replace_all_entity_attributes(entity_id, content_type, body)

Replace all entity attributes

The request payload is an object representing the new entity attributes. The object follows the JSON entity representation format (described in a \"JSON Entity Representation\" above), except that `id` and `type` are not allowed. The attributes previously existing in the entity are removed and replaced by the ones in the request. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import entities_api
from openapi_client.model.replace_all_entity_attributes_request import ReplaceAllEntityAttributesRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    entity_id = "entityId_example" # str | Id of the entity in question.
    content_type = "Content-Type_example" # str | 
    body = ReplaceAllEntityAttributesRequest(
        temperature={},
        seat_number={},
    ) # ReplaceAllEntityAttributesRequest | 
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)
    options = "keyValues" # str | Operations options (optional) if omitted the server will use the default value of "keyValues"

    # example passing only required values which don't have defaults set
    try:
        # Replace all entity attributes
        api_instance.replace_all_entity_attributes(entity_id, content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->replace_all_entity_attributes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace all entity attributes
        api_instance.replace_all_entity_attributes(entity_id, content_type, body, type=type, options=options)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->replace_all_entity_attributes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity in question. |
 **content_type** | **str**|  |
 **body** | [**ReplaceAllEntityAttributesRequest**](ReplaceAllEntityAttributesRequest.md)|  |
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional]
 **options** | **str**| Operations options | [optional] if omitted the server will use the default value of "keyValues"

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

# **retrieve_entity**
> RetrieveEntityResponse retrieve_entity(entity_id)

Retrieve Entity

The response is an object representing the entity identified by the ID. The object follows the JSON entity representation format (described in \"JSON Entity Representation\" section). This operation must return one entity element only, but there may be more than one entity with the same ID (e.g. entities with same ID but different types). In such case, an error message is returned, with the HTTP status code set to 409 Conflict. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import entities_api
from openapi_client.model.retrieve_entity_response import RetrieveEntityResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    entity_id = "entityId_example" # str | Id of the entity to be retrieved
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)
    attrs = "attrs_example" # str | Comma-separated list of attribute names whose data must be included in the response. The attributes are retrieved in the order specified by this parameter. See \"Filtering out attributes and metadata\" section for more detail. If this parameter is not included, the attributes are retrieved in arbitrary order, and all the attributes of the entity are included in the response. (optional)
    metadata = "metadata_example" # str | A list of metadata names to include in the response. See \"Filtering out attributes and metadata\" section for more detail. (optional)
    options = "keyValues" # str | Options dictionary (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Entity
        api_response = api_instance.retrieve_entity(entity_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->retrieve_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Entity
        api_response = api_instance.retrieve_entity(entity_id, type=type, attrs=attrs, metadata=metadata, options=options)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->retrieve_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to be retrieved |
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional]
 **attrs** | **str**| Comma-separated list of attribute names whose data must be included in the response. The attributes are retrieved in the order specified by this parameter. See \&quot;Filtering out attributes and metadata\&quot; section for more detail. If this parameter is not included, the attributes are retrieved in arbitrary order, and all the attributes of the entity are included in the response. | [optional]
 **metadata** | **str**| A list of metadata names to include in the response. See \&quot;Filtering out attributes and metadata\&quot; section for more detail. | [optional]
 **options** | **str**| Options dictionary | [optional]

### Return type

[**RetrieveEntityResponse**](RetrieveEntityResponse.md)

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

# **retrieve_entity_attributes**
> RetrieveEntityAttributesResponse retrieve_entity_attributes(entity_id)

Retrieve Entity Attributes

This request is similar to retreiving the whole entity, however this one omits the `id` and `type` fields. Just like the general request of getting an entire entity, this operation must return only one entity element. If more than one entity with the same ID is found (e.g. entities with same ID but different type), an error message is returned, with the HTTP status code set to 409 Conflict. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import entities_api
from openapi_client.model.retrieve_entity_attributes_response import RetrieveEntityAttributesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    entity_id = "entityId_example" # str | Id of the entity to be retrieved
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)
    attrs = "attrs_example" # str | Comma-separated list of attribute names whose data are to be included in the response. The attributes are retrieved in the order specified by this parameter. If this parameter is not included, the attributes are retrieved in arbitrary order, and all the attributes of the entity are included in the response. See \"Filtering out attributes and metadata\" section for more detail. (optional)
    metadata = "metadata_example" # str | A list of metadata names to include in the response. See \"Filtering out attributes and metadata\" section for more detail. (optional)
    options = "keyValues" # str | Options dictionary (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Entity Attributes
        api_response = api_instance.retrieve_entity_attributes(entity_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->retrieve_entity_attributes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Entity Attributes
        api_response = api_instance.retrieve_entity_attributes(entity_id, type=type, attrs=attrs, metadata=metadata, options=options)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->retrieve_entity_attributes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to be retrieved |
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional]
 **attrs** | **str**| Comma-separated list of attribute names whose data are to be included in the response. The attributes are retrieved in the order specified by this parameter. If this parameter is not included, the attributes are retrieved in arbitrary order, and all the attributes of the entity are included in the response. See \&quot;Filtering out attributes and metadata\&quot; section for more detail. | [optional]
 **metadata** | **str**| A list of metadata names to include in the response. See \&quot;Filtering out attributes and metadata\&quot; section for more detail. | [optional]
 **options** | **str**| Options dictionary | [optional]

### Return type

[**RetrieveEntityAttributesResponse**](RetrieveEntityAttributesResponse.md)

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

# **update_existing_entity_attributes**
> update_existing_entity_attributes(entity_id, content_type, body)

Update Existing Entity Attributes

The request payload is an object representing the attributes to update. The object follows the JSON entity representation format (described in \"JSON Entity Representation\" section), except that `id` and `type` are not allowed. The entity attributes are updated with the ones in the payload. In addition to that, if one or more attributes in the payload doesn't exist in the entity, an error is returned. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import entities_api
from openapi_client.model.update_existing_entity_attributes_request import UpdateExistingEntityAttributesRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    entity_id = "entityId_example" # str | Id of the entity to be updated
    content_type = "Content-Type_example" # str | 
    body = UpdateExistingEntityAttributesRequest(
        temperature={},
        seat_number={},
    ) # UpdateExistingEntityAttributesRequest | 
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)
    options = "keyValues" # str | Operations options (optional) if omitted the server will use the default value of "keyValues"

    # example passing only required values which don't have defaults set
    try:
        # Update Existing Entity Attributes
        api_instance.update_existing_entity_attributes(entity_id, content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->update_existing_entity_attributes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Existing Entity Attributes
        api_instance.update_existing_entity_attributes(entity_id, content_type, body, type=type, options=options)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->update_existing_entity_attributes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to be updated |
 **content_type** | **str**|  |
 **body** | [**UpdateExistingEntityAttributesRequest**](UpdateExistingEntityAttributesRequest.md)|  |
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional]
 **options** | **str**| Operations options | [optional] if omitted the server will use the default value of "keyValues"

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

# **update_or_append_entity_attributes**
> update_or_append_entity_attributes(entity_id, content_type, body)

Update or Append Entity Attributes

The request payload is an object representing the attributes to append or update. The object follows the JSON entity representation format (described in \"JSON Entity Representation\" section), except that `id` and `type` are not allowed. The entity attributes are updated with the ones in the payload, depending on whether the `append` operation option is used or not. * If `append` is not used: the entity attributes are updated (if they previously exist) or appended   (if they don't previously exist) with the ones in the payload. * If `append` is used (i.e. strict append semantics): all the attributes in the payload not   previously existing in the entity are appended. In addition to that, in case some of the   attributes in the payload already exist in the entity, an error is returned. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example


```python
import time
import openapi_client
from openapi_client.api import entities_api
from openapi_client.model.update_or_append_entity_attributes_request import UpdateOrAppendEntityAttributesRequest
from pprint import pprint
# Defining the host is optional and defaults to http://orion.lab.fiware.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://orion.lab.fiware.org"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    entity_id = "entityId_example" # str | Entity id to be updated
    content_type = "Content-Type_example" # str | 
    body = UpdateOrAppendEntityAttributesRequest(
        ambient_noise={},
    ) # UpdateOrAppendEntityAttributesRequest | 
    type = "type_example" # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)
    options = "append" # str | Operations options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update or Append Entity Attributes
        api_instance.update_or_append_entity_attributes(entity_id, content_type, body)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->update_or_append_entity_attributes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update or Append Entity Attributes
        api_instance.update_or_append_entity_attributes(entity_id, content_type, body, type=type, options=options)
    except openapi_client.ApiException as e:
        print("Exception when calling EntitiesApi->update_or_append_entity_attributes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Entity id to be updated |
 **content_type** | **str**|  |
 **body** | [**UpdateOrAppendEntityAttributesRequest**](UpdateOrAppendEntityAttributesRequest.md)|  |
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional]
 **options** | **str**| Operations options | [optional]

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

