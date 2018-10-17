# -*- coding: utf-8 -*-
#Auther: dshowing
#Email: watt109629@outlook.com

import qrcode
#from PIL import Image

class QR(object):
    def __init__(self, text):
        self.STEP = 10
        self.str = text

    def showqr(self):
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
        return self.img2ascii(img)

    def img2ascii(self, image):
        """
        :param image: 图像
        :return: ASCII
        """
        max_lenth = self.STEP
        string = ''
        Im1 = image.convert('L')
        width, height = Im1.size
        pix = Im1.load()

        for i in range(0, width+max_lenth*2):
            if i % max_lenth == 0:
                string += '██'
        string += '\n'
        for w in range(0, width, max_lenth):
            string += '██'
            for h in range(0, height, max_lenth):
                p = pix[w, h]
                p = '██' if p > 0 else '  '
                string += p
            string += '██'
            string += '\n'
        for i in range(0, width+max_lenth*2):
            if i % max_lenth == 0:
                string += '██'
        return string
