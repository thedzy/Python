#!/usr/bin/env python3

from popup_cocoa_file import *


def main():
	filedialog = FileDialog()
	file_target_path = filedialog.open(fileTypes=['txt'], allowsMultipleSelection=False, directory=FileDialog.HOME, extensionHidden=False, showsHiddenFiles=True, message='Please select a file to copy', defaultButton='Select', treatsFilePackagesAsDirectories=True)

	if len(file_target_path) == 0:
		print('Canceled')
		exit()
	elif len(file_target_path) == 1:
		try:
			with open(file_target_path[0], 'r') as file_target:
				file_target = file_target.read()
		except IOError as err:
			print('Error: ' + err)
			exit()
	else:
		print('Files Selected: ')
		print('\n'.join(file_target))

	file_target_name, file_target_ext = os.path.splitext(os.path.basename(file_target_path[0]))
	file_destination_path = filedialog.save(nameFieldStringValue=file_target_name, requiredFileType='txt', nameFieldLabel='Name of Copy:', allowsOtherFileTypes=True, directory=FileDialog.HOME, extensionHidden=False, showsHiddenFiles=True, message='Please choose a file to create/replace', defaultButton='Copy', treatsFilePackagesAsDirectories=True)

	if len(file_destination_path) == 0:
		print('Canceled')
		exit()
	else:
		print('File to create/replace: ')
		print(file_destination_path)
		try:
			with open(file_destination_path, 'w') as file_destination:
				file_destination.write(str(file_target))
				file_destination.close()
		except IOError as err:
			print('Error: ' + err)
			exit()


if __name__ == '__main__':
	main()
