import qrcode

# Input text or URL
data = "https://busta.games"

qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")