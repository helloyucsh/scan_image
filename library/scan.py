#!/usr/bin/python
import zbar,Image
def imagecode(filename):
	# create a reader
	scanner = zbar.ImageScanner()
	# configure the reader
	scanner.parse_config('enable')
	# obtain image data
	pil = Image.open(filename).convert('L')
	width, height = pil.size
	raw = pil.tostring()
	# wrap image data
	image = zbar.Image(width, height, 'Y800', raw)
	# scan the image for barcodes
	scanner.scan(image)
	# extract results
	for symbol in image:
	   # do something useful with results
	   #print 'decoded', symbol.type,'symbol', '"%s"' % symbol.data
           imagecode_is= symbol.data
           #print 'imagecode_is',imagecode_is
	# clean up
	del(image)
        return imagecode_is 
