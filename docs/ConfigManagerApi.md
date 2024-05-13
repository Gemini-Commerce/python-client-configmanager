# configmanager.ConfigManagerApi

All URIs are relative to *https://config-manager.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_manager_bulk_set_configs**](ConfigManagerApi.md#config_manager_bulk_set_configs) | **POST** /configmanager.ConfigManager/BulkSetConfigs | BulkSetConfigs
[**config_manager_get_config**](ConfigManagerApi.md#config_manager_get_config) | **POST** /configmanager.ConfigManager/GetConfig | GetConfig
[**config_manager_get_tenant_id_by_code**](ConfigManagerApi.md#config_manager_get_tenant_id_by_code) | **POST** /configmanager.ConfigManager/GetTenantIdByCode | 


# **config_manager_bulk_set_configs**
> object config_manager_bulk_set_configs(body)

BulkSetConfigs

Bulk set configs

### Example

* OAuth Authentication (standardAuthorization):

```python
import time
import os
import configmanager
from configmanager.models.configmanager_bulk_set_configs_request import ConfigmanagerBulkSetConfigsRequest
from configmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://config-manager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = configmanager.Configuration(
    host = "https://config-manager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with configmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configmanager.ConfigManagerApi(api_client)
    body = configmanager.ConfigmanagerBulkSetConfigsRequest() # ConfigmanagerBulkSetConfigsRequest | 

    try:
        # BulkSetConfigs
        api_response = api_instance.config_manager_bulk_set_configs(body)
        print("The response of ConfigManagerApi->config_manager_bulk_set_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigManagerApi->config_manager_bulk_set_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigmanagerBulkSetConfigsRequest**](ConfigmanagerBulkSetConfigsRequest.md)|  | 

### Return type

**object**

### Authorization

[standardAuthorization](../README.md#standardAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_manager_get_config**
> ConfigmanagerConfigResponse config_manager_get_config(body)

GetConfig

Get a config

### Example

* OAuth Authentication (standardAuthorization):

```python
import time
import os
import configmanager
from configmanager.models.configmanager_config_response import ConfigmanagerConfigResponse
from configmanager.models.configmanager_get_config_request import ConfigmanagerGetConfigRequest
from configmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://config-manager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = configmanager.Configuration(
    host = "https://config-manager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with configmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configmanager.ConfigManagerApi(api_client)
    body = configmanager.ConfigmanagerGetConfigRequest() # ConfigmanagerGetConfigRequest | 

    try:
        # GetConfig
        api_response = api_instance.config_manager_get_config(body)
        print("The response of ConfigManagerApi->config_manager_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigManagerApi->config_manager_get_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigmanagerGetConfigRequest**](ConfigmanagerGetConfigRequest.md)|  | 

### Return type

[**ConfigmanagerConfigResponse**](ConfigmanagerConfigResponse.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_manager_get_tenant_id_by_code**
> ConfigmanagerGetTenantIdByCodeResponse config_manager_get_tenant_id_by_code(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import configmanager
from configmanager.models.configmanager_get_tenant_id_by_code_request import ConfigmanagerGetTenantIdByCodeRequest
from configmanager.models.configmanager_get_tenant_id_by_code_response import ConfigmanagerGetTenantIdByCodeResponse
from configmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://config-manager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = configmanager.Configuration(
    host = "https://config-manager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with configmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configmanager.ConfigManagerApi(api_client)
    body = configmanager.ConfigmanagerGetTenantIdByCodeRequest() # ConfigmanagerGetTenantIdByCodeRequest | 

    try:
        api_response = api_instance.config_manager_get_tenant_id_by_code(body)
        print("The response of ConfigManagerApi->config_manager_get_tenant_id_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigManagerApi->config_manager_get_tenant_id_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigmanagerGetTenantIdByCodeRequest**](ConfigmanagerGetTenantIdByCodeRequest.md)|  | 

### Return type

[**ConfigmanagerGetTenantIdByCodeResponse**](ConfigmanagerGetTenantIdByCodeResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

