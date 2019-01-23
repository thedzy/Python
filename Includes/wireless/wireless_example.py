#!/usr/bin/env python

from wireless import *


def main():
	wifi = Wifi()
	print('Wifi Information')
	print_info('Interface', wifi.get_name())
	print_info('Hardware Address', wifi.get_hardwareAddress())
	print_info('SSID', wifi.get_ssid())
	print_info('BSSID', wifi.get_bssid())
	print_info('Channel', wifi.get_channel())
	print_info('Transmit Rate', wifi.get_transmitRate())

	wifi_networks = wifi.find_Networks()

	print('\n\nWifi Networks')
	print_info('SSID', 'Band')

	print("-" * 40)
	for wifi_network in wifi_networks:
		CWChannelBand = {
			0: "Unknown",
			1: "2GHz",
			2: "5GHz"
		}
		print_info(wifi_network.ssid(), CWChannelBand[wifi_network.wlanChannel().channelBand()])


def print_info(title='', status=''):
	"""
	Print rmessage and status
	:param msg: (string) Message Title
	:param status: (any) Message Status
	"""
	print('%-20s: %s' % (title, str(status)))


if __name__ == "__main__":
	main()
