project('Bare metal Hi', ['c','as'])
add_global_arguments('-std=c11', language : 'c')
add_global_arguments('-std=c11', language : 'as')

pkgconfig_gen(
  version : '0.1',
  name : 'baremetal_hi',
  filebase : 'baremetal-hi',
  description : 'Write "Hi" to a Uart port')

testexe = exectuable(
  'testbin',
  'test.c', 'startup.s')
