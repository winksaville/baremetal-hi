  .global _Reset
_Reset:
  // Initialize the statck which is defined in link.xxx.d script
  ldr sp, =stack_top

  // Call main
  bl  main

#ifdef RESET_ON_MAIN_COMPLETE
  // If qemu is executed with -no-reboot option then
  // resetting the board will cause qemu to exit
  // and it won't be necessary to ctrl-a, x to exit.
  // See http://lists.nongnu.org/archive/html/qemu-discuss/2015-10/msg00057.html

  // For arm926ej-s you unlock the reset register
  // then reset the board, I'm resetting to level 6

  // Unlock the reset register
  ldr r1, =0xA05F
  ldr r2, =0x10000020
  str r1, [r2] 

  // Reset the board to level 6
  ldr r1, =0x106
  ldr r2, =0x10000040
  str r1, [r2]
#endif

  // Loop endlessly if we get here
  b .
