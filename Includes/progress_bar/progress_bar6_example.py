#!/usr/bin/env python3

from progress_bar6 import ProgressBar
import time


def main():
    lines = [
        'Reading install',
        '.', '.', '.', '.',
        '\n',
        'Unpacking',
        '.', '.', '.', '.',
        '\n',
        'Loading compressed files',
        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
        '\n',
        'Decompressing',
        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
        '\n'
        'Installing',
        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
        '\n'
        'Configuring',
        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
        '\n'
        'Completing',
        '.', '.', '.',
        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
    ]

    progress_length = len(lines)

    # Initialise with settings
    app = ProgressBar(title='Loading', set_max=progress_length, foreground=(0.5, 0.0, 0.0))

    # Or set after
    app.set_title('Progressing...')
    app.set_max(progress_length)
    app.set_colour('#00aa00', (255, 255, 255))
    app.set_determinante(True)

    for progress_count in range(progress_length):
        time.sleep(.05)  # Do real work here
        if app.is_active():
            # Increment by 1
            app.set_increment(1)
            app.set_label('Loading... {0}'.format(progress_count))

        # Display messages
        app.add_output(lines[progress_count])

    app.add_output('Complete!', reset=True)
    time.sleep(1.0)


if __name__ == '__main__':
    main()
