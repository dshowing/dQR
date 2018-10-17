
# dQR

*Translate string to QRcode on your Terminal.*


## Requirements

* python3
* pip3

## Installation

```
pip install dQR
```

## Usage

### Terminal
`dQR [Your string]`

like this
```
dQR  http://www.sina.com
```

### In python project
```
from dQR.dqrcode import QR
img = QR('http://www.sina.com')
print(img.showqr())
```