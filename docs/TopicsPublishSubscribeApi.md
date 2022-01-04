# hermes_client.TopicsPublishSubscribeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_pubsub_demo_get**](TopicsPublishSubscribeApi.md#get_api_v1_pubsub_demo_get) | **GET** /api/v1/pubsub/demo | Get
[**publish_message_api_v1_pubsub_post**](TopicsPublishSubscribeApi.md#publish_message_api_v1_pubsub_post) | **POST** /api/v1/pubsub | Publish Message


# **get_api_v1_pubsub_demo_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_api_v1_pubsub_demo_get()

Get

### Example


```python
import time
import hermes_client
from hermes_client.api import topics_publish_subscribe_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hermes_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with hermes_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_publish_subscribe_api.TopicsPublishSubscribeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get
        api_response = api_instance.get_api_v1_pubsub_demo_get()
        pprint(api_response)
    except hermes_client.ApiException as e:
        print("Exception when calling TopicsPublishSubscribeApi->get_api_v1_pubsub_demo_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **publish_message_api_v1_pubsub_post**
> publish_message_api_v1_pubsub_post(publish_model)

Publish Message

### Example

* Bearer Authentication (Authenticator):

```python
import time
import hermes_client
from hermes_client.api import topics_publish_subscribe_api
from hermes_client.model.http_validation_error import HTTPValidationError
from hermes_client.model.error import Error
from hermes_client.model.publish_model import PublishModel
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
    api_instance = topics_publish_subscribe_api.TopicsPublishSubscribeApi(api_client)
    publish_model = PublishModel(
        topic="topic1",
        data=None,
    ) # PublishModel | 

    # example passing only required values which don't have defaults set
    try:
        # Publish Message
        api_instance.publish_message_api_v1_pubsub_post(publish_model)
    except hermes_client.ApiException as e:
        print("Exception when calling TopicsPublishSubscribeApi->publish_message_api_v1_pubsub_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_model** | [**PublishModel**](PublishModel.md)|  |

### Return type

void (empty response body)

### Authorization

[Authenticator](../README.md#Authenticator)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**401** | 3005 - Invalid credentials  3007 - Token is not active yet  3008 - Token is too old  3006 - The provided token is not well formed |  -  |
**403** | 3009 - User does not have the necessary permissions to perform the request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

