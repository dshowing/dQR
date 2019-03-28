
# dQR

*Convert string to qrcode on your terminal.*


## Requirements

* python 2/3
* pip

## Installation

```
pip install dQR
```

## Usage

### Terminal
```
dQR  http://www.sina.com
```

### In python project
```
from dQR.dqrcode import QR
img = QR('http://www.sina.com')
print(img.showqr())
```
![qrcode](./dQR/show_png.png)
