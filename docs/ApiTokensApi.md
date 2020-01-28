# ververica_sdk.ApiTokensApi

All URIs are relative to *https://ververica.prod.bird.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_token_using_post**](ApiTokensApi.md#create_api_token_using_post) | **POST** /apitokens/v1/namespaces/{ns}/apitokens | createApiToken
[**delete_api_token_using_delete**](ApiTokensApi.md#delete_api_token_using_delete) | **DELETE** /apitokens/v1/namespaces/{ns}/apitokens/{apiTokenName} | deleteApiToken
[**get_api_token_using_get**](ApiTokensApi.md#get_api_token_using_get) | **GET** /apitokens/v1/namespaces/{ns}/apitokens/{apiTokenName} | getApiToken
[**list_api_tokens_using_get**](ApiTokensApi.md#list_api_tokens_using_get) | **GET** /apitokens/v1/namespaces/{ns}/apitokens | listApiTokens


# **create_api_token_using_post**
> CreateApiTokenResponse create_api_token_using_post(api_token, ns)

createApiToken

### Example
```python
from __future__ import print_function
import time
import ververica_sdk
from ververica_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_sdk.ApiTokensApi()
api_token = ververica_sdk.ApiToken() # ApiToken | apiToken
ns = 'ns_example' # str | ns

try:
    # createApiToken
    api_response = api_instance.create_api_token_using_post(api_token, ns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokensApi->create_api_token_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | [**ApiToken**](ApiToken.md)| apiToken | 
 **ns** | **str**| ns | 

### Return type

[**CreateApiTokenResponse**](CreateApiTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_token_using_delete**
> DeleteApiTokenResponse delete_api_token_using_delete(api_token_name, ns)

deleteApiToken

### Example
```python
from __future__ import print_function
import time
import ververica_sdk
from ververica_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_sdk.ApiTokensApi()
api_token_name = 'api_token_name_example' # str | apiTokenName
ns = 'ns_example' # str | ns

try:
    # deleteApiToken
    api_response = api_instance.delete_api_token_using_delete(api_token_name, ns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokensApi->delete_api_token_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token_name** | **str**| apiTokenName | 
 **ns** | **str**| ns | 

### Return type

[**DeleteApiTokenResponse**](DeleteApiTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_token_using_get**
> GetApiTokenResponse get_api_token_using_get(api_token_name, ns)

getApiToken

### Example
```python
from __future__ import print_function
import time
import ververica_sdk
from ververica_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_sdk.ApiTokensApi()
api_token_name = 'api_token_name_example' # str | apiTokenName
ns = 'ns_example' # str | ns

try:
    # getApiToken
    api_response = api_instance.get_api_token_using_get(api_token_name, ns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokensApi->get_api_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token_name** | **str**| apiTokenName | 
 **ns** | **str**| ns | 

### Return type

[**GetApiTokenResponse**](GetApiTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_tokens_using_get**
> ListApiTokensResponse list_api_tokens_using_get(ns)

listApiTokens

### Example
```python
from __future__ import print_function
import time
import ververica_sdk
from ververica_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ververica_sdk.ApiTokensApi()
ns = 'ns_example' # str | ns

try:
    # listApiTokens
    api_response = api_instance.list_api_tokens_using_get(ns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokensApi->list_api_tokens_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns** | **str**| ns | 

### Return type

[**ListApiTokensResponse**](ListApiTokensResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

