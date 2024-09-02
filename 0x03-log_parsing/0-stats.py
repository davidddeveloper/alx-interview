#!/usr/bin/python3
"""
    0-stats.py: print out statistics read from stdin
"""
import sys
import signal
import re


class Log:
    """
        Represent a log of network statistic

    """

    # matches string in this format: ip - [strf datetime] url status filesize
    __pattern = r"(^\d*\.\d*\.\d*\.\d*)\s-\s(\[\d{4}\-(\d{1}|\d{2})"
    __pattern += r"\-(\d{1}|\d{2})\s(\d{1}|\d{2})\:(\d{1}|\d{2})"
    __pattern += r"\:(\d{1}|\d{2})\.\d*\])\s((\"|\')[A-Z]*\s\/[a-zA-Z]"
    __pattern += r"*\/\d*\s[A-Z]*\/\d{1}\.\d{1}(\"|\'))\s(\d{3})\s([0-9]*)"
    __counter = 0

    def __init__(self):
        self.status_codes = {}
        self.file_size = 0

    def read_lines(self):
        """
            Read from stdin line by line
            extract the value of status codes and filesize
        """

        for line in sys.stdin:
            if self.__counter == 10:  # log stats after every 10 lines read
                self.log()
                self.__counter = 0

            self.extract(re.search(Log.__pattern, line))
            self.__counter += 1

            # log stats when ctrl+c signal receive and exit
            signal.signal(signal.SIGINT, self.sigint_handler)

    def extract(self, search):
        if search:
            search = search.groups()
            file_size = int(search[-1])  # convert to integer
            status_code = (search[-2])  # convert to int

            self.save(file_size, status_code)

    def save(self, file_size, status_code):
        """
            Do two thing:
                increment file_size in every line
                count status_code

        """
        try:
            if self.status_codes[status_code]:
                self.status_codes[status_code] += 1  # increment
        except KeyError:
            self.status_codes[status_code] = 1  # add it

        self.file_size += file_size

    def log(self):
        """
            print the statistic
        """
        print("File size:", self.file_size)

        keys = list(self.status_codes.keys())
        keys.sort()  # for printing in ascending order

        for key in keys:
            print(f"{key}: {self.status_codes[key]}")

    def sigint_handler(self, signal, frame):
        """
            log stats when ctrl+c signal receive
            and exit

        """
        self.log()

    def run(self):
        return self.read_lines()


log = Log()
log.run()
