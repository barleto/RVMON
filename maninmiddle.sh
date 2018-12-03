if [ -f r.txt ]; then
    rm -f r.txt
fi
if [ -f w.txt ]; then
    rm -f w.txt
fi
sudo socat $1,raw,echo=0 \
SYSTEM:'tee r.txt |socat - "PTY,link=/dev/ttyUSBV,raw,echo=0,waitslave" |tee w.txt' &
sleep 1
sudo chmod 666 /dev/ttyUSBV
chmod 666 r.txt
chmod 666 w.txt
wait
