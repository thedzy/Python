# wireless.py
Function for easy read and setting of wireless on macOS.

# Functions
## find_Networks(self, ssid=None):
Find a network and return the network object if it exists
## find_Network(self, ssid=None):
Find a network and return True if it exists
## find_NetworkCached(self):
The networks currently in the scan cache for the WLAN interface.
## get_activePHYMode(self):
Dynamically queries the interface for the current active PHY mode. Returns kCWPHYModeNone in the case of an error, or if the interface is not participating in a network.
## get_aggregateNoise(self):
Dynamically queries the interface for the current aggregate noise measurement. Returns 0 in the case of an error, or if the interface is not participating in a network.
## get_bssid(self):
Dynamically queries the interface for the current BSSID. Returns a UTF-8 string formatted as <00:00:00:00:00:00>, or nil in the case of an error, or if the interface is not participating in a network.
## get_capabilities(self):
Dynamically queries the interface for the supported channels. Returns an array of CWChannel objects, or nil<i/> in the case of an error.
## get_channel(self):
Dynamically queries the interface for the current channel. Returns nil in the case of an error, or if the interface is not participating in a network.
## get_countryCode(self):
Dynamically queries the interface for the current country code. Returns nil in the case of an error, or if the interface is OFF.
## get_deviceAttached(self):
The interface has its corresponding hardware attached.
## get_hardwareAddress(self):
The hardware media access control (MAC) address for the interface, returned as a UTF-8 string.
## get_interfaceName(self):
Returns a NSString representing the supported WLAN BSD interface name on the current system (i.e. 'en1', 'en2'). If there are no supported interfaces for the current system, then this method will return empty.
## get_interfaceMode(self):
Dynamically queries the interface for the current mode. Returns kCWInterfaceModeNone in the case of an error, or if the interface is not participating in a network.
## get_interfaceState(self):
Dynamically queries the interface state
## get_lastNetworkJoined(self):
## get_lastPreferredNetworkJoined(self):
## get_lastTetherDeviceJoined(self):

---

## get_maximumLinkSpeed(self):
Dynamically queries the interface for the maximum link speed supported by the medium in bits per second.
## get_name(self):
Returns a NSString representing the supported WLAN BSD interface name on the current system (i.e. 'en1', 'en2'). If there are no supported interfaces for the current system, then this method will return empty.
## get_noiseMeasurement(self):
Dynamically queries the interface for the current aggregate noise measurement. Returns 0 in the case of an error, or if the interface is not participating in a network.
## get_networkInterfaceAvailable(self):
Dynamically queries the interface for availability
## get_powerOn(self):
Dynamically queries the interface for the current power state. Returns NO in the case of an error.
## get_rssiValue(self):
Dynamically queries the interface for the current aggregate RSSI measurement. Returns 0 in the case of an error, or if the interface is not participating in a network.
## get_security(self):
Dynamically queries the interface for the security mode. Returns kCWSecurityUnknown in the case of an error, or if the interface is not participating in a network.
## get_serviceActive(self):
The interface has its corresponding network service enabled. Returns NO in the case of an error.
## get_ssid(self):
Dynamically queries the interface for the current SSID. Returns nil in the case of an error, or if the interface is not participating in a network, or if the SSID can not be encoded as a valid UTF-8 or WinLatin1 string.
## get_supportedWLANChannels(self):
Dynamically queries the interface for the supported channels. Returns an array of CWChannel objects, or nil<i/> in the case of an error.
## get_transmitPower(self):
Dynamically queries the interface for the current transmit power. Returns 0 in the case of an error.
## get_transmitRate(self):
Dynamically queries the interface for the current transmit rate. Returns 0 in the case of an error, or if the interface is not participating in a network.
## get_wlanChannel(self):
Dynamically queries the interface for the current channel. Returns nil in the case of an error, or if the interface is not participating in a network.

---

## get_configuration(self):
Returns an immutable configuration for an AirPort WLAN interface.
## get_configuration_networkProfiles(self):
The order of this array corresponds to the order in which the the CWNetworkProfile objects participate in the auto-join process.
## get_eapolClient_eapolClientControlMode(self):
Dynamically queries the EAP for the current control mode. Returns nil in the case of an error.
## get_eapolClient_eapolClientStatus(self):
## get_eapolClient_eapolClientUUID(self):
## get_eapolClient_eapolClientControlState(self):
Dynamically queries the EAP for the current control state. Returns nil in the case of an error.
## get_eapolClient_eapolClientSupplicantState(self):

---

## set_power(self, power=True):
Sets power state for the current interface . Returns current power state.

---

## disassociate(self):
This method has no effect if the interface is not associated to a network. This operation may require an administrator password.
## associateToEnterpriseNetwork_identity_username_password_error(self, ssid, identity, username, password, error=None):
Connects to the given enterprise network.
## associateToNetwork_password_error(self, ssid, password, error=None):
Connects to the given enterprise network.
## removeNetwork(self, *ssid):
Remove SSIDs from known and preferred networks

** This API goes much deeper, indicate if you want to see more functions added