"""
    FIWARE-NGSI v2 Specification

    TODO: Add a description  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.list_entity_types_response import ListEntityTypesResponse
from openapi_client.model.retrieve_entity_type_response import RetrieveEntityTypeResponse


class TypesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.list_entity_types_endpoint = _Endpoint(
            settings={
                'response_type': ([ListEntityTypesResponse],),
                'auth': [],
                'endpoint_path': '/v2/types/',
                'operation_id': 'list_entity_types',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'offset',
                    'options',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'options',
                ],
                'validation': [
                    'limit',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                    },
                    ('offset',): {

                    },
                },
                'allowed_values': {
                    ('options',): {

                        "COUNT": "count",
                        "VALUES": "values"
                    },
                },
                'openapi_types': {
                    'limit':
                        (float,),
                    'offset':
                        (float,),
                    'options':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'offset': 'offset',
                    'options': 'options',
                },
                'location_map': {
                    'limit': 'query',
                    'offset': 'query',
                    'options': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.retrieve_entity_type_endpoint = _Endpoint(
            settings={
                'response_type': (RetrieveEntityTypeResponse,),
                'auth': [],
                'endpoint_path': '/v2/types/{entityType}',
                'operation_id': 'retrieve_entity_type',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'entity_type',
                ],
                'required': [
                    'entity_type',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'entity_type':
                        (str,),
                },
                'attribute_map': {
                    'entity_type': 'entityType',
                },
                'location_map': {
                    'entity_type': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def list_entity_types(
        self,
        **kwargs
    ):
        """List Entity Types  # noqa: E501

        If the `values` option is not in use, this operation returns a JSON array with the entity types. Each element is a JSON object with information about the type: * `type` : the entity type name. * `attrs` : the set of attribute names along with all the entities of such type, represented in   a JSON object whose keys are the attribute names and whose values contain information of such   attributes (in particular a list of the types used by attributes with that name along with all the   entities). * `count` : the number of entities belonging to that type. If the `values` option is used, the operation returns a JSON array with a list of entity type names as strings. Results are ordered by entity `type` in alphabetical order. Response code: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_entity_types(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (float): Limit the number of types to be retrieved.. [optional]
            offset (float): Skip a number of records.. [optional]
            options (str): Options dictionary.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [ListEntityTypesResponse]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.list_entity_types_endpoint.call_with_http_info(**kwargs)

    def retrieve_entity_type(
        self,
        entity_type,
        **kwargs
    ):
        """Retrieve entity type  # noqa: E501

        This operation returns a JSON object with information about the type: * `attrs` : the set of attribute names along with all the entities of such type, represented in   a JSON object whose keys are the attribute names and whose values contain information of such   attributes (in particular a list of the types used by attributes with that name along with all the   entities). * `count` : the number of entities belonging to that type. Response code: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.retrieve_entity_type(entity_type, async_req=True)
        >>> result = thread.get()

        Args:
            entity_type (str): Entity Type

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            RetrieveEntityTypeResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['entity_type'] = \
            entity_type
        return self.retrieve_entity_type_endpoint.call_with_http_info(**kwargs)

