from telethon import TelegramClient, events

api_id = 
api_hash = ''

client = TelegramClient('session_name', api_id, api_hash)


@client.on(events.NewMessage)
async def handle_message(event):
    message_text = event.message.text
    chat_id = event.message.peer_id
    date = event.message.date
    user = await event.get_sender()
    username = user.username
    print(
        f"Received message '{message_text}' from chat '{chat_id}' date '{date}' username {username}")

    if message_text.lower() == 'hi':
        await client.send_message(chat_id, 'Hi to You')

    if "🔥" in message_text.lower() and "profit" in message_text.lower():
        # Send the last received message to the specific user
        await client.send_message('mohder', f"Last message is: {message_text }")

    if "🔥" in message_text.lower() and "profit" in message_text.lower():
        # Send the last received message to the specific user
        await client.send_message('Farzin_fakharii', f"Last message is: {message_text }")


client.start()
client.run_until_disconnected()
