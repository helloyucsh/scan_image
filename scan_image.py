#!/usr/bin/python
from sys import argv
import zbar,string
import Image
import subprocess

333333333333333333333333333333333333333333333333333333333333333333
def linux_command(command_line):
    process1=subprocess.Popen(command_line,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result,err=process1.communicate()
    return result,err

#####################################################################
def move_old_image(filename):
    #find file's directory
    print 'check file if it should be removed or not',filename
    command_line=['find','./image/','-name',filename]
    result,err = linux_command(command_line)
#    result=result.split('\n')
#    for search_result in result:
    search_result=result.replace('\n','')
    if not(search_result==''): 
	        print 'need to removed file',search_result
        	moved=search_result.rpartition('/')[0]+'/'
                moved=moved+'_removed_'+filename
	        command_line=['mv',str(search_result),moved]
	        mv_result,err=linux_command(command_line)
                if not(err==''):
            		print'need to remove file ,but some error ==>',mv_result
                        print 'shwo mv err and exit program\n',err
                    	exit(1)
                else:
	            print 'Completely have moved file',moved


    # obtain image data
def getimagecode(filelist):

    # create a reader
    scanner = zbar.ImageScanner()
    # configure the reader
    scanner.parse_config('enable')

    filelist.translate(string.maketrans("\t\r", "  "))
    filelist_split=filelist.split('\n')
    filelist_split.remove('')
    print filelist_split
    filename_map_codenumber=[]
    file_sub_name='_scanned.'+argv[1].rpartition('.')[2]
    for filename in filelist_split:
        if not(string.find(filename,'scanned')==-1):
              print 'without to be scanned',filename 
              continue
#       print 'filename is what %s %s',type(filename),filename
#       print 'rpartion filename is',filename.rpartion('/')
#       print 'scan image {0} need to be scan'.format(filename)        
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
	    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
            extract_dir=filename.rpartition('/')[0]+'/' 
            extract_file=symbol.data+file_sub_name
            move_old_image(extract_file)
            extract_file_inc_dir=extract_dir+extract_file
            filename_map_codenumber.append([filename,extract_file_inc_dir])
            
    # clean up
    del(image)
    return filename_map_codenumber

if len(argv)<2: exit(1)
command_line=['find','./image/','-name',str(argv[1])]
search_result,err = linux_command(command_line)
print 'linux_command result:',search_result,err 

filename_map_codenumber=getimagecode(search_result)
for map in filename_map_codenumber:
    print map[0],'<==>',map[1]

for source_destination in filename_map_codenumber:
    command_line=['cp',source_destination[0],source_destination[1]]
    search_result,err = linux_command(command_line)
    if not(err==""):
       print 'scanned image {0} was failed to copy'.format(source_destination[0])
       exit(1) 
    else: 
        print 'sucess scan one image',source_destination[0]
        print 'will delete original image',source_destination[0]
      
        command_line=['rm',source_destination[0]]
        search_result,err = linux_command(command_line)
        if not(err==''):
            print 'fail to delete file',source_destination[0]
            exit(1)


print 'program succedd ,end it '
