# echo_device.py
import sys, time, serial

PORT = sys.argv[1] if len(sys.argv) > 1 else "/dev/pts/2"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=0.01)
print(f"[echo_device] listening on {PORT} @ {BAUD}")

try:
    while True:
        data = ser.read(4096)
        if data:
            # Simulate your firmware echoing bytes back out
            ser.write(data)
        else:
            # idle a touch so we don't burn CPU
            time.sleep(0.001)
except KeyboardInterrupt:
    pass
finally:
    ser.close()
