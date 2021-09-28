import logging
import sys 

logFileName = sys.argv[0].split(".")[0] + ".log"
print(logFileName)

#FORMAT = '%(asctime)-15s %(level)-15s %(message)s'
#logging.basicConfig(format=FORMAT)

logging.basicConfig(filename=logFileName, level=logging.DEBUG)
#, format=FORMAT)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

