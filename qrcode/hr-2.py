import pyqrcode
url='https://www.hackerrank.com/arunsundar471'
k=pyqrcode.create(url)
k.svg('Qr2.svg',scale=10)