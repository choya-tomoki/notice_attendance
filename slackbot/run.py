from slackbot.bot import Bot
import logging

from slackbot_settings import API_TOKEN
logging.basicConfig()


def run():
    bot = Bot()
    bot.run()

    
print('start slackbot')
run()