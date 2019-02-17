#!/usr/bin/env python

"""
Script:	wireless.py
Date:	2019-01-24

Platform: MacOS

Description:
Class to acceess wireless network information and modify
See: https://developer.apple.com/documentation/corewlan/
"""
__author__ = "thedzy"
__copyright__ = "Copyright 2019, thedzy"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "thedzy"
__email__ = "thedzy@hotmail.com"
__status__ = "Developer"


class Wifi():

	def __init__(self):
		import os
		import objc

		objc.loadBundle('CoreWLAN', bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
		                module_globals=globals())

	# Get commands
	# print("\n".join(dir(CWInterface)))

	# FINDS
	def find_Networks_with_hidden(self, ssid=None):
		"""
		Find a network and return the network object if it exists
		:param ssid: Name of the SSID
		:return: (Array) (CWNetwork)
		Note: Not compatible with 10.12 Sierra and lower
		"""
		networks = CWInterface.interface().scanForNetworksWithName_includeHidden_error_(ssid, True, None)[0]

		if ssid is None:
			return networks
		else:
			return networks.anyObject()

	def find_Networks(self, ssid=None):
		"""
		Find a network and return the network object if it exists
		:param ssid: Name of the SSID
		:return: (Array) (CWNetwork)
		"""
		networks = CWInterface.interface().scanForNetworksWithName_error_(ssid, None)[0]

		if ssid is None:
			return networks
		else:
			return networks.anyObject()

	def find_Network(self, ssid=None):
		"""
		Find a network and return True if it exists
		:param ssid: Name of the SSID
		:return: (Bool)
		"""
		if len(CWInterface.interface().scanForNetworksWithName_includeHidden_error_(ssid, True, None)[0]) == 0:
			return True
		else:
			return False

	def find_NetworkCached(self):
		"""
		The networks currently in the scan cache for the WLAN interface.
		:return: (Array) (CWNetwork). Returns nil in the case of an error.
		"""
		return CWInterface.interface().cachedScanResults()

	# GETS
	def get_activePHYMode(self):
		"""
		Dynamically queries the interface for the current active PHY mode. Returns kCWPHYModeNone in the case of an error,
		or if the interface is not participating in a network.
		:return:
			kCWPHYModeNone = 0
			kCWPHYMode11a = 1
			kCWPHYMode11b = 2
			kCWPHYMode11g = 3
			kCWPHYMode11n = 4
			kCWPHYMode11ac = 5
		"""
		return CWInterface.interface().phyMode()

	def get_aggregateNoise(self):
		"""
		Dynamically queries the interface for the current aggregate noise measurement. Returns 0 in the case of an error, or if the interface is not participating in a network.
		:return: (Integer) Noise
		"""
		return CWInterface.interface().aggregateNoise()

	def get_bssid(self):
		"""
		Dynamically queries the interface for the current BSSID. Returns a UTF-8 string formatted as <00:00:00:00:00:00>, or
		 nil in the case of an error, or if the interface is not participating in a network.
		:return:  String
		"""
		return CWInterface.interface().bssid()

	def get_capabilities(self):
		"""
		Dynamically queries the interface for the supported channels. Returns an array of CWChannel objects, or nil<i/> in
		the case of an error.
		:return: Array
		"""
		return CWInterface.interface().capabilities()

	def get_channel(self):
		"""
		Dynamically queries the interface for the current channel. Returns nil in the case of an error, or if the interface
		is not participating in a network.
		:return: String
		"""
		return CWInterface.interface().channel()

	def get_countryCode(self):
		"""
		Dynamically queries the interface for the current country code. Returns nil in the case of an error, or if the
		interface is OFF.
		:return: String
		"""
		return CWInterface.interface().countryCode()

	def get_deviceAttached(self):
		"""
		The interface has its corresponding hardware attached.
		:return: Bool
		"""
		return CWInterface.interface().deviceAttached()

	def get_hardwareAddress(self):
		"""
		The hardware media access control (MAC) address for the interface, returned as a UTF-8 string.
		:return: UTF-8 string
		"""
		return CWInterface.interface().hardwareAddress()

	def get_interfaceName(self):
		"""
		Returns a NSString representing the supported WLAN BSD interface name on the current system (i.e. "en1", "en2"). If
		there are no supported interfaces for the current system, then this method will return empty.
		Returns nil in the case of an error.
		:return: String
		"""
		return CWInterface.interface().interfaceName()

	def get_interfaceMode(self):
		"""
		Dynamically queries the interface for the current mode. Returns kCWInterfaceModeNone in the case of an error, or if
		the interface is not participating in a network.
		:return:
			none = 0
			kCWInterfaceModeStation = 1
			kCWInterfaceModeIBSS = 2 (ADHoc)
			kCWInterfaceModeHostAP = 3
		"""
		return CWInterface.interface().interfaceMode()

	def get_interfaceState(self):
		"""
		Dynamically queries the interface state
		:return:
			kCWInterfaceStateInactive = 0
			kCWInterfaceStateScanning = 1
			kCWInterfaceStateAuthenticating = 2
			kCWInterfaceStateAssociating = 3
			kCWInterfaceStateRunning = 4
		"""
		return CWInterface.interface().interfaceMode()

	def get_lastNetworkJoined(self):
		return CWInterface.interface().lastNetworkJoined()

	def get_lastPreferredNetworkJoined(self):
		return CWInterface.interface().lastPreferredNetworkJoined()

	def get_lastTetherDeviceJoined(self):
		return CWInterface.interface().lastTetherDeviceJoined()

	def get_maximumLinkSpeed(self):
		"""
		Dynamically queries the interface for the maximum link speed supported by the medium in bits per second.
		:return: Integer
		"""
		return CWInterface.interface().maximumLinkSpeed()

	def get_name(self):
		"""
		Returns a NSString representing the supported WLAN BSD interface name on the current system (i.e. "en1", "en2"). If
		there are no supported interfaces for the current system, then this method will return empty.
		Returns nil in the case of an error.
		:return: String
		"""
		return CWInterface.interface().name()

	def get_noiseMeasurement(self):
		"""
		Dynamically queries the interface for the current aggregate noise measurement. Returns 0 in the case of an error, or
		if the interface is not participating in a network.
		:return:  Integer
		"""
		return CWInterface.interface().noiseMeasurement()

	def get_networkInterfaceAvailable(self):
		"""
		Dynamically queries the interface for availability
		:return: Bool
		"""
		return CWInterface.interface().networkInterfaceAvailable()

	def get_powerOn(self):
		"""
		Dynamically queries the interface for the current power state. Returns NO in the case of an error.
		:return: bool
		"""
		return CWInterface.interface().powerOn()

	def get_rssiValue(self):
		"""
		Dynamically queries the interface for the current aggregate RSSI measurement. Returns 0 in the case of an error, or
		if the interface is not participating in a network.
		:return: Integer
		"""
		return CWInterface.interface().rssiValue()

	def get_security(self):
		"""
		Dynamically queries the interface for the security mode. Returns kCWSecurityUnknown in the case of an error, or if
		the interface is not participating in a network.
		:return:
			none = 0
			WEP = 1
			wpaPersonal = 2
			wpaPersonalMixed = 3
			wpa2Personal = 4
			personal = 5
			dynamicWEP = 6
			wpaEnterprise = 7
			wpaEnterpriseMixed = 8
			wpa2Enterprise = 9
			case enterprise = 10
			unknown = 9223372036854775807
		"""
		return CWInterface.interface().security()

	def get_serviceActive(self):
		"""
		The interface has its corresponding network service enabled. Returns NO in the case of an error.
		:return: Bool
		"""
		return CWInterface.interface().serviceActive()

	def get_ssid(self):
		"""
		Dynamically queries the interface for the current SSID. Returns nil in the case of an error, or if the interface is
		not participating in a network, or if the SSID can not be encoded as a valid UTF-8 or WinLatin1 string.
		:return: String
		"""
		return CWInterface.interface().ssid()

	def get_supportedWLANChannels(self):
		"""
		Dynamically queries the interface for the supported channels. Returns an array of CWChannel objects, or nil<i/> in
		the case of an error.
		:return: NSSet CWChannel
		See: https://developer.apple.com/documentation/corewlan/cwchannel?language=objc
		"""
		return CWInterface.interface().supportedWLANChannels()

	def get_transmitPower(self):
		"""
		Dynamically queries the interface for the current transmit power. Returns 0 in the case of an error.
		:return: Integer
		"""
		return CWInterface.interface().transmitPower()

	def get_transmitRate(self):
		"""
		Dynamically queries the interface for the current transmit rate. Returns 0 in the case of an error, or if the
		interface is not participating in a network.
		:return: Double
		"""
		return CWInterface.interface().transmitRate()

	def get_wlanChannel(self):
		"""
		Dynamically queries the interface for the current channel. Returns nil in the case of an error, or if the interface
		is not participating in a network.
		:return: CWChannel
		See: https://developer.apple.com/documentation/corewlan/cwchannel?language=objc
		"""
		return CWInterface.interface().wlanChannel()

	# GETS CONFIGURATION
	def get_configuration(self):
		"""
		Returns an immutable configuration for an AirPort WLAN interface.
		:return: CWConfiguration
		See: https://developer.apple.com/documentation/corewlan/cwconfiguration?language=objc
		"""
		return CWInterface.interface().configuration()

	def get_configuration_networkProfiles(self):
		"""
		The order of this array corresponds to the order in which the the CWNetworkProfile objects participate in the auto-join process.
		:return: Array
		"""
		return CWInterface.interface().configuration().networkProfiles()

	# GETS EAPOLCLIENT
	def get_eapolClient_eapolClientControlMode(self):
		"""
		Dynamically queries the EAP for the current control mode. Returns nil in the case of an error.
		:return: Integer
			kEAPOLControlModeNone = 0,
			kEAPOLControlModeUser = 1,
			kEAPOLControlModeLoginWindow = 2,
			kEAPOLControlModeSystem = 3
		"""
		return CWInterface.interface().eapolClient().eapolClientControlMode()

	def get_eapolClient_eapolClientStatus(self):
		return CWInterface.interface().eapolClient().eapolClientStatus()

	def get_eapolClient_eapolClientUUID(self):
		return CWInterface.interface().eapolClient().eapolClientUUID()

	def get_eapolClient_eapolClientControlState(self):
		"""
		Dynamically queries the EAP for the current control state. Returns nil in the case of an error.
		:return: Integer
			kEAPOLControlStateIdle = 0
			kEAPOLControlStateStarting = 1
			kEAPOLControlStateRunning = 2
			kEAPOLControlStateStopping = 3
		"""
		return CWInterface.interface().eapolClient().eapolClientControlState()

	def get_eapolClient_eapolClientSupplicantState(self):
		return CWInterface.interface().eapolClient().eapolClientSupplicantState()

	# SETS
	def set_power(self, power=True):
		"""
		Sets power state for the current interface . Returns current power state.
		:return: bool
		See: wifi_get_powerOn()
		"""
		iface.set_Power_error_(power, None)
		return CWInterface.interface().powerOn()

	# NETWORK ACCOCIATIONS
	def disassociate(self):
		"""
		This method has no effect if the interface is not associated to a network. This operation may require an
		administrator password.
		:return: Void
		"""
		CWInterface.interface().disassociate()

	def associateToEnterpriseNetwork_identity_username_password_error(self, ssid, identity, username, password,
	                                                                  error=None):
		"""
		Connects to the given enterprise network.
		:param network: (CWNetwork) The network to which the interface will associate.
		:param identity: (SecIdentityRef) The identity to use for IEEE 802.1X authentication. Holds the corresponding client certificate.
		:param username: (String) The username to use for IEEE 802.1X authentication.
		:param password: (String) The password to use for IEEE 802.1X authentication.
		:param error: (NSError) An NSError object passed by reference, which will be populated with the error code and the error description if an error occurs during the execution of this method. This parameter is optional and can be passed as nil.
		:return: A Boolean value which will indicate whether or not a failure occurred during execution. YES indicates no error occurred.
		"""
		network = wifi_find_Networks(ssid)
		if network is None:
			return False

		return CWInterface.interface().associateToEnterpriseNetwork_identity_username_password_error_(network, None,
		                                                                                              username,
		                                                                                              password, None)

	def associateToNetwork_password_error(self, ssid, password, error=None):
		"""
		Connects to the given enterprise network.
		:param network: (CWNetwork) The network to which the interface will associate.
		:param password: (String) The network passphrase or key. Required for association to WEP, WPA Personal, and WPA2 Personal networks.
		:param error: (NSError) An NSError object passed by reference, which will be populated with the error code and the error description if an error occurs during the execution of this method. This parameter is optional and can be passed as nil.
		:return: A Boolean value which will indicate whether or not a failure occurred during execution. YES indicates no error occurred.
		"""
		network = wifi_find_Networks(ssid)
		if network is None:
			return False

		return CWInterface.interface().associateToNetwork_password_error_(network, password, None)

	def removeNetwork(self, *ssid):
		"""
		Remove SSIDs from known and preferred networks
		:param ssid: (Array) (String) SSIDs to remove
		:return: Success
		"""
		# Create a new network configureation
		configuration_replcement = CWMutableConfiguration.alloc().initWithConfiguration_(
			CWInterface.interface().configuration())

		# Copy items not excluded by the ssid array
		profiles = list()
		for profile in list(CWInterface.interface().configuration().networkProfiles()):
			if profile.ssid() not in ssid:
				profiles.append(profile)

		# Set the new profiles
		configuration_replcement.setNetworkProfiles_(profiles)

		# Replace and return result
		return CWInterface.interface().commitConfiguration_authorization_error_(configuration_replcement, None, None)
