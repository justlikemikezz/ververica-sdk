# coding: utf-8

"""
    Ververica Platform API

    The Ververica Platform APIs, excluding Application Manager.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: platform@ververica.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.namespaces_api import NamespacesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNamespacesApi(unittest.TestCase):
    """NamespacesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.namespaces_api.NamespacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespace_using_post(self):
        """Test case for create_namespace_using_post

        createNamespace  # noqa: E501
        """
        pass

    def test_delete_namespace_using_delete(self):
        """Test case for delete_namespace_using_delete

        deleteNamespace  # noqa: E501
        """
        pass

    def test_get_namespace_using_get(self):
        """Test case for get_namespace_using_get

        getNamespace  # noqa: E501
        """
        pass

    def test_list_namespaces_using_get(self):
        """Test case for list_namespaces_using_get

        listNamespaces  # noqa: E501
        """
        pass

    def test_update_namespace_using_put(self):
        """Test case for update_namespace_using_put

        updateNamespace  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
