# For use in arg parsing
# parser.add_argument('-p', '--path', type=valid_path,
#                     action='store', dest='path', default=Path.home(),
#                     help='path')



def valid_path(path):
    """
    Validate path
    :param path: (str) Path
    :return: (Path) Path
    """
    parent = Path(path).parent
    if not parent.is_dir():
        print(f'{parent} is not a directory, make it?')
        if input('y/n: ').lower() == 'y':
            parent.mkdir(parents=True, exist_ok=True)
            Path(path)
        raise argparse.ArgumentTypeError(f'{path} is not a directory')
    return Path(path)
