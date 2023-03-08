import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5539795114:AAGaPZvo3qwcJhanbczTcIWJC5ODZmCH-4g)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1AZWarzQBu3aF5ER1GzeKSFb2B9Qmu2AkZXwHw5SHatzO9gTc0eubvNnSDMikvt7W-kgZRP8flIjTKLbPlroagTKkYXjPiGLFi7CkZnbfxmzaMi_EL97HFoT791eUjzC4cXMyo_H6vYSd0-VZGz70MLe4oa2EDL5Xoa1pfcjXqYtfwB4I5HXSJHFPhhGEhb2oZJ3JzV3xwLCUR8JeF3o-iCAY_-j9quCkQT95l061KG6Ozy6cJXRRollUDk1y5qZbmOH6wjz_HlC2dZKrhtyBOw2ZQ1e1vu_FqWaji8T78MwYjuWhgkbQAgAaw-wJV6aBCsVJzU1qChOOpNQYMg-OYd3dyBxblYc=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "JoyBang_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
