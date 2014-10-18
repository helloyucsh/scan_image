from wand.image import Image
def exif(scan_filename):
	with Image(filename=scan_filename) as image:
            exif=dict(image.metadata.items())['exif:DateTime']
	return exif
print exif('./image/1FA/1.jpeg') 
