#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostInterprocessConan(base.BoostBaseConan):
    name = "boost_interprocess"
    url = "https://github.com/bincrafters/conan-boost_interprocess"
    lib_short_names = ["interprocess"]
    header_only_libs = ["interprocess"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_container",
        "boost_core",
        "boost_date_time",
        "boost_integer",
        "boost_intrusive",
        "boost_move",
        "boost_static_assert",
        "boost_type_traits",
        "boost_unordered",
        "boost_winapi"
    ]

    def package_info_additional(self):
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("rt")    
            
    def package_id_additional(self):
        self.info.header_only()
        self.info.settings.os = str(self.settings.os)
