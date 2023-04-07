from telethon import TelegramClient, events
import re



def signal(text):
    symbol = (re.findall(r'\w+/\w+', text)[0])
    print('symbol :',  symbol)
    direction = 'long' if (re.search(r'Long', text)) else 'short'
    print('direction :', direction)
    leverage = re.search(r'x\d+', text).group()
    print('leverage: ', leverage)
    split_text = text.split('\n')
    list = ['Entry', '🥇', '🥈', '🥉', '🚀']
    price_list = []
    for line in split_text:
        for item in list:
            if item in line:
                price = re.findall(r'\d+', line)
                len_price = len(price)
                if item == 'Entry' and len_price >= 2:
                    price = f'{price[0]}.{price[1]}'
                    price_list.append(price)
                elif item == 'Entry':
                    price_list.append(price[0])

                if len_price > 2 and item != 'Entry':
                    price = f'{price[0]}.{price[1]}'
                    price_list.append(price)

                elif item != 'Entry':
                    price_list.append(price[0])
    entry = price_list[0]
    print('entry:', entry)
    tp1 = price_list[1]
    print('tp1', tp1)
    tp2 = price_list[2]
    print('tp2', tp2)
    tp3 = price_list[3]
    print('tp3', tp3)
    tp4 = price_list[4]
    print('tp4', tp4)

    return symbol, direction, leverage, entry, tp1, tp2, tp3, tp4


# { api
api_id = ''
api_hash = ''

# }


# { phone numbers  format(+contry code and number)

phone = '+'

# }


client1 = TelegramClient('session', api_id, api_hash)


@client1.on(events.NewMessage)
async def handle_message1(event):

    message_text = event.message.text  # message text
    chat_id = int(re.findall(r'\d+', str(event.message.peer_id))
                  [0])  # get chat id

    # { channel id condition

    if chat_id == 'id' :  #  , 
        # Send the last received message to the specific user
        await client1.send_message('telagram id', f"send this message:\n {message_text}")
        print(message_text)
        await client1.send_message('telagram id', f" {signal(message_text)}")


client1.start(phone=phone)
client1.run_until_disconnected()


