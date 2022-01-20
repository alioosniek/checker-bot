call  = types.InlineKeyboardButton(text = "Enter StArt", callback_data = 'Mrko')
@bot.message_handler(commands=['start'])
def start(message):
    Keyy = types.InlineKeyboardMarkup()
    Keyy.row_width = 1
    Keyy.add(call)
    bot.send_message(message.chat.id, text=f"""Hi Pro 
Bot Chacker Bins
Country : BR  , US
By - @pmmvn
by code : @YYYYJJYY """,parse_mode="markdown",reply_markup=Keyy)
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	if call.data =="Mrko":
		button(call.message)
	if call.data =="BZ":
		AS(call.message)
	if call.data =="AM":
		AK(call.message)
		
IRAQ = types.InlineKeyboardButton(text = "BRAZIL ", callback_data= 'BZ')
IRAN = types.InlineKeyboardButton(text = "AMRICA ", callback_data = 'AM')
def button(message):
    ms = types.InlineKeyboardMarkup(row_width=1)
    ms.add(IRAQ,IRAN)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**Select the country for examination ?**",parse_mode='markdown',reply_markup=ms)
    
def AS(message):
	mr = 0
	ko = 0
	user = "12357890"
	while True:
		us = str(''.join(random.choice(user) for i in range(4)))
		bin = "37"+us
		req = requests.get(f"https://lookup.binlist.net/{bin}").json()
		country = str(req['country']['name'])
		if country == "BR":
			mr+=1
			mar = (f"""
Bin Brazil Chack True 🇧🇷
= = = = = = = = = = = = = = 
Bin : {bin}
Country : {country}
= = = = = = = = = = = = = = 
BY - @pmmvn - @YYYYJJYY""")
			bot.send_message(message.chat.id, text=mar)
		else:
			ko+=1
		mees = types.InlineKeyboardMarkup(row_width=1)
		buut = types.InlineKeyboardButton(f" : {ko}",callback_data='jhi')
		buut5 = types.InlineKeyboardButton(f"bin : {bin}",callback_data='jhi5')
		buut1 = types.InlineKeyboardButton(f" : {mr}",callback_data='jhi1')            
		mees.add(buut,buut1,buut5)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**Chack Bins Brazil **",parse_mode='markdown',reply_markup=mees)
		
		
def AK(message):
	mr = 0
	ko = 0
	user = "12357890"
	while True:
		us = str(''.join(random.choice(user) for i in range(5)))
		bin = "5"+us
		req = requests.get(f"https://lookup.binlist.net/{bin}").json()
		country = str(req['country']['name'])
		type = str(req['type'])
		if country == "US":
				mr+=1
				mar = (f"""
Bin USA Chack True 🇺🇲
= = = = = = = = = = = = = = 
Bin : {bin}
Country : {country}
= = = = = = = = = = = = = = 
BY - @pmmvn - @YYYYJJYY""")
				bot.send_message(message.chat.id, text=mar)
		else:
			ko+=1
		mees = types.InlineKeyboardMarkup(row_width=1)
		buut = types.InlineKeyboardButton(f"❌ : {ko}",callback_data='jhi')
		buut5 = types.InlineKeyboardButton(f"bin : {bin}",callback_data='jhi5')
		buut1 = types.InlineKeyboardButton(f"✅ : {mr}",callback_data='jhi1')            
		mees.add(buut,buut1,buut5)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**Chack Bins USA **",parse_mode='markdown',reply_markup=mees)
		
bot.polling()
if __name__=="__main__":
	bot.remove_webhook()
	bot.set_webhook(url="https://telegramcheckp.herokuapp.com/"+BOT_TOKEN)
	server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 9000)))
	