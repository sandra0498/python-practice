from stegano import lsb

image = "landscape.jpg"
new_image = "hidden_image.jpg"

msg = "This is a secret message"

lsb.hide(image, message=msg).save(new_image)

message = lsb.reveal(new_image)
print("Hidden message: {}".format(message))
