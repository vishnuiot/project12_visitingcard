import vobject
import qrcode

vcard = vobject.vCard()
# Set the version of the vCard
    
vcard.add("version").value = "4.0"
vcard.add("fn").value = "John Doe"  # Full name
vcard.add("tel").value = "+1234567890"  # Telephone number
vcard.add("email").value = "john@gmail.com" # Email address



serilized_vcard = vcard.serialize()
print(serilized_vcard)

qr= qrcode.QRCode()
qr.add_data(serilized_vcard)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("vcard_qr.png")