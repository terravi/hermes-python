# hermes_client.AsyncNotificationEndpointApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_api_v1_notification_post**](AsyncNotificationEndpointApi.md#notification_api_v1_notification_post) | **POST** /api/v1/notification | Notification


# **notification_api_v1_notification_post**
> bool, date, datetime, dict, float, int, list, str, none_type notification_api_v1_notification_post(notification_model)

Notification

### Example

* Bearer Authentication (Authenticator):

```python
import time
import hermes_client
from hermes_client.api import async_notification_endpoint_api
from hermes_client.model.http_validation_error import HTTPValidationError
from hermes_client.model.error import Error
from hermes_client.model.notification_model import NotificationModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hermes_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authenticator
configuration = hermes_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with hermes_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = async_notification_endpoint_api.AsyncNotificationEndpointApi(api_client)
    notification_model = NotificationModel(
        body=None,
        channel=None,
    ) # NotificationModel | 

    # example passing only required values which don't have defaults set
    try:
        # Notification
        api_response = api_instance.notification_api_v1_notification_post(notification_model)
        pprint(api_response)
    except hermes_client.ApiException as e:
        print("Exception when calling AsyncNotificationEndpointApi->notification_api_v1_notification_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_model** | [**NotificationModel**](NotificationModel.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Authenticator](../README.md#Authenticator)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**401** | 3007 - Token is not active yet  3008 - Token is too old |  -  |
**403** | 3009 - User does not have the necessary permissions to perform the request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

