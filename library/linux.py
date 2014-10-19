#!/usr/bin/python
#import subprocess
from  subprocess import PIPE,Popen
import shlex
####################################################################
# input argument : <type> string ,<usage> command                  #
#                : <type> string,<usage> error_show 
#		 : <type> string ,<usage> success_show 		
# fucntion : excute linux command by PIPE			   # 
# return argument : result 					   #
####################################################################
def command(command,s_show='ex_command_ok',f_show='error to see\n'):
    command_s=(type(command) is str)and shlex.split(command) or command
#   print 'command_s \n',command_s
    process1=Popen(command_s,stdout=PIPE,stderr=PIPE)
    result,err=process1.communicate()
    if not(err==""):
       print f_show ,err ,'\n program terminate'
       exit(1)
    else:
         if not(s_show=='ex_command_ok') :   
             print s_show
    return result
