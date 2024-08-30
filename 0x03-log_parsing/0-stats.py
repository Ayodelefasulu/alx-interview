#!/usr/bin/python3
"""
This script parses logs and analyses them
"""
import sys
import signal

# Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Function to print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C) to print statistics before exiting.
    """
    print_statistics()
    sys.exit(0)


# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split()
    if len(parts) < 7:
        continue

    try:
        # Extract file size and status code
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update total file size
        total_file_size += file_size

        # Update status code count if valid
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

    except (ValueError, IndexError):
        # Skip lines with incorrect format
        continue

# If EOF reached, print the final statistics
print_statistics()
