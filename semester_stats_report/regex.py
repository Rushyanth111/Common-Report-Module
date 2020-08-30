import re

department_regex = re.compile("[A-Z]{2,3}")

usn_regex = re.compile("[0-9]{1}[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{3}")

subcode_regex = re.compile("[0-9]{2}[A-Z]{2,6}[0-9]{2,3}")

# https://docs.python.org/3/library/re.html#match-objects
# Match Objects have a boolean value of True.
