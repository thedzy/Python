#!/usr/bin/env python3

__author__ = 'Shane Young'
__version__ = '1.0'
__email__ = 'thedzy@thedzy.com'
__date__ = '2023-06-21'
__credits__ = ''

__description__ = \
    """
    google_credentials.py: 
    Authenticate with Google json credentials
    """

import argparse
import logging
from pathlib import Path

import google.auth.exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def main() -> None:
    logger.info('Start')
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets'
    ]
    credentials = auth_google(scopes, options.google_credentials, False)
    if not credentials:
        logger.critical('Unable to authenticate')
        exit(1)

    # Create the Google Sheets API service
    sheets = build('sheets', 'v4', credentials=credentials)

    logger.info('Done')


def auth_google(scopes: list, credentials_json: str, save_json: bool = False) -> Credentials:
    """
    Authenticate with Google Workspaces API
    :param scopes: List of scopes to authenticate with
    :param credentials_json: Json file with credentials
    :param save_json: Save scope and token to json file
    :return: Credentials object
    """
    credentials_file = Path(__file__).parent.joinpath(credentials_json.name)
    # Check if credentials file already contains credentials and token
    try:
        credentials = Credentials.from_authorized_user_file(credentials_file, scopes)
        if credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        return credentials
    except ValueError:
        try:
            logger.info('Web credentials not found, attempting to generate new ones')
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)
            credentials = flow.run_local_server(port=0)

            # Save the credentials for the next run and skip web auth
            if save_json:
                credentials_json.write(credentials.to_json())
            return credentials
        except ValueError as err:
            logger.error(f'Error processing credentials: {err}', exc_info=True)
            return None
        except Exception as err:
            logger.critical(f'Unknown error: {err.args}', exc_info=True)
    except google.auth.exceptions.RefreshError as err:
        logger.error(f'Error refreshing credentials: {err.args[1].get("error_description")}')
        return None
    except Exception as err:
        logger.critical(f'Unknown error: {err.args}', exc_info=True)

    return None


if __name__ == '__main__':
    def valid_path(path):
        parent = Path(path).parent
        if not parent.is_dir():
            print(f'{parent} is not a directory, make it?')
            if input('y/n: ').lower() == 'y':
                parent.mkdir(parents=True, exist_ok=True)
                Path(path)
            raise argparse.ArgumentTypeError(f'{path} is not a directory')
        return Path(path)


    # Create argument parser
    parser = argparse.ArgumentParser(description=__description__)

    # Google Workspaces auth
    parser.add_argument('-g', '--google-credentials', type=argparse.FileType('r+'),
                        action='store', dest='google_credentials',
                        required=True,
                        help='Google Workspaces credentials file')

    parser.add_argument('--save-creds', default=False,
                        action='store_true', dest='save_credentials',
                        help='Save credentials with token and scope')

    # Debug option
    parser.add_argument('--debug', default=20,
                        action='store_const', dest='debug', const=10,
                        help=argparse.SUPPRESS)

    # Output
    parser.add_argument('-o', '--output', type=valid_path,
                        default=Path('/tmp').joinpath(Path(__file__).stem).with_suffix('.log'),
                        action='store', dest='output',
                        help='output log')

    options = parser.parse_args()

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('{message}', style='{'))
    logger.addHandler(handler)

    main()
