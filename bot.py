import config
import telebot
from telebot import types
import sqlite3
import time
import threading


conn = sqlite3.connect('DB FOR BOT3.db', check_same_thread=False)
cursor = conn.cursor()

global null
null = "0"
global action2
action2 = "0"
global a
a = "0"
global b
b = "0"
global c
c = "0"
global d
d = "0"
global e
e = "0"
global f
f = "0"
global g
g = "0"
global r
r = "0"
global v
v = "0"
global z
z = "0"
global action
action = "0"
global place
place = "0"
global road
road = "0"
global u
u = "0"
global UserName_2
UserName_2 = "0"
global UserID_1
UserID_1 = "0"
global first
first = "0"
global second
second = "0"
global third
third = "0"
global UserID
UserID = 0
global Rights
Rights = 0

user = [372111586]
admins = [372111586]

bot = telebot.TeleBot(config.token)

def message_send():
    global u
    statTime = time.strftime("%H:%M")
    dateTime = time.strftime("%A")
    while True:
        if statTime == "9:00" or statTime == "13:00" or statTime == "18:00":
            for beta in user:
                if u == "0":
                    make = types.ReplyKeyboardMarkup()
                    buttion_1 = types.KeyboardButton(text="Я на объекте")
                    buttion_2 = types.KeyboardButton(text="Я на работе")
                    buttion_3 = types.KeyboardButton(text="Я дома")
                    buttion_4 = types.KeyboardButton(text="Я в лаборотории")
                    buttion_5 = types.KeyboardButton(text="Другое")
                    make.add(buttion_1, buttion_2, buttion_3, buttion_4, buttion_5)
                    bot.send_message(beta, "Где вы или чем заняты?", reply_markup=make)
                    u = "1"
                if dateTime == "Monday":
                    cursor.execute("SELECT DateTime, Action, PlaceProject, Action2, Road"
                                   " FROM Table_2 ORDER BY ID LIMIT ?", (str(beta)))
                    result = cursor.fetchall()
                    bot.send_message(beta, result)
        if statTime == "9:01" or statTime == "13:01" or statTime == "18:01":
            u = "0"
        if (statTime == "9:30" or statTime == "13:30" or statTime == "18:30") and first == "0":
            for beta in user:
                if u == "0":
                    make = types.ReplyKeyboardMarkup()
                    buttion_1 = types.KeyboardButton(text="Я на объекте")
                    buttion_2 = types.KeyboardButton(text="Я на работе")
                    buttion_3 = types.KeyboardButton(text="Я дома")
                    buttion_4 = types.KeyboardButton(text="Я в лаборотории")
                    buttion_5 = types.KeyboardButton(text="Другое")
                    make.add(buttion_1, buttion_2, buttion_3, buttion_4, buttion_5)
                    bot.send_message(beta, "Где вы или чем заняты?", reply_markup=make)
                    u = "1"

# Реакция на комманду /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте! Я бот для отчетов, каждый день нещадно с 9 утра спамить вас запросами "
                     "об отчетах покуда вы не ответите. Вы сами на это подписались! "
                     "Надеюсь наша работа с вами будет успешной.")
    for beta in admins:
        bot.send_message(message.chat.id,
                         "Вы являетесь админом и можете заносить новых пользователей с помощью команды '/newperson'.")

# ID new
@bot.message_handler(commands=["newperson"])
def new():
    global a
    for beta in admins:
        a = "2"
        bot.send_message(beta, "New user name:")

@bot.message_handler(regexp=["1"])
def hamon_user(message):
    global a
    global UserName
    for beta in admins:
        UserName = message.text
        bot.send_message(beta, "Rights(Админ-1, Обычный пользователь-2):")
        a = "4"

@bot.message_handler(regexp=["2"])
def muda_muda(message):
    global a
    global UserName
    for beta in admins:
        UserName = message.text
        bot.send_message(beta, "Rights(Админ-1, Обычный пользователь-2):")
        a = "4"

