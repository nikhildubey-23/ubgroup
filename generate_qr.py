import qrcode

data = "https://www.google.com/maps/place/22%C2%B003'18.1%22N+82%C2%B011'24.7%22E/@22.055029,82.190202,17z/data=!4m4!3m3!8m2!3d22.0550289!4d82.1902017?hl=en&entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D"
img = qrcode.make(data)
img.save("static/img/location2_qr.png")
