import select
import os


while True:
    fd = os.open('/tmp/listenfifo', os.O_RDWR)
    while True:
        _, w, _ = select.select([], [fd], [])
        if fd in w:
            break
    os.write(fd, 'hello'.encode())
    os.close(fd)
