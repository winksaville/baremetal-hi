# From http://www.valvers.com/open-software/raspberry-pi/step03-bare-metal-programming-in-c-pt3/
cmake_minimum_required( VERSION 2.8 )

# Mark the language as C so that CMake doesn't try to test the C++
# cross-compiler's ability to compile a simple program because that will fail
project(baremetal-hi C ASM )

# We had to adjust the CMAKE_C_FLAGS variable in the toolchain file to make sure
# the compiler would work with CMake's simple program compilation test. So unset
# it explicitly before re-setting it correctly for our system
set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O0" )
set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g" )
set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -nostartfiles" )

#set( CMAKE_EXE_LINKER_FLAGS "-T ${CMAKE_SOURCE_DIR}/link.ld" )

set( OBJ_DIR "${CMAKE_BINARY_DIR}/CMakeFiles/TestExe.dir" )

set( CMAKE_C_LINK_EXECUTABLE "${CMAKE_LINKER} -T ${CMAKE_SOURCE_DIR}/link.cmake.ld ${OBJ_DIR}/startup.S.obj ${OBJ_DIR}/test.c.obj -o TestExe")

add_executable(TestExe
  startup.S
  test.c)

add_custom_command(
  TARGET TestExe POST_BUILD
  COMMAND ${CMAKE_OBJCOPY} ./TestExe${CMAKE_EXECUTABLE_SUFFIX} -O binary ./test.bin
      WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
      COMMENT "Convert the ELF output file to a binary image" )

