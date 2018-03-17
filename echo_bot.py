import telebot
import logging

import requests
import random
import qrcode


#Read  Bot Token From File

with open ("key1.txt", "r") as key:
    token =  key.read().strip()
API_TOKEN = token

bot= telebot.TeleBot(API_TOKEN)

##### member check in channel ####
def channel_check(chat_id):
  status = ['creator', 'administrator', 'member']
  CHANNEL= '@burrito_grill'
  result = bot.get_chat_member(
    user_id=chat_id,
    chat_id=CHANNEL)
  if result.status not in status:
    try:
      bot.send_message(
        chat_id =chat_id,
        text   ='برای استفاده از ربات لطفا عضو کانال %s شوید' % CHANNEL
        )
    except:
      pass
    return -2
###############################

@bot.message_handler(func=lambda msg: True)

def get_msgs(msg):
    name = msg.chat.first_name
    lastname = msg.chat.last_name
    chat_id = msg.chat.id

    if msg.text == '/start':
        print('user by name {} is working with bot'.format(str(name) + ' ' + str(lastname)))

        newfile=open('users.txt','+a')
        newfile.write(str(name)+' '+str(lastname)+'\n')
        newfile.close()

        usern=msg.chat.username

        bot.send_message(chat_id=2829192, text='کاربر با آیدی : {} با ربات کار میکند'.format(str('@'+usern)))

        if channel_check(chat_id) == -2:
            return
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#        keyboard.row(telebot.types.KeyboardButton(u'تولید کد تخفیف'))
        keyboard.row(telebot.types.KeyboardButton(u'درباره ما'))
        keyboard.row(telebot.types.KeyboardButton(u'عکس رستوران'))
        keyboard.row(telebot.types.KeyboardButton(u'محل رستوران'))
        bot.send_message(msg.chat.id, u'به ربات کافه رستوران بوریتو خوش امدید', reply_markup=keyboard)

    if msg.text == 'محل رستوران':
        if channel_check(chat_id) == -2:
            return
        bot.send_location(msg.chat.id, latitude=35.7353595, longitude=51.4332841  )


    try:
        if msg.text=='درباره ما':
            if channel_check(chat_id) == -2:
                return
            bot.send_photo(chat_id=msg.chat.id, photo='AgADBAAD6qoxG8wZ0FCjH2adOv71Rxf_nBkABPfvAAGBlv1k03mdAwABAg',caption=u'burrito-grill.com \n'
            'کافه و رستوران بوريتو ☕️🍔 \n  آدرس: خیابان سهروردي - خیابان خرمشهر-پلاك ١٧٢✌🏼  تلفن:٨٨٥٢٢١٢١')
    except:
        pass



    if msg.text=='عکس رستوران':
        if channel_check(chat_id) == -2:
            return

        keyboard = telebot.types.ReplyKeyboardRemove()

        keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1.row(telebot.types.KeyboardButton(u'شعبه تهران'))
        keyboard1.row(telebot.types.KeyboardButton(u'شعبه متل قو'))
        keyboard1.row(telebot.types.KeyboardButton(u'شعبه نور'))
        keyboard1.row(telebot.types.KeyboardButton(u'بازگشت به منوی اصلی'))

        bot.reply_to(msg,'یکی از گزینه های زیر را انتخاب کنید :',reply_markup=keyboard1)

    if msg.text == 'شعبه تهران':
        if channel_check(chat_id) == -2:
            return
        bot.send_photo(chat_id=msg.chat.id, photo='AgADBAAD6qoxG8wZ0FCjH2adOv71Rxf_nBkABPfvAAGBlv1k03mdAwABAg',caption='تهران')
    if msg.text=='شعبه نور':
        if channel_check(chat_id) == -2:
            return
        bot.send_photo(chat_id=msg.chat.id, photo='AgADBAAD8KkxG3-JCFGzYo0GdRBoO9F6mxkABApF-fACNWTbAdcDAAEC',caption='نور')

    if msg.text=='شعبه متل قو':
        if channel_check(chat_id) == -2:
            return
        bot.send_photo(chat_id=msg.chat.id, photo="AgADBAADVqoxG8ak4FCnikrFR-cnhoHDaTAABBY4QfZm1MIRbH8AAgI",caption='متل قو')

    if msg.text=='بازگشت به منوی اصلی':
        if channel_check(chat_id) == -2:
            return
        keyboard1 = telebot.types.ReplyKeyboardRemove()
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
 #       keyboard.row(telebot.types.KeyboardButton(u'تولید کد تخفیف'))
        keyboard.row(telebot.types.KeyboardButton(u'درباره ما'))
        keyboard.row(telebot.types.KeyboardButton(u'محل رستوران'))
        keyboard.row(telebot.types.KeyboardButton(u'عکس رستوران'))
        bot.reply_to(msg,'منوی اصلی',reply_markup=keyboard)



#########
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)





bot.polling(none_stop=False, interval=0)
