#! /usr/bin/env python
# -*- coding: utf-8 -*-
import config
from config import *
import telebot
from telebot import types
import sqlite3
import time
import threading


conn = sqlite3.connect('DB FOR BOT3.db', check_same_thread=False)
cursor = conn.cursor()


user = [372111586, 27390261]
admins = [372111586, 27390261]

bot = telebot.TeleBot(config.token)

def function(uid):
    for beta in admins:
        if uid==beta:
            return True
    else:
        return False

def function_1(userid):
    for beta in user:
        if userid==beta:
            return True
    else:
        return False

def message_send(u):
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
    if function(message.from_user.id):
        bot.send_message(message.chat.id,
                         "Вы являетесь админом и можете заносить новых пользователей с помощью команды /newperson.")



# Добавление пользователей
@bot.message_handler(commands=["newperson"])
def new(message):
    if function(message.from_user.id):
        msg = bot.send_message(message.chat.id, "New user name:")
        bot.register_next_step_handler(msg, new_user_name)

@bot.message_handler(regexp="1")
def right_1(message):
    if function(message.from_user.id):
        config.Rights = "1"
        msg = bot.send_message(message.chat.id, "ID:")
        cursor.execute("UPDATE Table_2 SET Rights='1' WHERE LastMessage='NEW'")
        conn.commit()
        bot.register_next_step_handler(msg, new_user_add)

@bot.message_handler(regexp="2")
def right_2(message):
    if function(message.from_user.id):
        config.Rights = "2"
        msg = bot.send_message(message.chat.id, "ID:")
        cursor.execute("UPDATE Table_2 SET Rights='2' WHERE LastMessage='NEW'")
        conn.commit()
        bot.register_next_step_handler(msg, new_user_add)

def new_user_name(message):
    bot.send_message(message.chat.id, "Rights(Админ-1, Обычный пользователь-2):")
    cursor.execute("INSERT INTO User(UserName,LastMessage) VALUES(%r,'NEW')" % (message.text))
    conn.commit()

def new_user_add(message):
    user.append(message.text)
    cursor.execute("UPDATE Table_2 SET UserID=%r, LastMessage=' ' WHERE LastMessage='NEW'" % (message.text))
    conn.commit()
    if config.Rights == "1":
        admins.append(message.text)
        config.Rights = "0"



# Развитие событий "Я на объекте"
@bot.message_handler(regexp="Я на объекте")
def handle_message(message):
    workup = types.ReplyKeyboardMarkup()
    button_New = types.KeyboardButton(text="Объект новый")
    buttion_old = types.KeyboardButton(text="Объект старый")
    workup.add(button_New, buttion_old)
    bot.send_message(message.chat.id, "На каком объекте?", reply_markup=workup)
    cursor.execute("INSERT INTO Table_2(UserID,Action,Message) VALUES(%s,'Я на объекте','Last')" % (str(message.chat.id)))

@bot.message_handler(regexp="Объект новый")
def handle_message_id(message):
    msg = bot.send_message(message.chat.id, "Напишите название объекта. Помните вы не можете иметь более 3-х объектов. Если вы хотите удалить объект напишите 'Я хочу удалить объект'")
    bot.register_next_step_handler(msg, object_obj)

@bot.message_handler(regexp="Объект старый")
def handle_message_id_2(message):
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    object_obj(b, c, d)
    if b != "0":
        buttion_one = types.KeyboardButton(b)
        maxup.add(buttion_one)
    if c != "0":
        buttion_two = types.KeyboardButton(c)
        maxup.add(buttion_two)
    if d != "0":
        buttion_three = types.KeyboardButton(d)
        maxup.add(buttion_three)
    msg = bot.send_message(message.chat.id, "Напишите название объекта на котором вы сейчас", reply_markup=maxup)
    bot.register_next_step_handler(msg, object_obj)

def object_obj(message, b="0", c="0", d="0"):
    if b == "0":
        b = message.text
    if b != "0":
        c = message.text
        if c != "0":
            d = message.text
    msg = bot.send_message(message.chat.id, "Что вы там делаете?")
    cursor.execute("UPDATE Table_2 SET PlaceProject = %r WHERE UserID=%s AND Message='Last'" % (message.text, str(message.chat.id)))
    bot.register_next_step_handler(msg, object_end)

def object_end(message):
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    cursor.execute("UPDATE Table_2 UserName=%r, Rights=%r, DateTime=%r, Action2=%r ,Message=' ' WHERE UserID=%s AND Message='Last'" %
                   (str(UserName_2), str(UserID_1), time.asctime(),message.text, str(message.chat.id)))
    conn.commit()
    bot.send_message(message.chat.id, "Я запомню это")



# Развитие событий "В лаборотории"
@bot.message_handler(regexp="Я в лаборотории")
def mess(message):
    work = types.ReplyKeyboardMarkup(row_width=1)
    buttion_new = types.KeyboardButton(text="Я занимаюсь чем-то новым")
    buttion_old = types.KeyboardButton(text="Я все еще работаю над одним из старых проектов")
    work.add(buttion_new, buttion_old)
    bot.send_message(message.chat.id, "Что вы там делаете?", reply_markup=work)
    cursor.execute("INSERT INTO Table_2(UserID,Action,Message) VALUES(%s,'Я в лаюоротории','Last')" % (str(message.chat.id)))
    conn.commit()

