import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


# Add data to the QR code (in this case, a URL) 
data = "https://www.linkedin.com/in/jade-t-stanley/"
qr.add_data(data)

#Make the QR code
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

#Save or display the QR code image
img.save("jadetstanley.png")
img.show()

