import requests 
from config_reader import ConfigReader 
import logging 

class TelegramClient:
    def __init__(self):
        config_reader = ConfigReader()
        section_header = 'TELEGRAM'

        self.chat_id = config_reader.read_prop(section_header, 'chat_id')
        self.parse_mode = config_reader.read_prop(section_header, 'parse_mode')
        self.bot_token = config_reader.read_prop(section_header, 'bot_token')


    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&parse_mode={self.parse_mode}&text={message}"

        logging.debug("Sending message")
        
        try:
            # sends message
            response_json = requests.get(url).json()
            logging.debug(str(response_json))
            logging.debug("Message sent")
        except Exception as e:
            print("Some problem occured in sending message via telegram: {}".format(e))

