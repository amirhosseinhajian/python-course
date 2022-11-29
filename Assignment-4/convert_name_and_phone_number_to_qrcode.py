import qrcode
qr = qrcode.make(input("Plese enter your name: ") + '\n' + input("Plese enter your phone number: ")).save("QrCode.png")