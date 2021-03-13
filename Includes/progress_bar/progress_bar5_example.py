#!/usr/bin/env python3

from progress_bar5 import *
import time
from pathlib import Path


def main():
    base_path = Path.home().joinpath('Downloads/')
    files = [file for file in base_path.iterdir() if base_path.is_dir()]
    progress_length = len(files)

    app = ProgressBar(progress_length, title='Loading files', width=1000, bar_colour=(0, 128, 0), back_colour='#ccffcc')

    for file in files:
        app.set_label('Progressing...{}'.format(file.name))
        time.sleep(5 / len(files))  # do real work here
        if app.is_active():
            # Increment by 1
            app.increment(1)


if __name__ == '__main__':
    main()
