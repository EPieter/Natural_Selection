from PIL import Image
import os


# IMAGES

def resizeImage(size, dir_name):
    list_of_files = []
    is_dir = os.path.isdir("Sprites/" + str(size) + "px/")
    if not is_dir:
        os.mkdir("Sprites/" + str(size) + "px/")

    for root, dirs, files in os.walk("Sprites/normal/"):
        for file in files:
            list_of_files.append(os.path.join(root, file))

    for image in list_of_files:
        if dir_name:
            str_img = str(image).split("/")[0] + "/" + str(size) + "/" + str(image).split("/")[2]
        else:
            str_img = str(image).split("/")[0] + "/" + str(size) + "px/" + str(image).split("/")[2]
        img = Image.open(image)
        if dir_name:
            img = img.resize(int((size + "2").split("px")[0]), int((size + "2").split("px")[0]), Image.ANTIALIAS)
        else:
            img = img.resize((int(size), int(size)), Image.ANTIALIAS)
        img.save(str_img)


def resizeImageOnlyOne(size, dir_name=False):
    resizeImage(size, dir_name)


def resizeImageArray(list_sizes, dir_name=False):
    for size in list_sizes:
        resizeImage(size, dir_name)


def controlImages():
    pass


def regenerateAllImages():
    resizeImageArray(listOfImagesDirs(), dir_name=True)


def listOfImagesDirs():
    list_dirs = []
    for root, dirs, files in os.walk("Sprites/"):
        for file in dirs:
            list_dirs.append(file) if file != "normal" else None
    return list_dirs


def cropImage(filename):
    img = Image.open("custom/" + filename)
    width = img.width
    height = img.height
    diff = width - height
    print(diff)
    if diff != 0:
        if diff > 0:
            left = diff / 2
            right = left + height
            top = 0
            bottom = height
        else:
            left = 0
            right = width
            top = abs(diff / 2)
            bottom = top + width
    else:
        left = 0
        right = width
        top = 0
        bottom = height

    new_img = img.crop((left, top, right, bottom))
    new_img.save("Sprites/normal/" + filename)
    resizeImageArray([36, 72])
