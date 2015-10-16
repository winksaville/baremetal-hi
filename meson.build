project('Bare metal Hi', ['c'])

pkgconfig_gen(
  version : '0.1',
  name : 'baremetal_hi',
  filebase : 'baremetal-hi',
  description : 'Write "Hi"')

# Initialize some globals
srcs = []
compiler_args = []
compilerArgs = ['-std=c11', '-O2']
linkArgs = []

# Get Platform and initialize appropriate variables
Platform = get_option('Platform')

if Platform == 'Posix'
  compilerArgs += ['-DPosix']
  srcs = ['test.c']
endif

if Platform == 'Qemu_ARM_VersatilePB'
  compilerArgs += ['-DQemu_ARM_VersatilePB', '-mcpu=arm926ej-s']
  linkArgs = ['-T', '../link.meson.ld']
  srcs = ['test.c', 'startup.S']
endif

# Create the executable
testit = executable( 'testit', srcs, c_args : compilerArgs, link_args : linkArgs)

if Platform == 'Qemu_ARM_VersatilePB'
  custom_target( 'testbin',
    output : ['test.bin'],
    command : ['arm-eabi-objcopy', '-O', 'binary', 'testit', 'test.bin'],
    depends : [testit])

  if false
    # run doesn't work, it hangs
    custom_target( 'run',
      output : ['xyz'],
      command : ['qemu-system-arm', '-M', 'versatilepb', '-m', '128M', '-nographic', '-kernel', 'test.bin'])
  endif
endif
