from pyrogram import client, filters
from helpers import verifyCommand
from useYTDlp import deleteCreatedVideo, downloadVideo
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

    textSplit = text.split(command)

    if(len(textSplit) <= 1):
        return

    possibleLink = textSplit[1].strip(' ')
    filename = downloadVideo(possibleLink)
    if(not filename):
        await message.reply_text("Coś nie wyszło")
        return

    print('Sending video...')

    response = await message.reply_video(filename, quote=True)
    if(response):
        print('Video sent')
    else:
        print('Error sending video')

    isDeleted = deleteCreatedVideo(filename)

    if(isDeleted):
        print('Video deleted from ', filename)
    else:
        print('Video couldnt be deleted from ', filename)

app.run()
