# This is a sample Python script.
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

im = Image.open("_images/20210820_152718.jpg")
font_path = "_utils/ALBATRO2.TTF"


def copyright(image, texte, opacity=1.0, rotation=30):
    # Use a breakpoint in the code line below to debug your script.
    image = image.convert("RGBA")  # Press Ctrl+F8 to toggle the breakpoint.
    texte_image = Image.new("RGBA", image.size, (255, 255, 255, 0))

    fontsize = 1
    font = ImageFont.truetype(font_path, fontsize)
    texte_image.show()
    while font.getsize(texte) [0] < image.size [0]:
        fontsize += 1
        font = ImageFont.truetype(font_path, fontsize)

    text_height = font.getsize(texte) [1]
    pos = (0, (image.size [1] / 2) - (text_height / 2))

    d = ImageDraw.Draw(texte_image)
    d.text(pos, texte, fill=(255, 255, 255, round(opacity * 255)), font=font)

    texte_image = texte_image.rotate(rotation)

    return Image.alpha_composite(image, texte_image)


# Press the green button in the gutter to run the script.

im_copyright = copyright(im, "Alphonse", opacity=0.2, rotation=20)
im_copyright.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
