import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(name)s - %(message)s')
log = logging.getLogger('jsonOperation')

class jsonOperation():
    """
    A simple class that does the JSON operation,  all of them are static methods
    json keywords:
    dumps - convert json string to dict
    loads - convert dict to json
    load - loading a json file
    dump - writing the dictionary to a file
    """
    @staticmethod
    def convertJsonToDict(json_str):
        return json.loads(json_str)

    @staticmethod
    def convertDictToJson(dict_content):
        return json.dumps(dict_content)

    @staticmethod
    def loadJsonFromFile(jsonFile):
        try:
            with open(jsonFile) as f0:
                json_dict = json.load(f0)
        except Exception as err:
            log.error(err)
        else:
            return json_dict

    @staticmethod
    def writeJsonToFile(jsonFile, dict_content):
        try:
            with open(jsonFile, "w") as f0:
                json.dump(dict_content, f0)
                log.info('Successfully wrote JSON to a file')
        except Exception as err:
            log.error(err)