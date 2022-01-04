# hermes_client.ServiceVersionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_api_v1_version_get**](ServiceVersionApi.md#version_api_v1_version_get) | **GET** /api/v1/version | Version


# **version_api_v1_version_get**
> Version version_api_v1_version_get()

Version

### Example


```python
import time
import hermes_client
from hermes_client.api import service_version_api
from hermes_client.model.version import Version
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hermes_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with hermes_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = service_version_api.ServiceVersionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Version
        api_response = api_instance.version_api_v1_version_get()
        pprint(api_response)
    except hermes_client.ApiException as e:
        print("Exception when calling ServiceVersionApi->version_api_v1_version_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

