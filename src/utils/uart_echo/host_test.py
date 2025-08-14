# host_test.py
import sys, os, time, serial

PORT = sys.argv[1] if len(sys.argv) > 1 else "/dev/pts/3"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=0.25)
print(f"[host] open {PORT} @ {BAUD}")

# Send a few patterns
tests = [
    b"hello, uart!\n",
    bytes([0x00, 0xFF, 0x55, 0xAA]),
    os.urandom(1024),
]

for i, payload in enumerate(tests, 1):
    sent = ser.write(payload)
    ser.flush()
    # Collect the echo
    got = bytearray()
    deadline = time.time() + 2.0
    while len(got) < sent and time.time() < deadline:
        chunk = ser.read(4096)
        if chunk:
            got.extend(chunk)
    ok = (got == payload)
    print(f"[host] test {i}: sent={sent} got={len(got)} match={ok}")

ser.close()
