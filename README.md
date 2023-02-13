# Image-Editor

These codes have been used for extracting the images from a PDF file and then scanning it using OpenCV.
Every subsequent two pages are then merged for a collective single page view, making it half the pages.

--------------------------------------------------

Usage - [/E] [/S] [/R] [/M] "PDF-File"

Either one switch can be used, or two, or all switches can be used.

(/E) switch is for extracting the images from the PDF.
(/S) switch is for scanning the images from the (Images) folder.
(/R) switch is for renaming the images, in case of deletion caused from defective/duplicate images.
(/M) switch is for merging two images into one.

A folder with the name of the PDF File will be created in the directory of the py code.
In this folder, three more folders will be created, namely (Images, Output, Merge)
Images folder will contain the images from the PDF file. These images will then be scanned
and kept in the Output folder. If merging is needed, every two images from the Output folder
will then be merged into a single image.

A scanning code is kept separate as it is used as a tool. Store it in the same file
folder which contains the PDF files and this ESM code.

Merging is used for merging the images to view two pages in a single view, as this code is written 
for that use where both pages have continuous information in a single line with table format.


