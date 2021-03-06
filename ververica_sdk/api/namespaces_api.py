# coding: utf-8

"""
    Ververica Platform API

    The Ververica Platform APIs, excluding Application Manager.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: platform@ververica.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ververica_sdk.api_client import ApiClient


class NamespacesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_namespace_using_post(self, namespace, **kwargs):  # noqa: E501
        """createNamespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_namespace_using_post(namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Namespace namespace: namespace (required)
        :return: CreateNamespaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_namespace_using_post_with_http_info(namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.create_namespace_using_post_with_http_info(namespace, **kwargs)  # noqa: E501
            return data

    def create_namespace_using_post_with_http_info(self, namespace, **kwargs):  # noqa: E501
        """createNamespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_namespace_using_post_with_http_info(namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Namespace namespace: namespace (required)
        :return: CreateNamespaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_namespace_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `create_namespace_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'namespace' in params:
            body_params = params['namespace']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/v1/namespaces', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateNamespaceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_namespace_using_delete(self, ns, **kwargs):  # noqa: E501
        """deleteNamespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespace_using_delete(ns, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ns: ns (required)
        :return: DeleteNamespaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_namespace_using_delete_with_http_info(ns, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_namespace_using_delete_with_http_info(ns, **kwargs)  # noqa: E501
            return data

    def delete_namespace_using_delete_with_http_info(self, ns, **kwargs):  # noqa: E501
        """deleteNamespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespace_using_delete_with_http_info(ns, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ns: ns (required)
        :return: DeleteNamespaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ns']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_namespace_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ns' is set
        if ('ns' not in params or
                params['ns'] is None):
            raise ValueError("Missing the required parameter `ns` when calling `delete_namespace_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ns' in params:
            path_params['ns'] = params['ns']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/v1/namespaces/{ns}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteNamespaceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_namespace_using_get(self, ns, **kwargs):  # noqa: E501
        """getNamespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespace_using_get(ns, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ns: ns (required)
        :return: GetNamespaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_namespace_using_get_with_http_info(ns, **kwargs)  # noqa: E501
        else:
            (data) = self.get_namespace_using_get_with_http_info(ns, **kwargs)  # noqa: E501
            return data

    def get_namespace_using_get_with_http_info(self, ns, **kwargs):  # noqa: E501
        """getNamespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespace_using_get_with_http_info(ns, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ns: ns (required)
        :return: GetNamespaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ns']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_namespace_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ns' is set
        if ('ns' not in params or
                params['ns'] is None):
            raise ValueError("Missing the required parameter `ns` when calling `get_namespace_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ns' in params:
            path_params['ns'] = params['ns']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/v1/namespaces/{ns}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetNamespaceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_namespaces_using_get(self, **kwargs):  # noqa: E501
        """listNamespaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_namespaces_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListNamespacesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_namespaces_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_namespaces_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_namespaces_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """listNamespaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_namespaces_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListNamespacesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_namespaces_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/v1/namespaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListNamespacesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_namespace_using_put(self, namespace, ns, **kwargs):  # noqa: E501
        """updateNamespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_namespace_using_put(namespace, ns, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Namespace namespace: namespace (required)
        :param str ns: ns (required)
        :return: UpdateNamespaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_namespace_using_put_with_http_info(namespace, ns, **kwargs)  # noqa: E501
        else:
            (data) = self.update_namespace_using_put_with_http_info(namespace, ns, **kwargs)  # noqa: E501
            return data

    def update_namespace_using_put_with_http_info(self, namespace, ns, **kwargs):  # noqa: E501
        """updateNamespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_namespace_using_put_with_http_info(namespace, ns, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Namespace namespace: namespace (required)
        :param str ns: ns (required)
        :return: UpdateNamespaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'ns']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_namespace_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `update_namespace_using_put`")  # noqa: E501
        # verify the required parameter 'ns' is set
        if ('ns' not in params or
                params['ns'] is None):
            raise ValueError("Missing the required parameter `ns` when calling `update_namespace_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ns' in params:
            path_params['ns'] = params['ns']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'namespace' in params:
            body_params = params['namespace']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/v1/namespaces/{ns}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateNamespaceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
