#!/usr/bin/env python3

import re

import objc
from Foundation import NSBundle

IOKit = NSBundle.bundleWithIdentifier_('com.apple.framework.IOKit')
functions = [
    ('IOServiceMatching', b'@*'),
    ('IORegistryEntryCreateCFProperties', b'IIo^@@I'),
    ('IOServiceGetMatchingServices', b'iI@o^I'),
    ('IOIteratorNext', b'II'),
    ('IORegistryEntryGetName', b'iIo[128c]'),
    ('IORegistryEntryGetNameInPlane', b'ii**'),
    ('IOObjectCopyClass', b'^*I'),
]
objc.loadBundleFunctions(IOKit, globals(), functions)


def get_ioreg(ioreg_class):
    """
    Retrieve a class in ioreg
    :param ioreg_class: (String) Class name
    :return: (Dict) Classes if more than more found
    (Object) Class if one found
    Note: Full classes and objects can be seen with: /usr/sbin/ioreg -bl
    """
    class_id = IOServiceMatching(ioreg_class.encode())

    err, iterator = IOServiceGetMatchingServices(0, class_id, None)
    if err:
        return None

    data = {}
    counter = 0
    service = IOIteratorNext(iterator)
    while service != 0:
        err, entry_properties = IORegistryEntryCreateCFProperties(service, None, None, 0)
        if not err:
            kr, name = IORegistryEntryGetName(service, None)
            entry_name = name.decode("utf-8").replace('\x00', '')
            data.update({entry_name: entry_properties})
        service = IOIteratorNext(iterator)
        counter += 1

    if counter == 1:
        return entry_properties
    else:
        return data


def print_keypair(key, value=None):
    """
    Print key and/or value nicely formatted
    :param key: (String) Key
    :param value: (Any) Value
    """
    if value is None:
        print('\t%s' % key)
    else:
        print('\t%-20s: %s' % (key, str(value)))


"""
Volumes
"""
print('Volumes:')
volumes = get_ioreg('AppleAPFSVolume')
for volume in volumes:
    print_keypair(volume, volumes[volume]['BSD Name'])

"""
Machine Information
"""
print('Machine Info:')
machine_info = get_ioreg('IOPlatformExpertDevice')
print_keypair('Serial Number', machine_info['IOPlatformSerialNumber'])
print_keypair('UUID', machine_info['IOPlatformUUID'])
print_keypair('Product Name', bytes(machine_info['model']).decode("utf-8"))

"""
Video Cards
"""
print('Video Cards:')
pci_devices = get_ioreg('IOPCIDevice')
for pci_key in pci_devices.keys():
    if 'model' in pci_devices[pci_key].keys():
        print_keypair(bytes(pci_devices[pci_key]['model']).decode("utf-8"))
print_keypair('Active GPU', get_ioreg('AppleMuxControl')['ActiveGPU'])

"""
BlueTooth
"""
print('BlueTooth:')
print_keypair('Address', get_ioreg('IOBluetoothHCIController')['BluetoothDeviceAddress'])
print_keypair('Name', get_ioreg('IOBluetoothHCIController')['BluetoothLocalName'])
print_keypair('Wake Enabled', get_ioreg('IOBluetoothHCIController')['RemoteWakeEnabled'])
print_keypair('Built-in', get_ioreg('IOBluetoothHCIController')['Built-In'])
print_keypair('Vendor', get_ioreg('IOBluetoothHCIController')['BluetoothVendor'])

print('BlueTooth Devices')
for bluetooth in get_ioreg('IOBluetoothHCIController'):
    if re.match(r'([0-9a-f]{2}-){5}([0-9a-f]{2})', bluetooth):
        print_keypair(get_ioreg('IOBluetoothHCIController')[bluetooth]['Product'])

"""
USB Devices
"""
print('USB Devices:')
usb_devices = get_ioreg('IOUSBHostDevice')
for usb_device in usb_devices.keys():
    if 'USB Product Name' in usb_devices[usb_device].keys():
        print('\t' + str(usb_devices[usb_device]['USB Product Name']))

"""
Battery Information
"""
print('Battery Info:')
print_keypair('Current Capacity', get_ioreg('AppleSmartBattery')['CurrentCapacity'])
print_keypair('Design Capacity', get_ioreg('AppleSmartBattery')['DesignCapacity'])
print_keypair('Cycle Count', get_ioreg('AppleSmartBattery')['CycleCount'])
print_keypair('Design Cycle Count', get_ioreg('AppleSmartBattery')['DesignCycleCount9C'])
print_keypair('Manufacturer', get_ioreg('AppleSmartBattery')['Manufacturer'])

exit()
