from PIL import Image  # it says PIL but this is coming from the Pillow module

# Opening an image, getting info, and showing the image
im = Image.open('./screenshot.png')
print(im.format, im.size, im.mode)
im.show()

# Converting images to jpeg
if not im.mode == 'RGB':
    im = im.convert('RGB')  # the original image's mode was RGBA (A for transparency), but im.save does not support
    # saving RGBA as JPEG, so first convert it to plain RGB
im.save('./screenshot.jpg', 'JPEG')

im2 = Image.open('./screenshot.jpg')
print(im2.format, im2.size, im2.mode)
im2.show()  # note that the jpg was created and im2 shows up as jpeg, but im2.show()'s file shows a tempxx.png