from slacker import Slacker
import datetime
import time
import schedule

from slackbot_settings import API_TOKEN


slacker = Slacker(API_TOKEN)

def job():
    slacker.chat.post_message('notice-attendance', "出欠確認します！", username="出欠確認しますbot", icon_emoji="simple_smile")

schedule.every().day.at("08:30").do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().day.at("13:00").do(job)
schedule.every().day.at("14:30").do(job)
schedule.every().day.at("16:30").do(job)

  
while True:
  schedule.run_pending()
  time.sleep(60)