import pexpect
import sys
import logging
import time 

child = pexpect.spawn ('ssh calsoft@localhost')
#print spawn_i
#logging.warning (child)

child.logfile = sys.stdout
if (child.expect ('(yes/no)? ')):
    child.sendline ('yes')
child.expect ('[pP]assword:')
child.send ('password\n')
child.expect ('junoController:~[#$]')
child.sendline ('ls -l')
child.expect('junoController:~[$#]')
print "\n=============>", child.after, "<========\n"

#time.sleep (60)

child.sendline ('logout')
child.expect('Connection to localhost closed.')


#print child.isalive()
#child.interact()
