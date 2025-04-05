import telebot
from telebot.handler_backends import ContinueHandling
  
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("7913125511:AAEYrweZIDVkKOIkN5fZyal3xwuG3xRjiow")


# use in for delete with the necessary scope and language_code if necessary
bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("/start", "некоторое описание"),
        telebot.types.BotCommand("/heh", "hehheheheh")
    ],
    # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
    # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
)

# check command
cmd = bot.get_my_commands(scope=None, language_code=None)
print([c.to_json() for c in cmd])


# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start']) #'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    return ContinueHandling()

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    try:
        count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
        bot.reply_to(message, "he" * count_heh)
    except:
        bot.reply_to(message, 'Введите команду в формате /heh <число>')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello World!')
    return ContinueHandling()

@bot.message_handler(commands=['start'])
def start2(message):
    """
    This handler comes after the first one, but it will never be called.
    But you can call it by returning ContinueHandling() in the first handler.

    If you return ContinueHandling() in the first handler, the next 
    registered handler with appropriate filters will be called.
    """
    bot.send_message(message.chat.id, 'Hello World2!')

bot.infinity_polling()

# Запуск бота
bot.polling()