# Развитие событий "Я на объекте"
@bot.message_handler(regexp="Я на объекте")
def handle_message(message):
    global UserID1
    global first
    first="1"
    cursor.execute("SELECT UserID FROM User")
    UserID1 = cursor.fetchall()
    workup = types.ReplyKeyboardMarkup()
    button_New = types.KeyboardButton(text="Объект новый")
    buttion_old = types.KeyboardButton(text="Объект старый")
    workup.add(button_New, buttion_old)
    bot.send_message(message.chat.id, "На каком объекте?", reply_markup=workup)
    global action
    action = message.text


@bot.message_handler(regexp="Объект новый")
def handle_message_id(message):
    bot.send_message(message.chat.id, "Напишите название объекта. Помните вы не можете иметь более 3-х объектов")
    global a
    a = "1"


@bot.message_handler(regexp="Объект старый")
def handle_message_id(message):
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    if b != "0":
        buttion_one = types.KeyboardButton(b)
        maxup.add(buttion_one)
    if c != "0":
        buttion_two = types.KeyboardButton(c)
        maxup.add(buttion_two)
    if d != "0":
        buttion_three = types.KeyboardButton(d)
        maxup.add(buttion_three)
    bot.send_message(message.chat.id, "Напишите название объекта на котором вы сейчас", reply_markup=maxup)
    global a
    a = "1"


# Развитие событий "В лаборотории"
@bot.message_handler(regexp="Я в лаборотории")
def mess(message):
    global first
    global action
    action = message.text
    first = "1"
    work = types.ReplyKeyboardMarkup(row_width=1)
    buttion_new = types.KeyboardButton(text="Я занимаюсь чем-то новым")
    buttion_old = types.KeyboardButton(text="Я все еще работаю над одним из старых проектов")
    work.add(buttion_new, buttion_old)
    bot.send_message(message.chat.id, "Что вы там делаете?", reply_markup=work)


@bot.message_handler(regexp="Я занимаюсь чем-то новым")
def new(message):
    bot.send_message(message.chat.id, "Напишите название объекта. Помните вы не можете иметь более 3-х проектов")
    global z
    z = "1"


@bot.message_handler(regexp="Я все еще работаю над одним из старых проектов")
def handle_message_id(message):
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    if e != "0":
        buttion_one = types.KeyboardButton(e)
        maxup.add(buttion_one)
    if f != "0":
        buttion_two = types.KeyboardButton(f)
        maxup.add(buttion_two)
    if g != "0":
        buttion_three = types.KeyboardButton(g)
        maxup.add(buttion_three)
    bot.send_message(message.chat.id, "Напишите, чем именно вы сейчас заняты", reply_markup=maxup)
    global z
    z = "1"


# Реакция на "В дороге"
@bot.message_handler(regexp="Я в дороге")
def road_mess(message):
    global first
    first = "1"
    bot.send_message(message.chat.id, "Куда вы едете?")
    global action
    action = message.text
    global r
    r = "1"


# Реакция на "Другое"
@bot.message_handler(regexp="Другое")
def other(message):
    global first
    first = "1"
    bot.send_message(message.chat.id, "Напишите.")
    global action
    action = message.text
    global v
    v = "1"


# Реакция на "Дома"
@bot.message_handler(regexp="Я дома")
def other(message):
    global first
    first = "1"
    global UserID_1
    global UserName_2
    global place
    global action
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    action = message.text
    place = "0"
    cursor.execute("INSERT INTO Table_2 VALUES(%r,%i,%r,%r,%r,%r,%r,%r)" %
                   (str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), action, place, action2, null))
    conn.commit()
    bot.send_message(message.chat.id, "Ок")

