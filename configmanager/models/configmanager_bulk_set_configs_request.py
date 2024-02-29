# coding: utf-8

"""
    configmanager/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from configmanager.models.bulk_set_configs_request_config import BulkSetConfigsRequestConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigmanagerBulkSetConfigsRequest(BaseModel):
    """
    ConfigmanagerBulkSetConfigsRequest
    """ # noqa: E501
    tenant_id: StrictStr = Field(alias="tenantId")
    configs: List[BulkSetConfigsRequestConfig]
    __properties: ClassVar[List[str]] = ["tenantId", "configs"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConfigmanagerBulkSetConfigsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in configs (list)
        _items = []
        if self.configs:
            for _item in self.configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['configs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigmanagerBulkSetConfigsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "configs": [BulkSetConfigsRequestConfig.from_dict(_item) for _item in obj.get("configs")] if obj.get("configs") is not None else None
        })
        return _obj


