ENTRY(_Reset)
SECTIONS
{
  . = 0x10000;
  .startup  . : { ${STARTUP_OBJ}$(.text) }
  .text : { *(.text) }
  .data : { *(.data) }
  .bss : { *(.bss COMMON) }
  . = ALIGN(8);
  . = . + 0x1000; /* 4kB stack */
  stack_top = .;
}
