# Baremetal Hi

[![Build Status](https://travis-ci.org/winksaville/baremetal-hi.svg)](https://travis-ci.org/winksaville/baremetal-hi)

A trivial baremetal test app that prints "Hi" to the Uart on the qemu Virtual
Development board for ARM. The resulting runnable output is "test.bin" and can
be tested by running with qemu-system-arm:
```
qemu-system-arm -M versatilepb -m 128M -nographic -kernel test.bin
```
I'm also exploring various build systems as I'm trying to decide which to use
as my preferred build system in the future. At the moment I feel using a
meta-build system which generates [Ninja](https://martine.github.io/ninja/) code
is the best approach, but we'll see how it goes.

Currently the set of build systems I'm interested in are:
* [GNU Make](https://www.gnu.org/software/make/) (working)
* [kati](https://github.com/google/kati) (working)
* [CMake](https://cmake.org) (working)
* [Meson](https://mesonbuild.com) (working)
* [Craftr](https://github.com/craftr-build/craftr) (working with fixed craftr)

There are some prerequisites:
* An arm-eabi cross compiler. (For now see [here](https://github.com/winksaville/sortie-dopsys-myos)
and change 'i586-elf' to 'arm-eabi'). TODO: Create a project to make it easier to create
cross-compilers and also add a gdb.
* Install [Ninja](https://martine.github.io/ninja/)
* Install which ever build system you're interested.

Also, don't hesitate to provide pull requests or fork this project to
do your own exploration.
___
## To use [GNU Make](https://www.gnu.org/software/make/):
```
mkdir build-makefile
cd build-makefile
make
```
To run using QEMU:
```
make run
```
___
## To use [kati](https://github.com/google/kati)
Kati is interesting in that it uses GNU Makefiles as its
input source and internally generates ninja code.
```
mkdir build-kati
cd build-kati
kati -f ../Makefile
kati -f ../Makefile run
```
To have kati generate build.ninja and use ninja:
```
kati --ninja -f ../Makefile
ninja
ninja run
```
___
## To use [CMake](https://cmake.org/), based on [this](http://www.valvers.com/open-software/raspberry-pi/step03-bare-metal-programming-in-c-pt3/):
```
mkdir build-cmake-ninja
cd build-cmake-ninja
cmake -G "Ninja" -DCMAKE_TOOLCHAIN_FILE=../toolchain-arm-eabi.cmake ..
ninja
ninja run
```
For unix Makefile you can use the run target which doesn't work for ninja
```
mkdir build-cmake-make
cd build-cmake-make
cmake -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=../toolchain-arm-eabi.cmake ..
make
make run
```
___
## To use [Meson](https://mesonbuild.com):
The build.meson file supports two platforms, Posix and BmArm.
The BmArm causes test.c to assume a Qemu VersatilePB platform.

To build and run Posix platform:
```
mkdir build-meson-posix
cd build-meson-posix
meson -D Platform=Posix ..
ninja
ninja run
```
To build and run for BmArm platform:
```
mkdir build-meson-bmarm
cd build-meson-bmarm
meson -D Platform=BmArm --cross-file ../arm-eabi-cross_file.txt --buildtype plain ..
ninja
ninja run
```
___
## To use [Craftr](https://github.com/craftr-build/craftr):
I've hacked craftr and [my version](https://github.com/winksaville/craftr/tree/add-prog-obj_copy-run_target)
must be used.
```
mkdir build-craftr
cd build-craftr
craftr -c .. export
ninja
```
