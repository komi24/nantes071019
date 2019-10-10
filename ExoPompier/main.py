# -*- coding: utf-8 -*-

from Package.Board import Board
from time import sleep


b = Board()

for i in range(20):
    b.run()
    sleep(1)
