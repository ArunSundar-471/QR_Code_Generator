import pyqrcode
url='https://www.linkedin.com/in/arun-sundar-k-a055b5208/'
k=pyqrcode.create(url)
k.svg('Qr.svg',scale=10)


