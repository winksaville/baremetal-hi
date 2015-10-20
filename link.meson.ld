
ENTRY(_Reset)
SECTIONS
{
  . = 0x10000;
  /* TODO: fix meson naming scheme so there its something other
   * than testit@exe as the linker script doesn't like '@' */
  .startup  . : { testit?exe/startup.S.o(.text) }
  .text : { *(.text) }
  .data : { *(.data) }
  .bss : { *(.bss COMMON) }
  . = ALIGN(8);
  . = . + 0x1000; /* 4kB stack */
  stack_top = .;
}
