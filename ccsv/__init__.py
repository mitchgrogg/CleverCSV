# -*- coding: utf-8 -*-

__version__ = '0.1.1'

from csv import QUOTE_ALL, QUOTE_MINIMAL, QUOTE_NONNUMERIC, QUOTE_NONE

from .detect import Detector
from .detect import Detector as Sniffer
from .dict_read_write import DictReader, DictWriter
from .exceptions import Error
from .parser import field_size_limit
from .read import reader
from .wrappers import csv2df, read_as_dicts
from .write import writer