"""
    hermes

    Messages sender service  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import hermes_client
from hermes_client.api.service_version_api import ServiceVersionApi  # noqa: E501


class TestServiceVersionApi(unittest.TestCase):
    """ServiceVersionApi unit test stubs"""

    def setUp(self):
        self.api = ServiceVersionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_version_api_v1_version_get(self):
        """Test case for version_api_v1_version_get

        Version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
