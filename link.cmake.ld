ENTRY(_Reset)
SECTIONS
{
  . = 0x10000;
  /*
   * TODO: Figure out how to not have this absolute. Just making it
   * "CmakeFiles/TestExe.dir/startup.S.obj" causes an error that
   * "_Result" is multiply defined! It seems to be related to
   * the line in rules.ninja where arm-eabi-ld has full paths for
   * startup.S.obj and thus this has to be the full path. If I change
   * both ruild.ninja and this line to CmakeFiles/TestExe.dir/startup.S.obj
   * then it works.
   */
   .startup  . : { /home/wink/prgs/libs/baremetal-hi/build-cmake/CMakeFiles/TestExe.dir/startup.S.obj(.text) }
  .text : { *(.text) }
  .data : { *(.data) }
  .bss : { *(.bss COMMON) }
  . = ALIGN(8);
  . = . + 0x1000; /* 4kB stack */
  stack_top = .;
}
