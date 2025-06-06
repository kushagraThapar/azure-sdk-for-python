# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.recoveryservices import RecoveryServicesClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRecoveryServicesVaultExtendedInfoOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(RecoveryServicesClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_vault_extended_info_get(self, resource_group):
        response = self.client.vault_extended_info.get(
            resource_group_name=resource_group.name,
            vault_name="str",
            api_version="2025-02-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_vault_extended_info_create_or_update(self, resource_group):
        response = self.client.vault_extended_info.create_or_update(
            resource_group_name=resource_group.name,
            vault_name="str",
            resource_extended_info_details={
                "algorithm": "str",
                "encryptionKey": "str",
                "encryptionKeyThumbprint": "str",
                "etag": "str",
                "id": "str",
                "integrityKey": "str",
                "name": "str",
                "type": "str",
            },
            api_version="2025-02-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_vault_extended_info_update(self, resource_group):
        response = self.client.vault_extended_info.update(
            resource_group_name=resource_group.name,
            vault_name="str",
            resource_extended_info_details={
                "algorithm": "str",
                "encryptionKey": "str",
                "encryptionKeyThumbprint": "str",
                "etag": "str",
                "id": "str",
                "integrityKey": "str",
                "name": "str",
                "type": "str",
            },
            api_version="2025-02-01",
        )

        # please add some check logic here by yourself
        # ...
