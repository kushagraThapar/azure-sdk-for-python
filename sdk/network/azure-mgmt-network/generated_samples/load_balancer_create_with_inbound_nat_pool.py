# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python load_balancer_create_with_inbound_nat_pool.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.load_balancers.begin_create_or_update(
        resource_group_name="rg1",
        load_balancer_name="lb",
        parameters={
            "location": "eastus",
            "properties": {
                "backendAddressPools": [],
                "frontendIPConfigurations": [
                    {
                        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb/frontendIPConfigurations/test",
                        "name": "test",
                        "properties": {
                            "privateIPAllocationMethod": "Dynamic",
                            "subnet": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/lbvnet/subnets/lbsubnet"
                            },
                        },
                        "zones": [],
                    }
                ],
                "inboundNatPools": [
                    {
                        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb/inboundNatPools/test",
                        "name": "test",
                        "properties": {
                            "backendPort": 8888,
                            "enableFloatingIP": True,
                            "enableTcpReset": True,
                            "frontendIPConfiguration": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb/frontendIPConfigurations/test"
                            },
                            "frontendPortRangeEnd": 8085,
                            "frontendPortRangeStart": 8080,
                            "idleTimeoutInMinutes": 10,
                            "protocol": "Tcp",
                        },
                    }
                ],
                "inboundNatRules": [],
                "loadBalancingRules": [],
                "outboundRules": [],
                "probes": [],
            },
            "sku": {"name": "Standard"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2024-07-01/examples/LoadBalancerCreateWithInboundNatPool.json
if __name__ == "__main__":
    main()
