import vobject
import qrcode

vcard = vobject.vCard()
# Set the version of the vCard
    
vcard.add("version").value = "4.0"
vcard.add("fn").value = "Vishnu Prasad"  # Full name
vcard.add("tel").value = "+41 78 34 01 112"  # Telephone number
vcard.add("email").value = "vishnuprasad@smail.iitm.ac.in" # Email address
vcard.add("role").value = "Systems and Automation Engineer"  # Role or job title
vcard.add("ADDRESS").value = "Hofwiesen Strasse 4, Zurich, Switzerland"  # Address




serilized_vcard = vcard.serialize()
print(serilized_vcard)

# qr= qrcode.QRCode()
# qr.add_data(serilized_vcard)
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="blue")
# img.save("vishnu_qr.png")