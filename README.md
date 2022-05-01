
# Use case

You found a really interesting telegram channel that publishes a message about whether a GPU is available on amazon.
Interesting, but annoying at the same time: you receive a notification for both AMD and NVIDIA GPUs, but you are only interested in NVIDIA GPUs, so you get a lot of useless notifications.
You'd like to have a channel that notifies you only about NVIDIA GPU availability, but you do not want to build it from scratch.
Here is the solution to your problem! 

# How does it work?

![Dataflow Image](images/dataflow.png)

The python script reads the messages from the source channel and publishes those that satisfy the filtering condition on the target channel.

To read the messages from the `SOURCE_CHANNEL` the python script has to act as a real user who is subscribed to the channel.
To let the script access your telegram account, you will need the `API_ID` and `API_HASH` values that you can find using the [Telegram API Development Tools](https://core.telegram.org/api/obtaining_api_id).

The python script will select only the messages that contains ALL the specified `KEYWORDS`.
Moreover, the python script has to act as a bot that can publish messages in the target channel.
To create the bot and/or the target channel you can refer to the official [Telegram FAQ](https://telegram.org/faq).
In particular, you need the `BOT_TOKEN` that allows the script to impersonate the bot, and the `TARGET_CHANNEL` to identify the target channel itself.

# Usage

```
docker build -t telegram-channel-replay .
```

```
docker run -it \
    -e API_ID=<API_ID> \
    -e API_HASH=<API_HASH> \
    -e BOT_TOKEN=<BOT_TOKEN> \
    -e TARGET_CHANNEL=<TARGET_CHANNEL> \
    -e SOURCE_CHANNEL=<SOURCE_CHANNEL> \
    -e KEYWORDS=<KEYWORDS> \
    telegram-channel-replay
```

Every time you run the script it will ask you for your phone number or bot token to verify your identity.
