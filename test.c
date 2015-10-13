typedef unsigned char uint8_t;
typedef unsigned int uint32_t;

#define Qemu_ARM_VersatilPB
#ifdef Qemu_ARM_VersatilPB
volatile uint32_t* const pUart = (uint32_t*)0x101f1000;
#endif

void putchar_dbg(uint8_t ch) {
  *pUart = (uint32_t)ch;
}

int main(void) {
  putchar_dbg('H');
  putchar_dbg('i');
  putchar_dbg('\n');

  return 0;
}
