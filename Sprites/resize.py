from PIL import Image
import os

list_of_files = []


def resizeImage(size):
    for root, dirs, files in os.walk("images/normal/"):
        for file in files:
            list_of_files.append(os.path.join(root, file))

    for image in list_of_files:
        str_img = str(image).split("/")[0] + "/" + str(size) + "px/" + str(image).split("/")[2]
        img = Image.open(image)
        img = img.resize((size, size), Image.ANTIALIAS)
        img.save(str_img)
