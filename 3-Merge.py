from PIL import Image
import math
import os


# im = Image.new("RGB", (3330, 2330), "white")

# im1 = Image.open ("D:/Umar/Python/Mannai/2.jpg")

# im2 = Image.open ("D:/Umar/Python/Mannai/1.jpg")

# im.paste (im1, (0, 0))
# im.paste (im2, (1664,0))

# im.show()

# im.save (r'D:\Umar\Python\Mannai\SJC2F723060-001.jpg')

lst = os.listdir('Output') # directory path
n_pages = len(lst)

for page_number in range (1, n_pages, 2):

    FileL = (f"{page_number + 1}.jpg")
    FileR = (f"{page_number}.jpg")

    # im = Image.new("RGB", (3330, 2330), "white")

    im = Image.new("RGB", (3730, 2900), "white")
    im1 = Image.open (f'Output\{FileL}')
    im2 = Image.open (f'Output\{FileR}')

    im.paste (im1, (0, 0))
    im.paste (im2, (1865,0))

    # im.paste (im2, (1664,0))

    # print (f"FileL-{page_number + 1}.jpg")
    # print (f"FileR-{page_number}.jpg")    

    # print (FileL)
    # print (FileR)

    # print (f"SJC-{(page_number + 1) / 2}.jpg")

    out_file_num = math.floor((page_number + 1) / 2)

    if (out_file_num<=9):
        fname = (f"SJC2F723060-00{out_file_num}.jpg")
    elif (out_file_num>9 and out_file_num<=99):
        fname = (f"SJC2F723060-0{out_file_num}.jpg")
    else:
        fname = (f"SJC2F723060-{out_file_num}.jpg")

    # im.save (r"D:\\Umar\\Python\\Mannai\\Final_Doc\\SJC2F723060-00{math.floor((page_number + 1) / 2)}.jpg")

    im.save (f"Final-Merge\\{fname}")


