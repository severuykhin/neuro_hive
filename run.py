import telebot
import traceback
import time
import sys
import os
import json
import numpy as np

# Bot metadata
from key import KEY

# Modules
from gender_by_name.module import GenderByName
from cats_vs_dogs.module import CatsVsDogs
from eye_glasses.module import EyeGlasses

import pathlib


bot = telebot.TeleBot(KEY)
modules = {
    'cats_vs_dogs': CatsVsDogs, 
    'gender_by_name': GenderByName,
    'eye_glasses': EyeGlasses
}

args = sys.argv
module_name = args[1]

if not module_name in modules:
    raise Exception('Has no module named "%s". Use "%s"' % (module_name, ', '.join(modules)))

module = modules[module_name]()

@bot.message_handler(content_types="text")
def handler_text(message):
    response = module.handleTextMessage(message)
    bot.send_message(message.from_user.id, response)

@bot.message_handler(content_types=["photo"])
def handler_image(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    temp_file_name = '%s-%s.jpg' %(message.from_user.id, 'eee')
    temp_file_path = os.getcwd() + '/temp/' + temp_file_name

    with open(temp_file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
        response = module.handleImage({
            "file_path": temp_file_path
        })
        bot.send_message(message.from_user.id, response)


while True:
    try:
        bot.polling(none_stop=True)

    except KeyboardInterrupt as e:
        program.stop()
        sys.exit(0)
        break

    except Exception as e:
        print(e)
        time.sleep(15)
