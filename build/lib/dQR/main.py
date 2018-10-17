# -*- coding: utf-8 -*-
#Auther: dshowing
#Email: watt109629@outlook.com

import sys

from dQR import dqrcode


def show():
    args = sys.argv

    if len(args) == 1:
        print('Usage: dQR [Your string]')
    elif len(args) == 2:
        if args[1] == '-h' or args[1] == '--help':
            print('Usage: dQR [Your string]')
        else:
            #text = args[1]
            qr = dqrcode.QR(args[1])
            print(qr.showqr())
