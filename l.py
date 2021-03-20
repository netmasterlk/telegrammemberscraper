from telethon import TelegramClient
api_id ="2255829"
api_hash = '373664cf34a9802a4a78ee0c55a3cd2d'
# 'session_id' can be 'your_name'. It'll be saved as your_name.session
client = TelegramClient('session_id', api_id, api_hash)
client.connect()
True

if not client.is_user_authorized(+94741067346):
client.send_code_request('+94741067346')
client.sign_in('+94741067346', input('Enter code: '))
...
# Now you can use the connected client as you wish
dialogs, entities = client.get_dialogs(10)
print('\n'.join('{}. {}'.format(i, str(e))
...                 for i, e in enumerate(entities)))