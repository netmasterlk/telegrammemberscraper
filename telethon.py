from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = '2255829'
api_hash = '373664cf34a9802a4a78ee0c55a3cd2d'

client = TelegramClient('session_name', api_id, api_hash)
client.start()