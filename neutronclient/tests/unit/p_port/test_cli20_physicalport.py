# Copyright 2013 Big Switch Networks Inc.
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

import sys

from neutronclient.neutron.v2_0.p_port import physicalport
from neutronclient.tests.unit import test_cli20


class CLITestV20PhysicalPortJSON(test_cli20.CLITestV20Base):

    def test_create_physicalport_with_mandatory_params(self):
        """physical-port-create with mandatory (none) params."""
        resource = 'physical_port'
        cmd = physicalport.CreatePhysicalPort(test_cli20.MyApp(sys.stdout), None)
        name = 'my_physical_port'
        tenant_id = 'my-tenant'
        my_id = 'my-id'
        port_id = 'my-port-id'
        my_mac = 'my-mac'
        my_attachment = 'my-attachment'
        args = ['--admin-state-down',
                '--tenant-id', tenant_id,
                '--mac-address', my_mac,
                '--attachment', my_attachment]
        self._test_create_resource(resource, cmd, name, my_id, args,
                                   admin_state_up=True, tenant_id=tenant_id)

    def test_create_physicalport_with_all_params(self):
        """physical-port-create with all params set."""
        resource = 'physical_port'
        cmd = physicalport.CreatePhysicalPort(test_cli20.MyApp(sys.stdout), None)
        name = 'my-name'
        tenant_id = 'my-tenant'
        my_id = 'my-id'
        my_mac = 'my-mac'
        my_attachment = 'my-attachment'
        args = ['--admin-state-down',
                '--tenant-id', tenant_id,
                '--mac-address', my_mac,
                '--attachment', my_attachment]
        self._test_create_resource(resource, cmd, name, my_id, args,
                                   [], [], admin_state_up=False,
                                   tenant_id=tenant_id)

    def test_list_physicalports(self):
        """physical-port-list."""
        resources = "physical_ports"
        cmd = physicalport.ListPhysicalPort(test_cli20.MyApp(sys.stdout), None)
        self._test_list_resources(resources, cmd, True)

    def test_list_physicalports_pagination(self):
        """physical-port-list with pagination."""
        resources = "physical_ports"
        cmd = physicalport.ListPhysicalPort(test_cli20.MyApp(sys.stdout), None)
        self._test_list_resources_with_pagination(resources, cmd)

    def test_list_physicalports_sort(self):
        """sorted list: physical-port-list --sort-key name --sort-key id
        --sort-key asc --sort-key desc
        """
        resources = "physical_ports"
        cmd = physicalport.ListPhysicalPort(test_cli20.MyApp(sys.stdout), None)
        self._test_list_resources(resources, cmd,
                                  sort_key=["name", "id"],
                                  sort_dir=["asc", "desc"])

    def test_show_physicalport_id(self):
        """physical-port-show test_id."""
        resource = 'physical_port'
        cmd = physicalport.ShowPhysicalPort(test_cli20.MyApp(sys.stdout), None)
        args = ['--fields', 'id', self.test_id]
        self._test_show_resource(resource, cmd, self.test_id, args, ['id'])

    def test_show_physicalport_id_name(self):
        """physical-port-show."""
        resource = 'physical_port'
        cmd = physicalport.ShowPhysicalPort(test_cli20.MyApp(sys.stdout), None)
        args = ['--fields', 'id', '--fields', 'name', self.test_id]
        self._test_show_resource(resource, cmd, self.test_id,
                                 args, ['id', 'name'])

    def test_update_physicalport(self):
        """physical-port-update myid --name newname --tags a b."""
        resource = 'physical_port'
        cmd = physicalport.UpdatePhysicalPort(test_cli20.MyApp(sys.stdout), None)
        self._test_update_resource(resource, cmd, 'myid',
                                   ['myid', '--name', 'newname'],
                                   {'name': 'newname', })

    def test_delete_physicalport(self):
        """physical-port-delete my-id."""
        resource = 'physical_port'
        cmd = physicalport.DeletePhysicalPort(test_cli20.MyApp(sys.stdout), None)
        my_id = 'my-id'
        args = [my_id]
        self._test_delete_resource(resource, cmd, my_id, args)


class CLITestV20PhysicalPortXML(CLITestV20PhysicalPortJSON):
    format = 'xml'
