from conans import ConanFile, tools, os

class BoostInterprocessConan(ConanFile):
    name = "Boost.Interprocess"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-interprocess"
    source_url = "https://github.com/boostorg/interprocess"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["interprocess"]
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Container/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Date_Time/1.64.0@bincrafters/testing", \
                      "Boost.Integer/1.64.0@bincrafters/testing", \
                      "Boost.Intrusive/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Unordered/1.64.0@bincrafters/testing", \
                      "Boost.Unordered/1.64.0@bincrafters/testing", \
                      "Boost.Winapi/1.64.0@bincrafters/testing"

                      #assert1 config0 container7 core2 date_time11 integer3 intrusive6 move3 static_assert1 type_traits3 unordered8 winapi1
                      
    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=50 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()