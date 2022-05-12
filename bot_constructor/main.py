import telebot
from telebot import types
import config
import site_constructor
import Photo_to_text

bot = telebot.TeleBot(config.bot_ip)

def Download_Photo(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'Files/' + message.photo[1].file_id + '.png'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    return src

def text_for_site(text):
    text = text.replace('<', '&#60;')
    text = text.replace('>', '&#62;')
    text = text.replace('<', '&#60;')
    text = text.replace('&', '&#38;')
    text = text.replace('"', '&#34;')
    text = text.replace("'", '&#39;')
    text = text.replace('«', '&#171;')
    text = text.replace('»', '&#187;')
    text = text.replace("‘", '&#8216;')
    text = text.replace("’", '&#8217;')
    text = text.replace("‚", '&#8218;')
    text = text.replace("“", '&#8220;')
    text = text.replace('”', '&#8221;')
    text = text.replace("„", '&#8222;')
    return text

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("создать сайт")
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)
@bot.message_handler(content_types=['text', 'photo'])
def get_start_messages(message):
    if message.text == 'создать сайт':
        site_constructor.create_site()
        bot.send_message(message.from_user.id, "Введите Название сайта: ")
        bot.register_next_step_handler(message, get_title)
def get_title(message):
    site_constructor.choose_title(message.text)
    bot.send_message(message.from_user.id, 'Введите цвета фона на сайте(в формате HEX: #000000) или отправте картинку как фон')
    bot.register_next_step_handler(message, get_background)

def get_background(message):
    if message.content_type == 'photo':
        site_constructor.choose_background(Download_Photo(message), True)
        bot.send_message(message.from_user.id, 'Введите параметры DIV')
        bot.register_next_step_handler(message, get_div)
    if message.content_type == 'text':
        if message.text[0] == '#' and len(message.text) == 7:
            site_constructor.choose_background(message.text, False)
            bot.send_message(message.from_user.id, 'Введите параметры DIV')
            bot.register_next_step_handler(message, get_div)
        else:
            bot.send_message(message.from_user.id, 'Введите цвет в формате HEX')
            bot.register_next_step_handler(message, get_background)

def get_div(message):
    filling, top, left, color = message.text.split(',')
    site_constructor.add_div(filling, top, left, color)
    Send_Done_Site(message)

def Send_Done_Site(message):
    site_constructor.complete_creation()
    bot.send_message(message.from_user.id, 'Сайт создан!')
    f = open("index.html", 'rb')
    bot.send_document(message.from_user.id, f)
    f.close()
bot.polling(none_stop=True, interval=0)

