#!/usr/bin/env python3
"""
Script:	pkgbuilder.py
Date:	2020-08-12	

Platform: macOS

Description:
This is a wrapper of the built in macOS pkgbuilder but allowing you to specify files currently on your machine to be
packaged as they are on the machine and quickly add scripts

Intended for quick/easy installs

A quick way to make an install from a file and add some quick scripts to support it
"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2020, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path


def main():
    # Create temporary directory and cleanup
    install_root = tempfile.TemporaryDirectory(prefix='root_')
    scripts_root = tempfile.TemporaryDirectory(prefix='scripts_')

    # Copy files and folders into temp directory
    if options.items:
        for item in options.items:
            copy_file(Path(item), install_root)
        print('Files Copied')
    else:
        print('Warning, no files included.  No receipt will be created')

    shebang = '#!/usr/bin/env python3' if options.python else '#!/bin/sh'
    # Copy/create scripts
    if options.preinstall:
        print('Creating pre install')
        Path(options.preinstall)
        if Path(options.preinstall).is_file():
            print('Using file {}'.format(options.preinstall))
            print(shutil.copy(options.preinstall, Path(scripts_root.name).joinpath('preinstall')))
        else:
            with open(Path(scripts_root.name).joinpath('preinstall'), 'w+') as preinstall_script:
                print('Saving code to file')
                preinstall_script.write(shebang + '\n')
                preinstall_script.write(options.preinstall)
        Path(scripts_root.name).joinpath('preinstall').chmod(0x755)

    if options.postinstall:
        print('Creating post install')
        Path(options.postinstall)
        if Path(options.preinstall).is_file():
            print('Using file {}'.format(options.postinstall))
            print(shutil.copy(options.postinstall, Path(scripts_root.name).joinpath('postinstall')))
        else:
            with open(Path(scripts_root.name).joinpath('postinstall'), 'w+') as postinstall_script:
                print('Saving code to file')
                preinstall_script.write(shebang + '\n')
                postinstall_script.write(options.postinstall)
        Path(scripts_root.name).joinpath('postinstall').chmod(0x755)

    cmd = ['/usr/bin/pkgbuild',
           '--ownership', 'recommended',
           '--identifier', options.identifier,
           '--version', str(options.version),
           '--scripts', scripts_root.name,
           ]
    if options.items:
        cmd.extend(('--root', install_root.name))
    else:
        cmd.append('--nopayload')
    cmd.append(options.package.name)

    return_code = subprocess.call(cmd)

    exit(return_code)


def copy_file(source, destination):
    """
    Copy file and permissions with all parents and permissions
    :param source: (Path) File
    :param destination: (Path) Directory
    :return: void
    """

    destination_object = Path(destination.name)
    source_object = Path('/')
    for parent in reversed(source.parents):
        destination_object = destination_object.joinpath(parent.name)
        source_object = source_object.joinpath(parent.name)
        destination_object.mkdir(exist_ok=True)
        try:
            shutil.copystat(source_object, destination_object)
        except PermissionError:
            shutil.copymode(source_object, destination_object)

    if source.is_file():
        shutil.copy2(source, destination_object)
    else:
        destination_object = destination_object.joinpath(source.name)
        shutil.copytree(source, destination_object)


if __name__ == '__main__':

    def parser_formatter(format_class, **kwargs):
        """
        Use a raw parser to use line breaks, etc
        :param format_class: (class) formatting class
        :param kwargs: (dict) kwargs for class
        :return: (class) formatting class
        """
        try:
            return lambda prog: format_class(prog, **kwargs)
        except TypeError:
            return format_class


    def valid_path(path):
        """
        Handle directory path
        :param path: (string) Path
        :return: Path, exception
        """
        file_object = Path(path)
        if file_object.is_dir() or file_object.is_file():
            return path
        else:
            raise argparse.ArgumentError('{} does not appear to be a valid directory or file'.format(path))


    prog_description = """
    This is a wrapper of the built in macOS pkgbuilder but allowing you to specify files currently on your machine to be
    packaged as they are on the machine and quickly add scripts
    
    Intended for quick/easy installs
    
    A quick way to make an install from a file and add some quick scripts to support it
    """

    prog_examples = """
    Example1: pkgbuilder.py -f /Applications/CocoaDialog.app  -a "rm -r /Applications/CocoaDialog.app/" -v 2.0 \
    -i com.example.cocoadialog ~/Desktop/CocoaDialog.pkg
    
    Example2: pkgbuilder.py -f /Library/Acme/Licence -b ~/Downloads/licence_install.sh ~/Desktop/acme_licence.pkg
    """

    parser = argparse.ArgumentParser(description='pkgbuilder.py' + prog_description + prog_examples,
                                     formatter_class=parser_formatter(argparse.RawTextHelpFormatter,
                                                                      indent_increment=4, max_help_position=12,
                                                                      width=160))

    # Package name
    parser.add_argument('package', type=argparse.FileType('w'),
                        metavar='PKG_FILE',
                        help='Package to create')

    # Files and folders
    parser.add_argument('-f', '--contents', type=valid_path, nargs=argparse.ONE_OR_MORE,
                        action='store', dest='items',
                        metavar='PATH',
                        help='Folders and all their sub folders')

    # Scripts
    parser.add_argument('-a', '--postinstall',
                        action='store', dest='preinstall', default=None,
                        metavar='CODE_OR_FILE',
                        help='Pre install script or command\n'
                             'Example -a "mkdir /path/to/dir"')
    parser.add_argument('-b', '--preinstall',
                        action='store', dest='postinstall', default=None,
                        metavar='CODE_OR_FILE',
                        help='Post install script or command\n'
                             'Example -b rm /path/to/install/file')
    parser.add_argument('--python',
                        action='store_true', dest='python', default=False,
                        help='Use a python shebang line instead of bash')

    # Metadata
    parser.add_argument('-v', '--version', type=float,
                        action='store', dest='version', default=1.0,
                        metavar='VERSION',
                        help='Version number\n'
                             'Default: %(default)s')
    parser.add_argument('-i', '--identifier',
                        action='store', dest='identifier',
                        metavar='STRING',
                        help='Package identifier\n',
                        required=True)

    options = parser.parse_args()

    main()
