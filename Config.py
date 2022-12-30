import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "22733485"))
    API_HASH = os.environ.get("API_HASH", "e6095dc075ad1ef78eb7697ece6d6feb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5929537401:AAF2jMjx2tQsojl3C5JxmQXcJ__RiRjuWqQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQApmjBoh7INCB1jSLgkLKa8bTnilkJcoUAv9o2cvyMWOlxHy4lwjORABXjb24jdyCGXgLpcBIK54K2uXGBKsy5U7HVaBxjs5GAxIagb3TZhu7d0G96XY8jnSYO66Tmiktmr34nAw1HfCvx_oJmmiSByRYLRuC2s8LP_O1K2y59GYs_xsHMHHJIBwX2cjUsVGD6FxCDz_lo2mwsKSM35boEruR_2Ef6OAr7R0D7jlulTxpLi9sL-VCF92Ba_n8MdweAO6YS8CRDv5d7S6p4zIvviowmUhPJ5UPWEztZJFkon13rzT-zG01cyx0Gv53Q7IhcUGAorp9FZaknVJM5pGQu6AAAAAVxMZNEA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@PRO_MUSIC_II_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/38782fcbb44134010fba9.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/38782fcbb44134010fba9.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5843477713")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
