#!/usr/bin/python
from library import exif,linux,scan
#print exif.Edate('./image/1FA/1.jpeg')
#result=linux.command(command_line)
#print scan.imagecode('./image/1FA/1.jpeg')

command_line='find ./image  -name  \'*.*\' '
file_list=linux.command(command_line).split('\n')
file_list.remove('')
print "file_list \n" ,file_list
for s_f in file_list:
    f_dir,f=str(s_f.rpartition('/')[0]+'/'),s_f.rpartition('/')[2]
    f_code=scan.imagecode(s_f)
    f_name,f_subname=f.rpartition('.')[0],f.rpartition('.')[2]
    mv_f_name=(f_name==f_code)and str('d'+f_name) or f_code
    mv_f=f_dir+'/'+mv_f_name +'.'+f_subname
    com_mv=['mv',s_f,mv_f]
    linux.command(com_mv)
