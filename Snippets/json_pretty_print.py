#!/usr/bin/env python3

import json


def main():
	jsondata = {
		'object': {
			'users': [
				{
					'name': 'John Doe',
					'username': 'jdoe',
					'expires_utc': '',
					'identity': True,
					'admin': True
				},
				{
					'name': 'Jill Doe',
					'username': 'jidoe',
					'expires_utc': '',
					'identity': True,
					'admin': False
				},
			],
			'general': {
				'id': 1,
				'mac_address': 'AA:BB:CC:DD:EE:FF',
				'barcode_1': '1234567890',
				'barcode_2': '0987654321',
				'ip_address': '127.0.0.1',
				'status': {
					'enrolled': False,
					'provisioned': True,
					'decommisoined': False
				},
				'name': 'MacBook'
			},
			'software': {
				'applications': [],
				'available_software_updates': [],
				'available_updates': {},
				'fonts': [],
				'installed': [
					'Adobe Flash.pkg',
					'Safari.pkg',
					'Firefox.pkg',
					'Google Chrome.pkg',
				],
				'long_list1': [
					'precontain',
					'skeletony',
					'oostegite',
					'Saban',
					'chokidar',
					'cloam',
					'dysprosia',
					'nonvillager',
					'baggit',
					'Bucorvinae',
					'won',
					'enation',
					'waringin',
					'ninth',
					'inflected',
					'pilomotor',
					'gandergoose',
					'quadriad',
					'municipality',
					'interval'
				],
				'empty_list1': [],
				'long_list2': [
					'horsily',
					'tabidness',
					'arar',
					'Fontainea',
					'reactionarism',
					'gayatri',
					'loveful',
					'counterclaimant',
					'unsocialness',
					'protective'
				],
				'empty_list2': []
			}
		}
	}

	print(json.dumps(jsondata, indent=4, sort_keys=True))


if __name__ == '__main__':
	main()
