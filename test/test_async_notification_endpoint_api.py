"""
    hermes

    Messages sender service  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import hermes_client
from hermes_client.api.async_notification_endpoint_api import AsyncNotificationEndpointApi  # noqa: E501


class TestAsyncNotificationEndpointApi(unittest.TestCase):
    """AsyncNotificationEndpointApi unit test stubs"""

    def setUp(self):
        self.api = AsyncNotificationEndpointApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notification_api_v1_notification_post(self):
        """Test case for notification_api_v1_notification_post

        Notification  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
