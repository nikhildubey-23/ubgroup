import qrcode

data = "https://www.google.com/maps/search/?api=1&query=22.0550289,82.1902017"
img = qrcode.make(data)
img.save("static/img/location_qr.png")
