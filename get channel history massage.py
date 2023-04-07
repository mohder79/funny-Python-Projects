import pandas as pd
from telethon import TelegramClient

# { api info and phone numbber
api_id = 
api_hash = ''
client = TelegramClient('session', api_id, api_hash)

# }

# { channel id and number of message you wont
channel_id = 'https://t.me/+ElGmg5YJIA00MDlk'
message_count = 1000000

# }
data1 = []
data2 = []


async def main():
    async with client:
        channel = await client.get_entity(channel_id)

        async for message in client.iter_messages(channel, limit=message_count):
            text = message.text
            date = message.date
            # dt_without_tz = date.replace(tzinfo=None)

            data1.append(text)
            data2.append(date)


with client:
    client.loop.run_until_complete(main())


# print(data1)
df = pd.DataFrame(
    {'text': data1,
     'date': data2
     })

df.columns = ['text', 'date']
df['date'] = pd.to_datetime(df['date'])

df['date'] = pd.to_datetime(
    df['date']).dt.tz_convert('iran')
df['date'] = df['date'].dt.tz_localize(None)

df.to_excel('your_excel.xlsx')

print('complate')
