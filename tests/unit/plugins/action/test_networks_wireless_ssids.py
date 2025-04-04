import pytest
from ansible_collections.cisco.meraki.plugins.action.networks_wireless_ssids import (
    NetworksWirelessSsids,
)


class FakeParams:
    def __init__(self):
        self.data = {
            "meraki_api_key": "fakeapi",
            "networkId": "fakenetwork",
            "state": "present",
            "number": "0",
            "name": "Example1",
            "enabled": True,
            "authMode": "psk",
            "encryptionMode": "wpa",
            "wpaEncryptionMode": "WPA2 only",
            "psk": "12333f3333333333",
            "perClientBandwidthLimitDown": 1000,
            "perClientBandwidthLimitUp": 2000,
            "perSsidBandwidthLimitDown": 1001,
            "perSsidBandwidthLimitUp": 2001,
            "meraki_base_url": "https://api.meraki.com/api/v1",
            "meraki_single_request_timeout": 60,
            "meraki_certificate_path": "",
            "meraki_requests_proxy": "",
            "meraki_wait_on_rate_limit": True,
            "meraki_nginx_429_retry_wait_time": 60,
            "meraki_action_batch_retry_wait_time": 60,
            "meraki_retry_4xx_error": False,
            "meraki_retry_4xx_error_wait_time": 60,
            "meraki_maximum_retries": 2,
            "meraki_output_log": True,
            "meraki_log_path": "",
            "meraki_log_file_prefix": "meraki_api_",
            "meraki_print_console": True,
            "meraki_suppress_logging": True,
            "meraki_simulate": False,
            "meraki_be_geo_id": "",
            "meraki_use_iterator_for_get_pages": False,
            "meraki_inherit_logging_config": False,
            "activeDirectory": None,
            "adultContentFilteringEnabled": None,
            "apTagsAndVlanIds": None,
            "availabilityTags": None,
            "availableOnAllAps": None,
            "bandSelection": None,
            "concentratorNetworkId": None,
            "defaultVlanId": None,
            "disassociateClientsOnVpnFailover": None,
            "dnsRewrite": None,
            "dot11r": None,
            "dot11w": None,
            "enterpriseAdminAccess": None,
            "gre": None,
            "ipAssignmentMode": None,
            "lanIsolationEnabled": None,
            "ldap": None,
            "localRadius": None,
            "mandatoryDhcpEnabled": None,
            "minBitrate": None,
            "namedVlans": None,
            "oauth": None,
            "radiusAccountingEnabled": None,
            "radiusAccountingInterimInterval": None,
            "radiusAccountingServers": None,
            "radiusAttributeForGroupPolicies": None,
            "radiusAuthenticationNasId": None,
            "radiusCalledStationId": None,
            "radiusCoaEnabled": None,
            "radiusFailoverPolicy": None,
            "radiusFallbackEnabled": None,
            "radiusGuestVlanEnabled": None,
            "radiusGuestVlanId": None,
            "radiusLoadBalancingPolicy": None,
            "radiusOverride": None,
            "radiusProxyEnabled": None,
            "radiusServerAttemptsLimit": None,
            "radiusServerTimeout": None,
            "radiusServers": None,
            "radiusTestingEnabled": None,
            "secondaryConcentratorNetworkId": None,
            "speedBurst": None,
            "splashGuestSponsorDomains": None,
            "splashPage": None,
            "useVlanTagging": None,
            "visible": None,
            "vlanId": None,
            "walledGardenEnabled": None,
            "walledGardenRanges": None,
        }

    def get(self, get_value: str):
        return self.data.get(get_value)


problematic_keys = [
    "perClientBandwidthLimitDown",
    "perClientBandwidthLimitUp",
    "perSsidBandwidthLimitDown",
    "perSsidBandwidthLimitUp",
    "defaultVlanId",
    "radiusAccountingInterimInterval",
    "radiusGuestVlanId",
    "vlanId",
    "radiusServerAttemptsLimit",  # Ansible doc says: value must be between 1-5
    "radiusServerTimeout",  # Ansible doc says: must be between 1-10 seconds
]


@pytest.mark.parametrize("int_key", problematic_keys)
@pytest.mark.parametrize(
    "int_check_value",
    [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10000, "0", "1", "string", None],
)
def test_other_stuff(int_check_value, int_key):
    # Instantiate object with faked param class
    test_object = NetworksWirelessSsids(params=FakeParams(), meraki=None)
    # Patch in key and value under test
    test_object.new_object[int_key] = int_check_value
    # Call method with bad logic
    result = test_object.update_by_id_params()
    # Verify output is as expected
    assert result.get(int_key) == int_check_value
