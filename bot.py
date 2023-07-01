
'''
Телеграмм бот был создан с помощью библиотеки: Aiogram, Yt_dlp и двух программ FFprog и FFmpeg.
Бот позволяет пользователям искать и загружать видео с YouTube в формате аудио.
'''
import logging
from aiogram import Bot, Dispatcher, types, executor
import yt_dlp
import os
import time
from requests import get

# Создаем экземпляр бота и диспетчера:
bot = Bot(token="6001879308:AAHy09bFhdqzcLUIHx7Ie9OJ35r9QKMlUmM")
dp = Dispatcher(bot)

# Создаем класс FilenameCollectorPP, который используется для сбора и хранения путей к загруженным аудиофайлам.
class FilenameCollectorPP(yt_dlp.postprocessor.common.PostProcessor):
    def __init__(self):
        super(FilenameCollectorPP, self).__init__(None)
        self.filenames = []

    def run(self, information):
        self.filenames.append(information["filepath"])
        return [], information

# Создаем функцию, обрабатывающую команду /start, которая при запуске отправляет приветственное сообщение:
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply('Привет, это музыкальный бот!')

# Создаем функцию, обрабатывающую команду  /youtube, которая при запуске выполняет поиск и загрузку аудиофайла с YouTube:
@dp.message_handler(commands=['youtube'])
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
                 file_path = filename_collector.filenames[0]
                 new_file_path = os.path.join('media', os.path.basename(file_path))
                 os.rename(file_path, new_file_path)
                 await message.reply_document(open(new_file_path, 'rb'))
                 time.sleep(5)
                 os.remove(new_file_path)
            else:
                 video = yd1.extract_info(arg, download= True)

            return filename_collector.filenames[0]


# Запуск бота:
if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=True)