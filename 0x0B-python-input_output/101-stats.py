#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for item in sorted(status_codes):
        print("{}: {}".format(item, status_codes[item]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    counter = 0

    try:
        for line_idx in sys.stdin:
            if counter == 10:
                print_stats(size, status_codes)
                counter = 1
            else:
                counter += 1

            line_idx = line_idx.split()

            try:
                size += int(line_idx[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line_idx[-2] in valid_codes:
                    if status_codes.get(line_idx[-2], -1) == -1:
                        status_codes[line_idx[-2]] = 1
                    else:
                        status_codes[line_idx[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
