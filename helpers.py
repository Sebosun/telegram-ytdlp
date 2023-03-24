from typing import Literal

CommandsReturnType = Literal['ytdlp', False]

def verifyCommand(messageText: str) -> CommandsReturnType:
    if(messageText.startswith('/ytdlp')):
        return 'ytdlp'
    return False


