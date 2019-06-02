#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostInterprocessConan(base.BoostBaseConan):
    name = "boost_interprocess"
    version = "1.70.0"

    def package_info(self):
        super(BoostInterprocessConan, self).package_info()
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("rt")
