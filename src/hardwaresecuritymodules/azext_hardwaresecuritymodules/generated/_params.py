# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_hardwaresecuritymodules.action import (
    AddNetworkProfileSubnet,
    AddNetworkProfileNetworkInterfaces
)


def load_arguments(self, _):

    with self.argument_context('hardwaresecuritymodules dedicated-hsm list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('top', help='Maximum number of results to return.')

    with self.argument_context('hardwaresecuritymodules dedicated-hsm show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('name', options_list=[
                   '--name', '-n'], help='The name of the dedicated HSM.')

    with self.argument_context('hardwaresecuritymodules dedicated-hsm create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('name', options_list=[
                   '--name', '-n'], help='Name of the dedicated Hsm')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('sku', type=str,
                   help='The HSM device SKU if a non-standard HSM is wanted (default is: SafeNet Luna Network HSM A790)')
        c.argument('zones', nargs='+',
                   help='The Dedicated Hsm zones.')
        c.argument('tags', tags_type)
        c.argument(
            'stamp_id', help='This field will be used when RP does not support Availability zones.')
        c.argument('network_profile_subnet', options_list=['--network-profile-subnet', '-s'], action=AddNetworkProfileSubnet, nargs='+', help='Specifies the identifier '
                   'of the subnet. Expected value: id=xx.')
        c.argument('network_profile_network_interfaces', options_list=['--network-profile-network-interfaces', '-i'], action=AddNetworkProfileNetworkInterfaces, nargs='+', help='Sp'
                   'ecifies the list of resource Ids for the network interfaces associated with the dedicated HSM. Expe'
                   'cted value: -interfaces private-ip-address=xx.')

    with self.argument_context('hardwaresecuritymodules dedicated-hsm update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('name', options_list=[
                   '--name', '-n'], help='Name of the dedicated HSM')
        c.argument('tags', tags_type)

    with self.argument_context('hardwaresecuritymodules dedicated-hsm delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('name', options_list=[
                   '--name', '-n'], help='The name of the dedicated HSM to delete')
