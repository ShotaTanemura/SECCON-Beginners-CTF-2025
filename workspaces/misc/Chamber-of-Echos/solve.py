import threading
import time
import subprocess
from scapy.all import IP, ICMP, Raw, send, sniff
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

TARGET = '133.242.228.146'
KEY_HEX = b'546869734973415365637265744b6579'
cipher = AES.new(bytes.fromhex(KEY_HEX.decode()), AES.MODE_ECB)

blocks = {}
needed = None
finished = False
ping_process = None

def got_reply(pkt):
    if ICMP in pkt and pkt[ICMP].type == 0 and Raw in pkt:
        ct = bytes(pkt[Raw].load)
        try:
            pt = unpad(cipher.decrypt(ct), 16)
            idx = int(pt.split(b'|', 1)[0])
            frag = pt.split(b'|', 1)[1]
            blocks[idx] = frag
            print(f'Got block {idx}: {frag}')

            global needed, finished, ping_process
            if needed is None and len(frag) < 14:
                needed = idx + 1

            if needed and len(blocks) == needed:
                flag = b''.join(blocks[i] for i in sorted(blocks))
                print('\nFLAG:', flag.decode())
                finished = True
                if ping_process and ping_process.poll() is None:
                    ping_process.terminate()
                    print('[*] Ping process terminated.')
        except ValueError:
            pass

def stopper(pkt):
    return finished

def start_ping():
    global ping_process
    ping_process = subprocess.Popen(['ping', '-i', '0.2', TARGET])
    ping_process.wait()

threading.Thread(target=start_ping, daemon=True).start()

print('[*] Sniffing … press Ctrl-C once the flag prints.')
sniff(filter=f'icmp and src host {TARGET}', prn=got_reply, stop_filter=stopper)
