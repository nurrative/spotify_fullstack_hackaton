import logging
from aiogram import Bot, Dispatcher, types, executor
import yt_dlp
import os
import time
from requests import get



bot = Bot(token="6001879308:AAHy09bFhdqzcLUIHx7Ie9OJ35r9QKMlUmM")
dp = Dispatcher(bot)

class FilenameCollectorPP(yt_dlp.postprocessor.common.PostProcessor):
    def __init__(self):
        super(FilenameCollectorPP, self).__init__(None)
        self.filenames = []

    def run(self, information):
        self.filenames.append(information["filepath"])
        return [], information

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply('Привет, это музыкальный бот!')

@dp.message_handler(commands=['sea'])
async def search_cmd(message: types.Message):
    arg = message.get_args()
    YDL_OPTIONS = {'format': 'bestaudio/best',
                   'noplaylist': 'True',
                   'postprocessors': [{
                       'key': 'FFmpegExtractAudio',
                       'preferredcodec': 'mp3',
                       'preferredquality': '192'
                   }]}
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as yd1:
            try:
                get(arg)
            except:
                 filename_collector = FilenameCollectorPP()
                 yd1.add_post_processor(filename_collector)
                 video = yd1.extract_info(f"ytsearch:{arg}", download=True)['entries'][0]
                 await message.reply_document(open(filename_collector.filenames[0], 'rb'))
                 time.sleep(5)
                 os.remove(filename_collector.filenames[0])
            else:
                 video = yd1.extract_info(arg, download= True)

            return filename_collector.filenames[0]



if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=True)