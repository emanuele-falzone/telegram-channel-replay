from telethon import TelegramClient, events
from decouple import config

CHANNEL = config("CHANNEL")
API_ID = config("API_ID")
API_HASH = config("API_HASH")
BOT_TOKEN = config("BOT_TOKEN")
BOT_TARGET_CHANNEL = config("BOT_TARGET_CHANNEL")
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
        await bot.send_message(BOT_TARGET_CHANNEL, event.message)

async def main():
    print(f"API_ID: {API_ID}")
    print(f"API_HASH: {API_HASH}")

    print(f"Channel name: {CHANNEL}")

    channel_chat_id = await get_dialog_id(CHANNEL)
    print(f"Channel chat id: {channel_chat_id}")

    print(f"Keywords: {', '.join(KEYWORDS)}")
    client.add_event_handler(handler, events.NewMessage(chats=[channel_chat_id]))

client.loop.run_until_complete(main())
client.run_until_disconnected()