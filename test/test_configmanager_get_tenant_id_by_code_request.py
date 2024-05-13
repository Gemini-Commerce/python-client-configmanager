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

from configmanager.models.configmanager_get_tenant_id_by_code_request import ConfigmanagerGetTenantIdByCodeRequest

class TestConfigmanagerGetTenantIdByCodeRequest(unittest.TestCase):
    """ConfigmanagerGetTenantIdByCodeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigmanagerGetTenantIdByCodeRequest:
        """Test ConfigmanagerGetTenantIdByCodeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigmanagerGetTenantIdByCodeRequest`
        """
        model = ConfigmanagerGetTenantIdByCodeRequest()
        if include_optional:
            return ConfigmanagerGetTenantIdByCodeRequest(
                code = ''
            )
        else:
            return ConfigmanagerGetTenantIdByCodeRequest(
                code = '',
        )
        """

    def testConfigmanagerGetTenantIdByCodeRequest(self):
        """Test ConfigmanagerGetTenantIdByCodeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
