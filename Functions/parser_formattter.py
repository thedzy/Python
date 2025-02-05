# For use in arg parsing to extend the width of help
#     parser = argparse.ArgumentParser(
#         description='%(prog)s',
#         formatter_class=parser_formatter(argparse.RawTextHelpFormatter, indent_increment=4, max_help_position=12,
#                                          width=160))



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