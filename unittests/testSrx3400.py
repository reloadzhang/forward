#!/usr/bin/env python
# encodint:utf-8
# Author:Cheung Kei-Chuen
import unittest
import importlib
from forward.utils.forwardError import ForwardError
from forward.devclass.baseJuniper import BASEJUNIPER

class deviceClassSrx3400(unittest.TestCase):
    def setUp(self):
        self.deviceClassName = "srx3400"
        self.initParameters = ["ip",
                               "username",
                               "password",
                               "port",
                               "timeout",
                               "privilegePw",
                               "isLogin",
                               "isEnable",
                               "channel",
                               "shell",
                               "basePrompt",
                               "prompt",
                               "moreFlag"]
        self.baseClassMethod = ["login",
                                "logout",
                                "execute",
                                "getMore",
                                "getPrompt",
                                "cleanBuffer"]
        self.deviceClassMethod = ["_recv",
                                  "_commit",
                                  "addUser",
                                  "_configMode",
                                  "_exitConfigMode",
                                  "changePassword",
                                  "deleteUser"]

    def test_class_parameters(self):
        _dev = getattr(importlib.import_module('forward.devclass.{dev}'.format(dev=self.deviceClassName)),
                       self.deviceClassName.upper())
        for parameter in self.initParameters:
            if not hasattr(_dev(1,2,3), parameter):
                raise IOError('%s not have parameter:' % (self.deviceClassName), parameter)

    def test_base_class_method(self):
        _dev = getattr(importlib.import_module('forward.devclass.{dev}'.format(dev=self.deviceClassName)),
                       self.deviceClassName.upper())
        for method in self.baseClassMethod:
            if not hasattr(_dev(1,2,3), method):
                raise IOError('%s not have parameter:' % (self.deviceClassName), method)

    def test_inherit_check(self):
        # Inherit from BASETELNET
        cls = getattr(importlib.import_module('forward.devclass.{dev}'.format(dev=self.deviceClassName)),
                      self.deviceClassName.upper())
        self.assertEquals(cls.__bases__[0], BASEJUNIPER)

    def test_device_class_method(self):
        _dev = getattr(importlib.import_module('forward.devclass.{dev}'.format(dev=self.deviceClassName)),
                       self.deviceClassName.upper())
        for method in self.deviceClassMethod:
            if not hasattr(_dev(1,2,3), method):
                raise IOError('%s not have parameter:' % (self.deviceClassName), method)