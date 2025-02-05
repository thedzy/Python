# For use in arg parsing
# parser.add_argument('-d', '--date', type=date,
#                     action='store', dest='date', required=True,
#                     help='end time, (format:  %Y-%m-%dT%H:%M)')

def date(formatted_date):
    """
    Validate and return a date
    :param formatted_date: (str) Date in the format YYYY-MM-DD HH:MM:SS
    :return: (datetime.datetime) Date and time
    """
    date_format = '%Y-%m-%dT%H:%M'
    try:
        valid_date = datetime.strptime(formatted_date, date_format)
        if valid_date < datetime.now():
            return valid_date
        else:
            raise argparse.ArgumentTypeError(f'This is not the DeLorean you are looking for: {formatted_date} is in the future')
    except ValueError:
        raise argparse.ArgumentTypeError(f'Invalid date: {formatted_date}, but be in the format of {date_format}')
