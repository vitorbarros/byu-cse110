from PIL import Image


def is_green(r, g, b):
    return 0 <= r <= 76 and 76 <= g <= 244 and b <= 175


# opening beach image
image_beach = Image.open('images/beach.jpg')

# opening cactus image
image_cactus = Image.open('images/cactus.jpg')
(cactus_w, cactus_h) = image_cactus.size

combined_image = Image.new('RGB', image_beach.size)
pixel_combined_image = combined_image.load()

# loading images
pixel_beach = image_beach.load()
pixel_cactus = image_cactus.load()

cactus_x_range = range(0, cactus_w)
cactus_y_range = range(0, cactus_h)

# loops
for cx in cactus_x_range:
    for cy in cactus_y_range:
        (cr, cg, cb) = pixel_cactus[cx, cy]
        if not is_green(cr, cg, cb):
            pixel_combined_image[cx, cy] = (cr, cg, cb)
        else:
            pixel_combined_image[cx, cy] = pixel_beach[cx, cy]

combined_image.save('images/new_image.jpg')