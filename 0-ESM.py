import sys
import os
import os.path
import pypdfium2 as pdfium
import glob
from PIL import Image
import math
import cv2

'''
Here, we are defining the heights of the images or which is larger for merging.
We will be pasting two images onto one, and taking maximum dimensions of width 
and height for setting up the images according to how they are scanned.
'''

def maximum(height1, height2):

    if height1 >= height2:
        return height1
    else:
        return height2

if len (sys.argv) <= 2 or len (sys.argv) > 6:

    sys.exit ('\nUsage - '+sys.argv[0]+' [/E] [/S] [/R] [/M] "PDF-File"')

print (sys.argv)

Ext = Scan = Rnm = Mrg  = 0
msg = ''
   
for arg in sys.argv:

    '''
    (/E) switch is for extracting the images from the PDF
    (/S) switch is for scanning the images from the (Images) folder
    (/R) switch is for renaming the images, in case of deletion caused from defective/duplicate images
    (/M) switch is for merging two images into one
    '''
    
    if arg == '/E' or arg == '/e':
        Ext = 1
    elif arg == '/S' or arg == '/s':
        Scan = 1
    elif arg == '/M' or arg == '/m':
        Mrg = 1
    elif arg == '/R' or arg == '/r':
        Rnm = 1
    elif '.py' in arg:
        continue 
    elif '.pdf' in arg:
        filename = arg

    else:
        print ('\n'+arg)
        sys.exit ('\nUsage - '+sys.argv[0]+' [/E] [/S] [/R] [/M] "PDF-File"')

if not os.path.exists(filename):
    sys.exit('\nFile not found')

print('\nProcessing File -', filename)

filefolder, extension = os.path.splitext(filename)

# print (filefolder)

'''
A folder with the name of the PDF File will be created in the directory of the py code.
In this folder, three more folders will be created, namely (Images, Output, Merge)
Images folder will contain the images from the PDF file. These images will then be scanned
and kept in the Output folder. If merging is needed, every two images from the Output folder
 will then be merged into a single image
 '''

if not os.path.exists(filefolder):
    os.makedirs(filefolder)

if not os.path.exists(filefolder+'\Images'):
    os.makedirs(filefolder+'\Images')

if not os.path.exists(filefolder+'\Merge'):
    os.makedirs(filefolder+'\Merge')

if not os.path.exists(filefolder+'\Output'):
    os.makedirs(filefolder+'\Output')

if Ext:

    # For extracting the images from the PDF File

    msg = 'Extraction '
    print ('\nExtracting Starts')
    
    pdf = pdfium.PdfDocument (filename)

    n_pages = len(pdf)
    
    for page_number in range(n_pages):
                
        print ('Processing - '+str(page_number+1), end='\r')

        page = pdf.get_page(page_number)

        pil_image = page.render_topil(
            scale=1,
            rotation=0,
            # crop=(70, 0, 70, 0),  # L, B, R, T
            crop=(0, 0, 0, 0),
            greyscale=False,
            optimise_mode=pdfium.OptimiseMode.NONE,
        )

        imgfilename = (filefolder+f'\Images\{page_number + 1}.jpg')

        pil_image.save (imgfilename)

    print('\nExtract Completed')

if Scan:

    # For scanning the images from the (Images) folder
    
    msg = msg+'Scanning '
    print ('\nScanning Starts')

    '''
    A scanning code is kept separate as it is used as a tool. Store it in the same file
    folder which contains the PDF files and this ESM code
    '''
    
    os.system ('python 2-Scan.py --images '+filefolder+'/Images')

    print  ('\nScan Completed')

if Rnm:

    # For renaming the images, in case of deletion caused from defective/duplicate images
    
    msg = msg+'Renaming '
    print ('\nRenaming Starts')

    FilePath = filefolder+'/Output/'
    
    files = len((glob.glob(FilePath+"*.jpg")))
    oldFileNum = 1

    for newFileNum in range(1, files+1):
        
        newFileName = FilePath+str(newFileNum)+".jpg"
        
        # print ('Processing - '+str(newFileNum)+'.jpg', end='\r')

        while True:
            oldFileName = FilePath+str(oldFileNum)+".jpg"

            if os.path.isfile(oldFileName):
                if (oldFileName != newFileName):
                    # print(oldFileName, newFileName)
                    os.rename(oldFileName, newFileName) 
                    
                oldFileNum += 1
                break

            else:

                oldFileNum += 1

    print ('\nRenaming Completed')    
    
if Mrg:
    
    '''
    For merging the images to view two pages in a single view, as this code
    is written for that use where both pages have continuous information
    in a single line with table format
    '''

    msg = msg+'Merging '
    print ('\nMerge Starts')
    
    lst = os.listdir(filefolder+'/Output') 
    n_pages = len(lst) 

    for page_number in range (1, n_pages, 2):

        FileL = (f"{page_number + 1}.jpg")
        FileR = (f"{page_number}.jpg")
        
        im1 = Image.open (filefolder+f'/Output/{FileL}')
        im2 = Image.open (filefolder+f'/Output/{FileR}')

        width1, height1  = im1.size
        width2, height2  = im2.size
        
        # print (height1,width1,height2,width2)        
        
        im = Image.new("RGB", (width1+width2, maximum(height1, height2)), "white")

        im.paste (im1, (0, 0))
        im.paste (im2, (width1,0))

        out_file_num = math.floor((page_number + 1) / 2)

        if (out_file_num<=9):
            filename = (filefolder+f'-00{out_file_num}.jpg')
        elif (out_file_num>9 and out_file_num<=99):
            filename = (filefolder+f'-0{out_file_num}.jpg')
        else:
            filename = (filefolder+f'-{out_file_num}.jpg')

        im.save (filefolder+f'/Merge/{filename}')
    
    print ('Merging Completed')

print ('\n'+msg+'Done.')

sys.exit()



