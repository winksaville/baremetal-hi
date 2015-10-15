# From http://www.valvers.com/open-software/raspberry-pi/step03-bare-metal-programming-in-c-pt3/
cmake_minimum_required( VERSION 2.8 )

# Mark the language as C so that CMake doesn't try to test the C++
# cross-compiler's ability to compile a simple program because that will fail
project(baremetal-hi C ASM )

# Add our cflags
set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O2 -g -nostartfiles" )

# The directory where the objects are stored
set( OBJ_DIR "${CMAKE_BINARY_DIR}/CMakeFiles/TestExe.dir" )

# The link executable variable must be complete its and
# as far as I can tell this is the best way within CMake
# to be able to control the linker. Otherwise the code CMake
# generates doesn't work for bare metal applications.
set( CMAKE_C_LINK_EXECUTABLE "${CMAKE_LINKER} -nostdlib -T ${CMAKE_SOURCE_DIR}/link.cmake.ld -L ${CMAKE_BINARY_DIR} -l mycrt0 ${OBJ_DIR}/test.c.obj -o TestExe")

# Create TestExe application, it depends on library mycrt0
add_executable(TestExe test.c)
target_link_libraries(TestExe mycrt0)

# Create a library with startup.S.obj moving startup.S.obj into
# a library allows link.cmake.ld to not have to have a full path
# thus allowing the build directory to be anywhere.
add_library(mycrt0 startup.S)

# Create test.bin using objcopy
add_custom_command(
  TARGET TestExe POST_BUILD
  COMMAND ${CMAKE_OBJCOPY} ./TestExe${CMAKE_EXECUTABLE_SUFFIX} -O binary ./test.bin
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  COMMENT "Convert the ELF output file to a binary image")

# Run test.bin
add_custom_target(run
  COMMAND qemu-system-arm -M versatilepb -m 128M --nographic --kernel test.bin
  DEPENDS TestExe)
