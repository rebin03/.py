import pyqrcode


link = input("Enter the URL: ")

url = pyqrcode.create(link)

url.png("myqr.svg", scale=6)

url.png("myqr.png", scale=6)