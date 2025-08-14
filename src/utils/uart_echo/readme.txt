An echo virtual COM link to simulate UART;

socat -d -d pty,raw,echo=0 pty,raw,echo=0

socat[12898] N PTY is /dev/pts/2
socat[12898] N PTY is /dev/pts/3
