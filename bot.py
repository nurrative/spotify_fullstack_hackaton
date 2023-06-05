#Telegram-бота с использованием библиотеки aiogram и позволяет пользователям искать и загружать видео с YouTube в формате аудио.
import logging
from aiogram import Bot, Dispatcher, types, executor
import yt_dlp
import os
import time
from requests import get


# 2 Создание экземпляров бота и диспетчера:

bot = Bot(token="6001879308:AAHy09bFhdqzcLUIHx7Ie9OJ35r9QKMlUmM")
dp = Dispatcher(bot)
# 3 Определение пользовательского класса постпроцессора FilenameCollectorPP
class FilenameCollectorPP(yt_dlp.postprocessor.common.PostProcessor):
    def __init__(self):
        super(FilenameCollectorPP, self).__init__(None)
        self.filenames = []
# 4 Этот класс расширяет класс PostProcessor из модуля yt_dlp.postprocessor.common. 
# Он собирает имена файлов загруженных аудиофайлов.

    def run(self, information):
        self.filenames.append(information["filepath"])
        return [], information
# Обработка команды /start:
# Эта функция отправляет ответное сообщение, когда пользователь отправляет команду /start.
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply('Привет, это музыкальный бот!')
#Обработка команды /sea для поиска и загрузки видео с YouTube:
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
                 await message.reply_document(open(filename_collector.filenames[0], 'rd'))
                 time.sleep(5)
                 os.remove(filename_collector.filenames[0])
            else:
                 video = yd1.extract_info(arg, download= True)

            return filename_collector.filenames[0]

#Эта функция обрабатывает команду /sea для поиска и загрузки видео с YouTube. Внутри функции происходит следующее:

# Получение аргументов команды, переданных пользователем.
# Определение параметров загрузки видео с YouTube, включая формат аудио





if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=True)