#!-*- coding: utf-8 -*-
"""
:author: Stefan Lehmann <stefan.st.lehmann@gmail.com>

"""
import sys
import ctypes

def platform_is_linux():
    return sys.platform.startswith('linux') or \
           sys.platform.startswith('darwin')


def platform_is_windows():
    return sys.platform == 'win32'

def extended_functions_supported():
    _adsDLL = ctypes.windll.TcAdsDll
    return hasattr(_adsDLL, 'AdsPortOpenEx')
