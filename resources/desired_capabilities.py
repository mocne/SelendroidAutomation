__author__ = 'andriy.tutunyk'

import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Nexus4',
        'app': PATH('../application/' + app),
        'newCommandTimeout': 17200
    }
    return desired_caps