@bot.message_handler(regexp="Я занимаюсь чем-то новым")
def new(message):
    msg = bot.send_message(message.chat.id, "Напишите название проекта. Помните вы не можете иметь более 3-х проектов. Если вы хотите удалить проект напишите 'Я хочу удалить проект'")
    bot.register_next_step_handler(msg, project_pro)

@bot.message_handler(regexp="Я все еще работаю над одним из старых проектов")
def handle_message_id(message):
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    project_pro(e, f, g)
    if e != "0":
        buttion_one = types.KeyboardButton(e)
        maxup.add(buttion_one)
    if f != "0":
        buttion_two = types.KeyboardButton(f)
        maxup.add(buttion_two)
    if g != "0":
        buttion_three = types.KeyboardButton(g)
        maxup.add(buttion_three)
    msg = bot.send_message(message.chat.id, "Напишите, чем именно вы сейчас заняты", reply_markup=maxup)
    bot.register_next_step_handler(msg, project_pro)

def project_pro(message, e="0", f="0", g="0"):
    if e == "0":
        e = message.text
    if e != "0":
        f = message.text
        if f != "0":
            g = message.text
    msg = bot.send_message(message.chat.id, "Что вы там делаете?")
    cursor.execute("UPDATE Table_2 SET PlaceProject = %r WHERE UserID=%s AND Message='Last'" % (
    message.text, str(message.chat.id)))
    bot.register_next_step_handler(msg, project)

def project(message):
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    cursor.execute(
        "UPDATE Table_2 UserName=%r, Rights=%r, DateTime=%r, Action2=%r ,Message=' ' WHERE UserID=%s AND Message='Last'" %
        (str(UserName_2), str(UserID_1), time.asctime(), message.text, str(message.chat.id)))
    conn.commit()
    bot.send_message(message.chat.id, "Я запомню это")



# Реакция на "В дороге"
@bot.message_handler(regexp="Я в дороге")
def road_mess(message):
    msg = bot.send_message(message.chat.id, "Куда вы едете?")
    cursor.execute("INSERT INTO Table_2(UserID,Message) VALUES(%s,'Last')" % (str(message.chat.id)))
    conn.commit()
    bot.register_next_step_handler(msg, road_why)

def road(message):
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    bot.send_message(message.chat.id, "Я запомню это")
    cursor.execute("UPDATE Table_2 SET UserName=%r, Rights=%r, DateTime=%r, Action='Я в Дороге', Action2='В дороге', ForRoad=%r, Message='Not Last' WHERE UserID=%s AND Message='Last'" %
                    (str(UserName_2), str(UserID_1), time.asctime(), message.text, str(message.chat.id)))
    conn.commit()

def road_why(message):
    msg = bot.send_message(message.chat.id, "Зачем?")
    cursor.execute("UPDATE Table_2 SET PlaceProject=%r WHERE UserID=%s AND Message='Last'" % (message.text, str(message.chat.id)))
    conn.commit()
    bot.register_next_step_handler(msg, road)



# Реакция на "Другое"
@bot.message_handler(regexp="Другое")
def other(message):
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    cursor.execute("INSERT INTO Table_2(UserName,UserID, Rights, DateTime,Action,Message) VALUES(%r,%s,%r,%r,%r,'Last')" % (
    str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), message.text))
    msg = bot.send_message(message.chat.id, "Напишите.")
    bot.register_next_step_handler(msg, other_o)

def other_o(message):
    cursor.execute("UPDATE Table_2 SET Action2=%s ,Message=' ' WHERE UserID=%s AND Message='Last'" % (message.text, message.chat.id))
    conn.commit()
    bot.send_message(message.chat.id,"Я запомню это")



# Реакция на "Дома"
@bot.message_handler(regexp="Я дома")
def other(message):
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    action = message.text
    place = "0"
    cursor.execute("INSERT INTO Table_2 VALUES(%r,%i,%r,%r,%r,%r,%r,%r)" %
                   (str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), action, place, "Я дома", "0"))
    conn.commit()
    bot.send_message(message.chat.id, "Ок")



# Удаление проектов
@bot.message_handler(regexp="Я хочу удалить проект")
def delete(message):
    global jo
    jo = 1
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
    msg = bot.send_message(message.chat.id, "Выберите проект на удаление", reply_markup=maxup)
    bot.register_next_step_handler(msg, delete_project)

def delete_project(message):
    global e
    global f
    global g
    if message.text == e:
        e = f
        f = g
        g = "0"
    if message.text == f:
        f = g
        g = "0"
    if message.text == e:
        g = "0"



# Удаление объектов
@bot.message_handler(regexp="Я хочу удалить объект")
def delete(message):
    global jo
    jo = 1
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    if a != "0":
        buttion_one = types.KeyboardButton(b)
        maxup.add(buttion_one)
    if b != "0":
        buttion_two = types.KeyboardButton(c)
        maxup.add(buttion_two)
    if c != "0":
        buttion_three = types.KeyboardButton(d)
        maxup.add(buttion_three)
    msg = bot.send_message(message.chat.id, "Выберите объект на удаление", reply_markup=maxup)
    bot.register_next_step_handler(msg, delete_object)

def delete_object(message):
    global d
    global b
    global c
    if message.text == b:
        b = c
        c = d
        d = "0"
    if message.text == c:
        c = d
        d = "0"
    if message.text == d:
        d = "0"



if __name__ == '__main__':
    t = threading.Thread(target=message_send)
    t.start()
    bot.polling(none_stop=True)
