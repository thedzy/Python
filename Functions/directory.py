# For use in arg parsing
# parser.add_argument('-p', '--path', type=directory,
#                     action='store', dest='path', default=Path.home(),
#                     help='directory')


def directory(path):
    """
    Validate path is a directory
    :param path: (str) Path to directory
    :return: (Path) Directory
    """
    if not Path(path).is_dir():
        print(f'{path} is not a directory, make it?')
        if input('y/n: ').lower() == 'y':
            Path(path).mkdir(parents=True, exist_ok=True)
            return Path(path)
        raise argparse.ArgumentTypeError(f'{path} is not a directory')
    return Path(path)


