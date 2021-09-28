import re,sys,logging
from helpers.http_requests import httpOperation
from helpers.json_helper import jsonOperation

baseFileName = sys.argv[0].split(".")[0]
logFileName = baseFileName + '.log'
jsonFileName = baseFileName + '.json'
# print(logFileName)
FORMAT = '%(asctime)s - %(levelname)s: %(name)s - %(message)s'
logging.basicConfig(filename=logFileName, level=logging.DEBUG, format=FORMAT)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(name)s - %(message)s')
logger = logging.getLogger(__name__)
validIpPattern = re.compile('((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]){1,3}')

if __name__=="__main__":
    testbaseUrl = 'http://localhost:9000'
    token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2ZXIiOiIwIiwic2NvcGUiOlsidHJ1c3QiLCJyZWFkIiwiMTExMTExMTEtMTExMS0xMTExLTExMTEtMTExMTExMTExMTExIiwid3JpdGUiXSwiYW1yIjoicHdkIiwicm9sZXMiOlsiUk9MRV9BRE1JTiJdLCJpc3MiOiJpdGQiLCJjbHVzdGVySWQiOiIxIiwiaWQiOiI2MjVhZGIyOC05MDc2LTQ4NTQtODc4MS0zZjljMGZlYjA2NTIiLCJzdWJqZWN0VHlwZSI6InVzZXIiLCJqdGkiOiI1MWE5MmZjYS0yZTIyLTQ3ODgtYmZkOC1jOGI2MWJiNDE4ZTMiLCJwYXJlbnRJZCI6IjExMTExMTExLTExMTEtMTExMS0xMTExLTExMTExMTExMTExMSIsImNsaWVudF9pZCI6ImFwaS1jbGllbnQifQ.ItL1zJdLFX4IxMlcVI7qT5P3IngkOqtpONzBxTPTMwkditEc20v050Y4fdDOGjoHyPIzOuhs6TWaP2wzAI8xSIXUfdNz8pV6d6sDjfLQhxY7FrBDuB5MzOv4EC8H3vaxu7gMj3Ci3azZCHWRggQQL7LvNOddd-zn3NAVMUq4gDn7VS9WW-Ms1Hb6s8YORp-HqJLMBs_uLtrPwSifKE9OLerLXFwWANP0dvIkFP3OjKUyQqFUFKuGN3Fd6OiYAHFvWD-vceIb-xboscMGbq_Ljz6FhbYxgI5LuLgZEGLrCIJ4CdobeYpKUypmLbgnfWyzU5i0G5qNT-cde5oaO05wWA'
    testHttp = httpOperation(testbaseUrl, token)
    output = testHttp.httpGet('aegis/rest/v1/services/targets/devices', token=token)
    out_dict = jsonOperation.convertJsonToDict(output)
    ipAddr = out_dict[0]['host']
    logger.info('ip address - %s' %ipAddr)


    ## dump json output to a file
    jsonOperation.writeJsonToFile(jsonFileName, out_dict)

    logger.info(validIpPattern.match(ipAddr))

