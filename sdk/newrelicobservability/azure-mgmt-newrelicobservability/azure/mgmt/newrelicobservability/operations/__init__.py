# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._accounts_operations import AccountsOperations
from ._monitors_operations import MonitorsOperations
from ._organizations_operations import OrganizationsOperations
from ._plans_operations import PlansOperations
from ._billing_info_operations import BillingInfoOperations
from ._connected_partner_resources_operations import ConnectedPartnerResourcesOperations
from ._tag_rules_operations import TagRulesOperations
from ._monitored_subscriptions_operations import MonitoredSubscriptionsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Operations",
    "AccountsOperations",
    "MonitorsOperations",
    "OrganizationsOperations",
    "PlansOperations",
    "BillingInfoOperations",
    "ConnectedPartnerResourcesOperations",
    "TagRulesOperations",
    "MonitoredSubscriptionsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
