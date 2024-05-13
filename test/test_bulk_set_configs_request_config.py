# coding: utf-8

"""
    Config Manager Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from configmanager.models.bulk_set_configs_request_config import BulkSetConfigsRequestConfig

class TestBulkSetConfigsRequestConfig(unittest.TestCase):
    """BulkSetConfigsRequestConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkSetConfigsRequestConfig:
        """Test BulkSetConfigsRequestConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkSetConfigsRequestConfig`
        """
        model = BulkSetConfigsRequestConfig()
        if include_optional:
            return BulkSetConfigsRequestConfig(
                key = '',
                value = '',
                business_domain = ''
            )
        else:
            return BulkSetConfigsRequestConfig(
                key = '',
                value = '',
        )
        """

    def testBulkSetConfigsRequestConfig(self):
        """Test BulkSetConfigsRequestConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
