import logging
import sys 

logFile=sys.argv[0].split('.')[0] + ".log"
print(logFile)

logFormat = '%(asctime)s - %(levelname)s: %(message)s'

#logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)

logging.basicConfig(filename=logFile, level=logging.DEBUG, format=logFormat)

logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
