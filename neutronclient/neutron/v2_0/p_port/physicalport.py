# Copyright 2013 Big Switch Networks
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

import argparse
import logging

from neutronclient.neutron import v2_0 as neutronv20
from neutronclient.openstack.common.gettextutils import _


class ListPhysicalPort(neutronv20.ListCommand):
    """List PhysicalPort that belong to a given tenant."""

    resource = 'physical_port'
    log = logging.getLogger(__name__ + '.ListPhysicalPort')
    list_columns = ['id', 'tenant_id', 'name', 'mac_address',
                    'attachment', 'port_id']
    _formatters = {}
    pagination_support = True
    sorting_support = True


class ShowPhysicalPort(neutronv20.ShowCommand):
    """Show information of a given PhysicalPort."""

    resource = 'physical_port'
    log = logging.getLogger(__name__ + '.ShowPhysicalPort')


class CreatePhysicalPort(neutronv20.CreateCommand):
    """Create a physical port."""

    resource = 'physical_port'
    log = logging.getLogger(__name__ + '.CreatePhysicalPort')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--mac-address',
            required=True,
            help=_('Mac Address of the physical port'))
        parser.add_argument(
            '--attachment',
            required=True,
            help=_('Attachment of the physical port'))
        parser.add_argument(
            '--name',
            help=_('Name for the physical port'))
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state',
            action='store_false',
            help=_('Set admin state up to false'))

    def args2body(self, parsed_args):
        body = {
            self.resource: {
                'admin_state_up': parsed_args.admin_state,}, }
        neutronv20.update_dict(parsed_args, body[self.resource],
                               ['name', 'tenant_id', 'mac_address',
                                'attachment', 'port_id'])
        return body


class UpdatePhysicalPort(neutronv20.UpdateCommand):
    """Update a given physical port."""

    resource = 'physical_port'
    log = logging.getLogger(__name__ + '.UpdatePhysicalPort')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--mac-address',
            help=_('Mac Address of the physical port'))
        parser.add_argument(
            '--attachment',
            help=_('Attachment of the physical port'))
        parser.add_argument(
            '--network-id',
            help=_('Neutron network id for the physical port'))
        parser.add_argument(
            '--tenant-id',
            help=_('Tenant id for the physical port'))
        parser.add_argument(
            '--name',
            help=_('Name for the physical port'))
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state',
            action='store_false',
            help=_('Set admin state up to false'))
        parser.add_argument(
            '--admin-state-up',
            dest='admin_state',
            action='store_true',
            help=_('Set admin state up to true'))

    def args2body(self, parsed_args):
        body = {
            self.resource: {
                'admin_state_up': parsed_args.admin_state,}, }
        neutronv20.update_dict(parsed_args, body[self.resource],
                               ['name', 'tenant_id', 'mac_address',
                                'attachment', 'network_id'])
        return body

class DeletePhysicalPort(neutronv20.DeleteCommand):
    """Delete a given physical port."""

    resource = 'physical_port'
    log = logging.getLogger(__name__ + '.DeletePhysicalPort')