# Удаление проектов
@bot.message_handler(regexp="Я хочу удалить проект")
def delete(message):
    global jo
    jo=1
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    if e != "0":
        buttion_one = types.KeyboardButton(e)
        maxup.add(buttion_one)
    if f != "0":
        buttion_two = types.KeyboardButton(f)
        maxup.add(buttion_two)
    if g != "0":
        buttion_three = types.KeyboardButton(g)
        maxup.add(buttion_three)
    bot.send_message(message.chat.id, "Выберите проект на удаление", reply_markup=maxup)

# Удаление объектов
@bot.message_handler(regexp="Я хочу удалить объект")
def delete(message):
    global jo
    jo=1
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    if a != "0":
        buttion_one = types.KeyboardButton(a)
        maxup.add(buttion_one)
    if b != "0":
        buttion_two = types.KeyboardButton(b)
        maxup.add(buttion_two)
    if c != "0":
        buttion_three = types.KeyboardButton(c)
        maxup.add(buttion_three)
    bot.send_message(message.chat.id, "Выберите объект на удаление", reply_markup=maxup)

# Реакция на любой текст
@bot.message_handler(content_types=["text"])
def messsage_reaction(message):
    global r
    global a
    global b
    global c
    global d
    global place
    global action2
    global action
    global road
    global z
    global UserName
    global UserID
    global Rights
    global UserName_2
    global UserID_1
    global null
    global e
    global f
    global g
    global jo
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    if road == "1":
        road = message.text
        bot.send_message(message.chat.id, "Я запомню это")
        cursor.execute("INSERT INTO Table_2 VALUES(%r,%i,%r,%r,%r,%r,%r,%r)" %
                       (str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), action, place, action2, road))
        conn.commit()
    if r == "0":
        pass
    elif r == "1":
        place = message.text
        bot.send_message(message.chat.id, "Зачем?")
        r = "0"
        road = "1"
    if jo == 1:
        if message.text == e:
            e = f
            f = g
            g = "0"
        if message.text == f:
            f = g
            g = "0"
        if message.text == e:
            g = "0"
        if message.text == a:
            a = b
            b = c
            c = "0"
        if message.text == b:
            b = c
            c = "0"
        if message.text == c:
            c = "0"
        jo = 0
    if v == "1":
        action2 = message.text
        bot.send_message(message.chat.id, "Я запомню это")
        cursor.execute("INSERT INTO Table_2 VALUES(%r,%i,%r,%r,%r,%r,%r,%r)" %
                       (str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), action, place, action2, null))
        conn.commit()
    if z == "1":
        place = message.text
        z = "0"
        bot.send_message(message.chat.id, "Я запомню это")
        cursor.execute("INSERT INTO Table_2 VALUES(%r,%i,%r,%r,%r,%r,%r,%r)"%
                       (str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), action, place, action2, null))
        conn.commit()
    if a == "0":
        UserID = "0"
        Rights = "0"
        UserName = "0"
        if action2 == "1":
            action2 = message.text
            cursor.execute("INSERT INTO Table_2 VALUES(%r,%i,%r,%r,%r,%r,%r,%r)" %
                           (str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), action, place, action2, null))
            conn.commit()
            bot.send_message(message.chat.id, "Я запомню это")
    if a == "1":
        if b == "0":
            b = message.text
            if b != "0":
                c = message.text
                if c != "0":
                    d = message.text
        place = message.text
        bot.send_message(message.chat.id, "Что вы там делаете?")
        a = "0"
        action2 = "1"
    if a == "2":
        Rights = message.text
        bot.send_message(message.chat.id, "Rights:")
        a = "0"
    if a == "4":
        UserID = int(message.text)
        cursor.execute("INSERT INTO User VALUES(?,?,?,?)", (UserName, UserID, Rights, null))
        conn.commit()
        a="0"
        user.append(message.text)
        if Rights == "1":
            admins.append(message.text)

if __name__ == '__main__':
    t = threading.Thread(target=message_send)
    t.start()
    bot.polling(none_stop=True)
