#!/usr/bin/env python3
import sys

stdout = sys.stdout.buffer

for chunk in [
    b"This is test",
    b" text.\nThis is a",
    b" very, very, very",
    b" (well, not really)",
    b" long line.\r\nThis line ends in a CR.\r\xC2\xA1Weird!",
]:
    stdout.write(chunk)
    stdout.flush()
