# -*- coding: utf-8 -*-
#Auther: dshowing
#Email: watt109629@outlook.com

from setuptools import setup

__author__ = 'dshowing'
__time__ = '2018/10/16'

setup(
    name='dQR',
    version='1.0',
    url='https://github.com/RitterHou/Lilith',
    author='dshowing',
    author_email='watt109629@outlook.com',
    description='Translate string in QRcode on terminal.',
    license='GPL3',
    packages=['dQR'],
    entry_points={
        'console_scripts': [
            'dQR=dQR.main:show'
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'qrcode==5.3',
        'Pillow==4.2.1'
    ],
)
