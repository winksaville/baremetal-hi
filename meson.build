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
linkDeps = []

# Get Platform and initialize appropriate variables
Platform = get_option('Platform')

if Platform == 'Posix'
  compilerArgs += ['-DPosix']
  srcs = ['test.c']
endif

if Platform == 'Qemu_ARM_VersatilePB'
  compilerArgs += ['-DQemu_ARM_VersatilePB', '-mcpu=arm926ej-s']
  linkfile = 'link.meson.ld'
  linkArgs = ['-Wl,-T,@0@/@1@'.format(meson.current_source_dir(), linkfile)]
  linkDeps = [linkfile]
  srcs = ['test.c', 'startup.S']
endif

# Create the executable
testit = executable( 'testit', srcs, c_args : compilerArgs, link_args : linkArgs, link_depends : linkDeps)

if Platform == 'Qemu_ARM_VersatilePB'
  testbin = custom_target( 'testbin',
    output : ['test.bin'],
    command : ['arm-eabi-objcopy', '-O', 'binary', 'testit', 'test.bin'],
    depends : [testit])

  run_target('run', 'qemu-system-arm', '-M', 'versatilepb', '-m', '128M', '-nographic', '-kernel', testbin)
else
  run_target('run', testit)
endif
