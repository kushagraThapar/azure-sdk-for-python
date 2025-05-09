# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.monitor.aio import MonitorManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMonitorManagementServiceDiagnosticSettingsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(MonitorManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_service_diagnostic_settings_get(self, resource_group):
        response = await self.client.service_diagnostic_settings.get(
            resource_uri="str",
            api_version="2016-09-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_service_diagnostic_settings_create_or_update(self, resource_group):
        response = await self.client.service_diagnostic_settings.create_or_update(
            resource_uri="str",
            parameters={
                "location": "str",
                "eventHubAuthorizationRuleId": "str",
                "id": "str",
                "logs": [{"enabled": bool, "category": "str", "retentionPolicy": {"days": 0, "enabled": bool}}],
                "metrics": [
                    {"enabled": bool, "timeGrain": "1 day, 0:00:00", "retentionPolicy": {"days": 0, "enabled": bool}}
                ],
                "name": "str",
                "serviceBusRuleId": "str",
                "storageAccountId": "str",
                "tags": {"str": "str"},
                "type": "str",
                "workspaceId": "str",
            },
            api_version="2016-09-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_service_diagnostic_settings_update(self, resource_group):
        response = await self.client.service_diagnostic_settings.update(
            resource_uri="str",
            service_diagnostic_settings_resource={
                "eventHubAuthorizationRuleId": "str",
                "logs": [{"enabled": bool, "category": "str", "retentionPolicy": {"days": 0, "enabled": bool}}],
                "metrics": [
                    {"enabled": bool, "timeGrain": "1 day, 0:00:00", "retentionPolicy": {"days": 0, "enabled": bool}}
                ],
                "serviceBusRuleId": "str",
                "storageAccountId": "str",
                "tags": {"str": "str"},
                "workspaceId": "str",
            },
            api_version="2016-09-01",
        )

        # please add some check logic here by yourself
        # ...
