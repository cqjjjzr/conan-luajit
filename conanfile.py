from conans import ConanFile, CMake, tools

class LuajitConan(ConanFile):
    name = "luajit"
    version = "2.0.5"
    license = "MIT"
    url = "https://github.com/int010h/conan-luajit"
    description = "LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language."
    settings = "os", "compiler", "build_type", "arch"
    # TODO: build options
    # options = {"shared": [True, False]}
    # default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/int010h/LuaJIT.git luajit")
        self.run("cd luajit && git checkout v2.0.5")
        tools.replace_in_file("luajit/CMakeLists.txt", "project ( luajit C ASM)", '''project ( luajit C ASM)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        self.run('cmake %s/luajit %s' % (self.source_folder, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="luajit/src")
        self.copy("*.h", dst="include", src="", excludes="luajit/*")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lua"]
