# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from .. import try_manual
from azure.cli.testsdk import ResourceGroupPreparer
from .preparers import VirtualNetworkPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    test.cmd('az feature register --namespace Microsoft.HardwareSecurityModules --name AzureDedicatedHSM')
    test.cmd(
        'az feature register --namespace Microsoft.Network --name AllowBaremetalServers')
    test.cmd('az network vnet create --name vn -g {rg} --subnet-name default')
    test.cmd('az vm create -g {rg} --name vm1 --image UbuntuLTS')
    test.cmd(
        'az network vnet subnet create --vnet-name vn -n GatewaySubnet -g {rg} --address-prefix 10.0.5.0/24')
    test.cmd(
        'az network vnet subnet create --vnet-name vn -g {rg} --name hsm --address-prefixes 10.0.2.0/24 --delegations Microsoft.HardwareSecurityModules/dedicatedHSMs')
    test.cmd(
        'az network public-ip create -n ERGWVIP -g {rg} --allocation-method Dynamic')
    test.cmd(
        'az network vnet-gateway create -n ERGW -l japaneast --public-ip-address ERGWVIP -g {rg} --vnet vn --sku standard --gateway-type ExpressRoute')


# EXAMPLE: /DedicatedHsm/put/Create a new or update an existing dedicated HSM
@try_manual
def step__dedicatedhsm_put_create_a_new_or_update_an_existing_dedicated_hsm(test, rg):
    test.cmd('az hardwaresecuritymodules dedicated-hsm create '
             '--name "hsm1" '
             '--location "japaneast" '
             '--network-profile-network-interfaces private-ip-address="10.0.2.21" '
             '--network-profile-subnet id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/vn/subnets/hsm" '
             '--stamp-id "stamp1" '
             '--sku name="SafeNet Luna Network HSM A790" '
             '--tags Dept="hsm" Environment="dogfood" '
             '--resource-group "{rg}"',
             checks=[])

# EXAMPLE: /DedicatedHsm/get/Get a dedicated HSM
@try_manual
def step__dedicatedhsm_get_get_a_dedicated_hsm(test, rg):
    test.cmd('az hardwaresecuritymodules dedicated-hsm show '
             '--name "hsm1" '
             '--resource-group "{rg}"',
             checks=[])

# EXAMPLE: /DedicatedHsm/get/List dedicated HSM devices in a resource group
@try_manual
def step__dedicatedhsm_get_list_dedicated_hsm_devices_in_a_resource_group(test, rg):
    test.cmd('az hardwaresecuritymodules dedicated-hsm list '
             '--resource-group "{rg}"',
             checks=[])

# EXAMPLE: /DedicatedHsm/get/List dedicated HSM devices in a subscription
@try_manual
def step__dedicatedhsm_get_list_dedicated_hsm_devices_in_a_subscription(test, rg):
    test.cmd('az hardwaresecuritymodules dedicated-hsm list',
             checks=[])


# EXAMPLE: /DedicatedHsm/patch/Update an existing dedicated HSM
@try_manual
def step__dedicatedhsm_patch_update_an_existing_dedicated_hsm(test, rg):
    test.cmd('az hardwaresecuritymodules dedicated-hsm update '
             '--name "hsm1" '
             '--tags Dept="hsm" Environment="dogfood" Slice="A" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /DedicatedHsm/delete/Delete a dedicated HSM
@try_manual
def step__dedicatedhsm_delete_delete_a_dedicated_hsm(test, rg):
    test.cmd('az hardwaresecuritymodules dedicated-hsm delete '
             '--name "hsm1" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def call_scenario(test, rg):
    try:
        setup(test, rg)
        step__dedicatedhsm_put_create_a_new_or_update_an_existing_dedicated_hsm(
            test, rg)
        step__dedicatedhsm_get_get_a_dedicated_hsm(test, rg)
        step__dedicatedhsm_get_list_dedicated_hsm_devices_in_a_resource_group(
            test, rg)
        step__dedicatedhsm_get_list_dedicated_hsm_devices_in_a_subscription(
            test, rg)
        step__dedicatedhsm_patch_update_an_existing_dedicated_hsm(test, rg)
        step__dedicatedhsm_delete_delete_a_dedicated_hsm(test, rg)
    except:
        test.cmd('az group delete -n {rg} --yes ')


@try_manual
class AzureDedicatedHSMResourceProviderScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitesthardwaresecuritymodules_hsm-group'[:7], location='japaneast', key='rg', parameter_name='rg')
    def test_hardwaresecuritymodules(self, rg):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        call_scenario(self, rg)
