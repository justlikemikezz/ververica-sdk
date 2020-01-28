# ververica_sdk.NamespacesApi

All URIs are relative to *https://ververica.prod.bird.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespace_using_post**](NamespacesApi.md#create_namespace_using_post) | **POST** /namespaces/v1/namespaces | createNamespace
[**delete_namespace_using_delete**](NamespacesApi.md#delete_namespace_using_delete) | **DELETE** /namespaces/v1/namespaces/{ns} | deleteNamespace
[**get_namespace_using_get**](NamespacesApi.md#get_namespace_using_get) | **GET** /namespaces/v1/namespaces/{ns} | getNamespace
[**list_namespaces_using_get**](NamespacesApi.md#list_namespaces_using_get) | **GET** /namespaces/v1/namespaces | listNamespaces
[**update_namespace_using_put**](NamespacesApi.md#update_namespace_using_put) | **PUT** /namespaces/v1/namespaces/{ns} | updateNamespace


# **create_namespace_using_post**
> CreateNamespaceResponse create_namespace_using_post(namespace)

createNamespace

### Example
```python
from __future__ import print_function
import time
import ververica_sdk
from ververica_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_sdk.NamespacesApi()
namespace = ververica_sdk.Namespace() # Namespace | namespace

try:
    # createNamespace
    api_response = api_instance.create_namespace_using_post(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->create_namespace_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | [**Namespace**](Namespace.md)| namespace | 

### Return type

[**CreateNamespaceResponse**](CreateNamespaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespace_using_delete**
> DeleteNamespaceResponse delete_namespace_using_delete(ns)

deleteNamespace

### Example
```python
from __future__ import print_function
import time
import ververica_sdk
from ververica_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_sdk.NamespacesApi()
ns = 'ns_example' # str | ns

try:
    # deleteNamespace
    api_response = api_instance.delete_namespace_using_delete(ns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->delete_namespace_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns** | **str**| ns | 

### Return type

[**DeleteNamespaceResponse**](DeleteNamespaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespace_using_get**
> GetNamespaceResponse get_namespace_using_get(ns)

getNamespace

### Example
```python
from __future__ import print_function
import time
import ververica_sdk
from ververica_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_sdk.NamespacesApi()
ns = 'ns_example' # str | ns

try:
    # getNamespace
    api_response = api_instance.get_namespace_using_get(ns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespace_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns** | **str**| ns | 

### Return type

[**GetNamespaceResponse**](GetNamespaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaces_using_get**
> ListNamespacesResponse list_namespaces_using_get()

listNamespaces

### Example
```python
from __future__ import print_function
import time
import ververica_sdk
from ververica_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_sdk.NamespacesApi()

try:
    # listNamespaces
    api_response = api_instance.list_namespaces_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->list_namespaces_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListNamespacesResponse**](ListNamespacesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_namespace_using_put**
> UpdateNamespaceResponse update_namespace_using_put(namespace, ns)

updateNamespace

### Example
```python
from __future__ import print_function
import time
import ververica_sdk
from ververica_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_sdk.NamespacesApi()
namespace = ververica_sdk.Namespace() # Namespace | namespace
ns = 'ns_example' # str | ns

try:
    # updateNamespace
    api_response = api_instance.update_namespace_using_put(namespace, ns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->update_namespace_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | [**Namespace**](Namespace.md)| namespace | 
 **ns** | **str**| ns | 

### Return type

[**UpdateNamespaceResponse**](UpdateNamespaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

