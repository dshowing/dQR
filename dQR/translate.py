# -*- coding: utf-8 -*-
#Auther: dshowing
#Email: watt109629@outlook.com

import qrcode
from PIL import Image

class QR(object):
    def __init__(self, text):
        self.STEP = 10
        self.str = text

    def str2qr(self):
        """
        :param str: 字符串
        :return: 二维码
        """
        size = self.STEP
        str = self.str
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=size,
            border=0,
        )
        qr.add_data(str)
        qr.make(fit=True)

        img = qr.make_image()
        return img

    def img2ascii(self):
        """
        :param image: 图像
        :return: ASCII
        """
        image = self.str2qr()
        max_lenth = self.STEP
        string = ''
        Im1 = Image.open(image)
        Im2 = Im1.convert('L')
        width, height = Im2.size

        pix = Im2.load()

        for w in range(0, width+2, max_lenth):
            if w == 0:
                for i in range(0, width+2):
                    string += '██'
            elif w == width+2:
                for i in range(0, width+2):
                    string += '██'
            string += '██'
            for h in range(0, height+2, max_lenth):
                p = pix[w, h]
                p = '██' if p > 0 else '  '
                string += p
            string += '██'
            string += '\n'
        return string
