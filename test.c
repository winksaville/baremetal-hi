typedef unsigned char uint8_t;
typedef unsigned int uint32_t;

//#define BmArm
//#define POSIX

#ifdef BmArm
// Assume a VersatilePB
volatile uint32_t* const pUart = (uint32_t*)0x101f1000;
#endif

#ifdef Posix
extern int putchar(int ch);
#endif

void putchar_dbg(uint8_t ch) {
#ifdef BmArm
  *pUart = (uint32_t)ch;
#endif
#ifdef Posix
  putchar(ch);
#endif
}

int main(void) {
  putchar_dbg('H');
  putchar_dbg('i');
  putchar_dbg('\n');

  return 0;
}
