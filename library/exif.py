from wand.image import Image
def Edate(scan_filename):
	with Image(filename=scan_filename) as image:
            Edate=dict(image.metadata.items())['exif:DateTime']
	return Edate
