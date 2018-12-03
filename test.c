int main(){
  __asm__(
    ".global start, _start\n"
    "start:\n"
    "_start:\n"
"    set 0x10e0, %g1		! init IU\n"
"    set 0x41, %g5\n"
"    set 0x80000100, %g6\n"
"    st %g5, [ %g6 ]\n");
  return 0;
}
