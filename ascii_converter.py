from PIL import Image
import sys

def convert_to_ascii(image_file_path, returnname, type_of_img):
    img = Image.open(image_file_path)

    width, height = img.size

    if width > 500:
        img = resize(img, type_of_img)

    width, height = img.size

    picture = img.load()

    grid = []
    for i in range(height):
        grid.append(["X"] * width)

    for y in range(height):
        for x in range(width):
            value = sum(picture[x,y])
            if(value == 0):
                grid[y][x] = "@"
            elif value in range(1,100):
                grid[y][x] = "%"
            elif value in range(100,200):
                grid[y][x] = "#"
            elif value in range(200,300):
                grid[y][x] = "*"
            elif value in range(300,400):
                grid[y][x] = "+"
            elif value in range(400,500):
                grid[y][x] = "="
            elif value in range(500,600):
                grid[y][x] = "-"
            elif value in range(600,700):
                grid[y][x] = ":"
            elif value in range(700,750):
                grid[y][x] = "."
            else:
                grid[y][x] = " "

    output = open(returnname + ".txt", "w")

    for row in grid:
        output.write("".join(row)+"\n")

    output.close()

def resize(image, type_of_img):
    w, h = image.size

    while(w > 500):
        image.resize((w//2, h//2)).save("resized.%s" % type_of_img)
        image = Image.open("resized.%s" % type_of_img)
        w, h = image.size # get new width and height

    return image

file = sys.argv[1]
returnname, type_of_img = file.split(".")

convert_to_ascii(file, returnname, type_of_img)
