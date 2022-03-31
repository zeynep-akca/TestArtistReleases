import inspect
import logging
from jproperties import Properties
import os
import sys
import pandas as pd


class BaseClass:
    def getProperties(self):
        Root_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(Root_Dir)
        properties_folder = os.path.join(Root_Dir, "config")
        properties_path = os.path.join(properties_folder, "config.properties")
        p = Properties()
        with open(properties_path, 'rb') as property_file:
            p.load(property_file, "utf-8")
        return p

