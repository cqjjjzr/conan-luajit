from conans import ConanFile, CMake
import os

class LuajitTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        assert os.path.isfile(os.path.join(self.deps_cpp_info["luajit"].rootpath, "licenses", "COPYRIGHT"))
        bin_path = os.path.join("bin", "example")
        self.run(bin_path, run_environment=True)
