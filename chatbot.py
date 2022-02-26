import telegram
from telegram.ext import Updater, MessageHandler, Filters
# The messageHandler is used for all message updates
# messageHandler 用于所有消息更新
import configparser
import logging


def main():
    # Load your token and create an Updater for your Bot
    #  加载你的令牌并为你的机器人创建一个更新程序
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    # You can set this logging module, so you will know when and why things do not work as expected
    # 你可以设置这个日志模块，这样你就会知道什么时候以及为什么事情没有按预期工作
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    # register a dispatcher to handle message: here we register an echo dispatcher
    # 注册一个dispatcher来处理消息：这里我们注册一个echo dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # To start the bot:
    # 启动机器人：
    updater.start_polling()
    updater.idle()


def echo(update, context):
    reply_message = update.message.text.upper()
    logging.info("Update: " + str(update))
    logging.info("context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)

if __name__ == '__main__':
    main()
