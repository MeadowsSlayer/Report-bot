from bot import *
import sqlite3

def connect():
    connection = sqlite3.connect('DB FOR BOT.db', check_same_thread=False)
    return connection


def message_send():
	a=0
	i=0
	b=0
	while True:
		connects = connect()
		cursor = connects.cursor()
		cursor.execute('SELECT UserID FROM User')
		result = cursor.fetchall()
		cursor.execute('SELECT COUNT(*) FROM User')
		count = str(cursor.fetchone())
		cursor.close()
		connects.close()
		now_time = datetime.datetime.now()
		if (now_time.hour == 9) or (now_time.hour == 12) or (now_time.hour == 18):
			for row in result:
				if str(b) in str(count):
					time.sleep(3600)
					b=0
				print(row)
				make = types.ReplyKeyboardMarkup()
				buttion_1 = types.KeyboardButton(text="Я на объекте")
				buttion_2 = types.KeyboardButton(text="Я в дороге")
				buttion_3 = types.KeyboardButton(text="Я дома")
				buttion_4 = types.KeyboardButton(text="Я в лаборатории")
				buttion_5 = types.KeyboardButton(text="Другое")
				make.add(buttion_1, buttion_2, buttion_3, buttion_4, buttion_5)
				bot.send_message(row[i], "Где вы или чем заняты?", reply_markup=make)
				++i
				b+=1
