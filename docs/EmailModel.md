# EmailModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** | Who is sending the message | 
**to** | **[str]** | List of email to which the mail is to be sent | 
**subject** | **str** | Subject of the message to be delivered by email | 
**cc** | **[str]** | List of email to which the mail is to be sent as copy | [optional]  if omitted the server will use the default value of []
**ccn** | **[str]** | List of email to which the mail is to be sent as             hidden copy | [optional]  if omitted the server will use the default value of []
**body** | **str** | HTML message to be delivered by email | [optional] 
**body_txt** | **str** | Plain text message to be delivered by email | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


