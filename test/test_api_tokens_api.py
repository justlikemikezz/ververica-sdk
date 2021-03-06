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
from swagger_client.api.api_tokens_api import ApiTokensApi  # noqa: E501
from swagger_client.rest import ApiException


class TestApiTokensApi(unittest.TestCase):
    """ApiTokensApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.api_tokens_api.ApiTokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_api_token_using_post(self):
        """Test case for create_api_token_using_post

        createApiToken  # noqa: E501
        """
        pass

    def test_delete_api_token_using_delete(self):
        """Test case for delete_api_token_using_delete

        deleteApiToken  # noqa: E501
        """
        pass

    def test_get_api_token_using_get(self):
        """Test case for get_api_token_using_get

        getApiToken  # noqa: E501
        """
        pass

    def test_list_api_tokens_using_get(self):
        """Test case for list_api_tokens_using_get

        listApiTokens  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
