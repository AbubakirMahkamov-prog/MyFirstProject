import telebot,requests,json
from telebot import types
valyu=requests.get('https://nbu.uz/uz/exchange-rates/json/')
valyutalar=[]
if valyu.status_code==200:
    valyutalar=json.loads(valyu.content)
bot = telebot.TeleBot("1492086900:AAGBxwMbAtaJheqfi8-SmiyGKj82wUaAz9M")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('AQSh dollari')
    itembtn2 = types.KeyboardButton('Yevro')
    itembtn3 = types.KeyboardButton('Rossiya rubli')   
    itembtn4 = types.KeyboardButton('Angliya funt sterlingi') 
    itembtn5 = types.KeyboardButton('Shveytsariya franki') 
    itembtn6 = types.KeyboardButton('Yaponiya iyenasi') 
    itembtn7 = types.KeyboardButton('Qozog‘iston tengesi') 
    itembtn8 = types.KeyboardButton('Xitoy yuani')
    itembtn9 = types.KeyboardButton('Daniya kronasi')
    itembtn10 = types.KeyboardButton('Misr funti')   
    itembtn11 = types.KeyboardButton('Malayziya ringgiti') 
    itembtn12 = types.KeyboardButton('Koreya respublikasi voni') 
    itembtn13 = types.KeyboardButton('BAA dirhami') 
    itembtn14 = types.KeyboardButton('Kanada dollari') 
    markup.row(itembtn1,itembtn2,itembtn3)
    markup.row(itembtn4,itembtn5,itembtn6)
    markup.row(itembtn7,itembtn8,itembtn9)
    markup.row(itembtn10,itembtn11,itembtn12)
    markup.row(itembtn13,itembtn14)
    bot.send_message(message.chat.id, "<b>Valyuta kurslari uchun davlarlardan birini tanlang</b>", reply_markup=markup,parse_mode='HTML')
@bot.message_handler(func=lambda message:True)
def javob(message):
        for i in valyutalar:
            if i['title']==message.text:
                bot.send_message(message.chat.id,'<b>'+message.text+'</b>\n\n<b>1   '+i['code']+'  ning narxi</b>   :  '+i['cb_price'] +'\n\n<b>Vaqt holatiga</b> : '+i['date']+'\n\n<b>Manba  :</b>  nbu.uz',parse_mode='HTML')
bot.polling()
