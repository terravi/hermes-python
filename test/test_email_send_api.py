"""
    hermes

    Messages sender service  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import hermes_client
from hermes_client.api.email_send_api import EmailSendApi  # noqa: E501


class TestEmailSendApi(unittest.TestCase):
    """EmailSendApi unit test stubs"""

    def setUp(self):
        self.api = EmailSendApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_email_api_v1_email_post(self):
        """Test case for email_api_v1_email_post

        Email  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()