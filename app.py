from pyrogram import client, filters
from helpers import verifyCommand
from useYTDlp import delete_created_video, download_video
from dotenv import load_dotenv
import os

Client = client.Client

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

if(not api_id):
    raise Exception('API_ID is not set')
if(not api_hash):
    raise Exception('API_HASH is not set')

app = Client(
    "my_bot",
    api_id=api_id, 
    api_hash=api_hash,
)
       
@app.on_message(filters.text)
async def my_handler(_, message):
    print('message detected')
    if(message.chat.id != -1001439976239):
        return

    text = message.text
    command = verifyCommand(text)

    if(not command):
        return 

    print('init attempt to download ', message.text)

    text_split = text.split(command).strip(' ')

    """ if theres nothing after /ytdlp """
    if(len(text_split) <= 1):
        return

    possible_link = text_split[1].strip(' ')
    video_filename, exception = download_video(possible_link)
    if(isinstance(exception, Exception)):
        print(exception)
        await message.reply_text(f'Error downloading video {exception}')
        return

    if(not isinstance(video_filename, str)):
        return

    print('Sending video...')

    response = await message.reply_video(video_filename, quote=True)
    if(response):
        print('Video sent')
    else:
        print('Error sending video')

    is_deleted = delete_created_video(video_filename)

    if is_deleted:
        print('Video deleted from ', video_filename)
    else:
        print('Video couldnt be deleted from ', video_filename)

app.run()
