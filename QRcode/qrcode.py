import pyqrcode
# from pyqrcode import QRcode

s = "https://www.youtube.com/watch?v=Q3JMD4oaXlI"

url = pyqrcode.create(s)

url.svg("shaabashyiaan.svg", scale=8)