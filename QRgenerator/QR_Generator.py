import pyqrcode


link = input("Enter the URL: ")
filename = input("Enter the filename for the QR code (without extension): ")

url = pyqrcode.create(link)

url.png(f"{filename}.svg", scale=6)

url.png(f"{filename}.png", scale=6)