# ververica-sdk
The Ververica Platform APIs, excluding Application Manager.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.ververica.com](https://www.ververica.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ververica_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ververica_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import ververica_sdk
from ververica_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_sdk.ApiTokensApi(ververica_sdk.ApiClient(configuration))
api_token = ververica_sdk.ApiToken() # ApiToken | apiToken
ns = 'ns_example' # str | ns

try:
    # createApiToken
    api_response = api_instance.create_api_token_using_post(api_token, ns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokensApi->create_api_token_using_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://ververica.prod.bird.co*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiTokensApi* | [**create_api_token_using_post**](docs/ApiTokensApi.md#create_api_token_using_post) | **POST** /apitokens/v1/namespaces/{ns}/apitokens | createApiToken
*ApiTokensApi* | [**delete_api_token_using_delete**](docs/ApiTokensApi.md#delete_api_token_using_delete) | **DELETE** /apitokens/v1/namespaces/{ns}/apitokens/{apiTokenName} | deleteApiToken
*ApiTokensApi* | [**get_api_token_using_get**](docs/ApiTokensApi.md#get_api_token_using_get) | **GET** /apitokens/v1/namespaces/{ns}/apitokens/{apiTokenName} | getApiToken
*ApiTokensApi* | [**list_api_tokens_using_get**](docs/ApiTokensApi.md#list_api_tokens_using_get) | **GET** /apitokens/v1/namespaces/{ns}/apitokens | listApiTokens
*NamespacesApi* | [**create_namespace_using_post**](docs/NamespacesApi.md#create_namespace_using_post) | **POST** /namespaces/v1/namespaces | createNamespace
*NamespacesApi* | [**delete_namespace_using_delete**](docs/NamespacesApi.md#delete_namespace_using_delete) | **DELETE** /namespaces/v1/namespaces/{ns} | deleteNamespace
*NamespacesApi* | [**get_namespace_using_get**](docs/NamespacesApi.md#get_namespace_using_get) | **GET** /namespaces/v1/namespaces/{ns} | getNamespace
*NamespacesApi* | [**list_namespaces_using_get**](docs/NamespacesApi.md#list_namespaces_using_get) | **GET** /namespaces/v1/namespaces | listNamespaces
*NamespacesApi* | [**update_namespace_using_put**](docs/NamespacesApi.md#update_namespace_using_put) | **PUT** /namespaces/v1/namespaces/{ns} | updateNamespace


## Documentation For Models

 - [ApiToken](docs/ApiToken.md)
 - [CreateApiTokenResponse](docs/CreateApiTokenResponse.md)
 - [CreateNamespaceResponse](docs/CreateNamespaceResponse.md)
 - [DeleteApiTokenResponse](docs/DeleteApiTokenResponse.md)
 - [DeleteNamespaceResponse](docs/DeleteNamespaceResponse.md)
 - [GetApiTokenResponse](docs/GetApiTokenResponse.md)
 - [GetNamespaceResponse](docs/GetNamespaceResponse.md)
 - [ListApiTokensResponse](docs/ListApiTokensResponse.md)
 - [ListNamespacesResponse](docs/ListNamespacesResponse.md)
 - [Namespace](docs/Namespace.md)
 - [RoleBinding](docs/RoleBinding.md)
 - [UpdateNamespaceResponse](docs/UpdateNamespaceResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

platform@ververica.com
