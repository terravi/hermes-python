# hermes_client.EmailSendApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_api_v1_email_post**](EmailSendApi.md#email_api_v1_email_post) | **POST** /api/v1/email | Email


# **email_api_v1_email_post**
> email_api_v1_email_post(email_model)

Email

### Example

* Bearer Authentication (Authenticator):

```python
import time
import hermes_client
from hermes_client.api import email_send_api
from hermes_client.model.email_model import EmailModel
from hermes_client.model.http_validation_error import HTTPValidationError
from hermes_client.model.error import Error
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
    api_instance = email_send_api.EmailSendApi(api_client)
    email_model = EmailModel(
        sender="foo@bar.com",
        to=["recipient@bar.com"],
        cc=[],
        ccn=[],
        subject="Test",
        body="<h1>Test</h1>This is a <b>test</b> message",
        body_txt="This is a test message",
    ) # EmailModel | 

    # example passing only required values which don't have defaults set
    try:
        # Email
        api_instance.email_api_v1_email_post(email_model)
    except hermes_client.ApiException as e:
        print("Exception when calling EmailSendApi->email_api_v1_email_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_model** | [**EmailModel**](EmailModel.md)|  |

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
**401** | 3007 - Token is not active yet  3008 - Token is too old |  -  |
**403** | 3009 - User does not have the necessary permissions to perform the request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

