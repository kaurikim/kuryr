# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from unittest import mock

from oslo_utils import uuidutils

from kuryr.lib.binding.drivers import nested
from kuryr.lib import constants
from kuryr.lib import utils
from kuryr.tests.unit import base


class TestNestedDriver(base.TestCase):
    """Unit tests for nested driver"""

    @mock.patch('kuryr.lib.binding.drivers.utils.remove_device')
    def test_port_unbind(self, mock_remove_device):
        fake_docker_endpoint_id = utils.get_hash()
        fake_docker_network_id = utils.get_hash()
        fake_port_id = uuidutils.generate_uuid()
        fake_neutron_v4_subnet_id = uuidutils.generate_uuid()
        fake_neutron_v6_subnet_id = uuidutils.generate_uuid()
        fake_vif_details = {"port_filter": True, "ovs_hybrid_plug": False}
        fake_vif_type = "ovs"
        fake_port = self._get_fake_port(
            fake_docker_endpoint_id, fake_docker_network_id,
            fake_port_id, constants.PORT_STATUS_ACTIVE,
            fake_neutron_v4_subnet_id, fake_neutron_v6_subnet_id,
            vif_details=fake_vif_details, vif_type=fake_vif_type)
        nested.port_unbind(fake_docker_endpoint_id, fake_port['port'])
        mock_remove_device.assert_called_once()
