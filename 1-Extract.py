import pypdfium2 as pdfium
import sys, os.path

if len (sys.argv) != 2:
    sys.exit ('\nUsage - '+sys.argv[0]+' "PDF-File"')

if not os.path.exists(sys.argv[1]):
    sys.exit('\nFile Not Found - '+sys.argv[1]+'\nMaybe wrong file name?')

pdf = pdfium.PdfDocument (sys.argv[1])

n_pages = len(pdf)

for page_number in range(n_pages):

    page = pdf.get_page(page_number)

    pil_image = page.render_topil(
        scale=1,
        rotation=0,
        # crop=(70, 0, 70, 0),  # L, B, R, T
        crop=(0, 0, 0, 0),
        greyscale=False,
        optimise_mode=pdfium.OptimiseMode.NONE,
    )

    fname = (f"Images\\{page_number + 1}.jpg")

    pil_image.save (fname)

sys.exit('Process Completed Successfully. :)')



