from telethon import TelegramClient, events
from decouple import config

API_ID = config("API_ID")
API_HASH = config("API_HASH")
BOT_TOKEN = config("BOT_TOKEN")
SOURCE_CHANNEL = config("SOURCE_CHANNEL")
TARGET_CHANNEL = config("TARGET_CHANNEL")
KEYWORDS = config("KEYWORDS", default = "").split(",")

client = TelegramClient('anon', API_ID, API_HASH).start()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

async def get_dialog_id(dialog_name):
    async for dialog in client.iter_dialogs():
        if (dialog.name == dialog_name):
            return dialog.id
    raise Error("Dialog with name {} not found!".format(dialog_name))

async def handler(event):
    if all(keyword in event.raw_text for keyword in KEYWORDS):
        await bot.send_message(TARGET_CHANNEL, event.message)

async def main():
    print(f"API_ID: {API_ID}")
    print(f"API_HASH: {API_HASH}")

    print(f"SOURCE_CHANNEL: {SOURCE_CHANNEL}")

    SOURCE_CHANNEL_CHAT_ID = await get_dialog_id(SOURCE_CHANNEL)
    print(f"SOURCE_CHANNEL_CHAT_ID: {SOURCE_CHANNEL_CHAT_ID}")

    print(f"TARGET_CHANNEL: {TARGET_CHANNEL}")

    print(f"KEYWORDS: {', '.join(KEYWORDS)}")
    client.add_event_handler(handler, events.NewMessage(chats=[SOURCE_CHANNEL_CHAT_ID]))

client.loop.run_until_complete(main())
client.run_until_disconnected()