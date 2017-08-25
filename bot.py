#! /usr/bin/env python
# -*- coding: utf-8 -*-
from time_thread import *
import time
import config
from config import *
import telebot
from telebot import types
import sqlite3
import threading
import datetime

def connect():
    connection = sqlite3.connect('DB FOR BOT.db', check_same_thread=False)
    return connection


user = []
admins = [372111586, 27390261]
but=[372111586]
but_p=[372111586]

bot = telebot.TeleBot(config.token)
def function(uid):
    for beta in admins:
        if uid == beta:
            return True
    else:
        return False

def function_1(userid):
    for beta in user:
        if userid == beta:
            return True
    else:
        return False
    


# Реакция на комманду /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте! Я бот для отчетов, каждый день нещадно с 9 утра спамить вас запросами "
                     "об отчетах покуда вы не ответите. Вы сами на это подписались! "
                     "Надеюсь наша работа с вами будет успешной.")
    if function(message.chat.id):
        bot.send_message(message.chat.id,
                         "Вы являетесь админом и можете давать пользователям права админов с помощью комманды /newadmin.")
    add_user(message)
        

def add_user(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("SELECT UserID FROM User WHERE UserID=%s" % (int(message.chat.id)))
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO User (UserName,UserID,LastMessage) VALUES(%r,%r,%i)" % (str(message.chat.first_name), str(message.chat.id),1))
        conn.commit()
        cursor.close()
        connect.close()
        


def buttion(beta):
    make = types.ReplyKeyboardMarkup()
    buttion_1 = types.KeyboardButton(text="Я на объекте")
    buttion_2 = types.KeyboardButton(text="Я в дороге")
    buttion_3 = types.KeyboardButton(text="Я дома")
    buttion_4 = types.KeyboardButton(text="Я в лаборотории")
    buttion_5 = types.KeyboardButton(text="Другое")
    make.add(buttion_1, buttion_2, buttion_3, buttion_4, buttion_5)
    bot.send_message(row, "Где вы или чем заняты?", reply_markup=make)

# Добавление пользователей
@bot.message_handler(commands=["newadmin"])
def new(message):
    if function(message.from_user.id):
        msg = bot.send_message(message.chat.id, "ID:")
        bot.register_next_step_handler(msg, new_user_name)

def new_user_name(message):
    bot.send_message(message.chat.id, "Пользователь отныне администратор")
    bot.send_message(int(message.text),
                         "Вы являетесь админом и можете давать пользователям права админов с помощью комманды /newadmin.")
    admins.append(int(message.text))



# Развитие событий "Я на объекте"
@bot.message_handler(regexp="Я на объекте")
def handle_message(message):
    workup = types.ReplyKeyboardMarkup()
    workup.add('Объект новый', 'Объект старый')
    bot.send_message(message.chat.id, "На каком объекте?", reply_markup=workup)
    cursor.execute("INSERT INTO Table_2(UserID,Action,Message) VALUES(%s,'Я на объекте','Last')" % (int(message.chat.id)))
    conn.commit()

@bot.message_handler(regexp="Объект новый")
def handle_message_id(message):
    msg = bot.send_message(message.chat.id, "Напишите название объекта. Если вы хотите удалить объект напишите 'Я хочу удалить объект'")
    bot.register_next_step_handler(msg, object_obj_2)

@bot.message_handler(regexp="Объект старый")
def answer_text(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("SELECT Buttion FROM UserButtion WHERE UserID=%i AND OP='O'" % (message.chat.id))
    [results] = cursor.fetchone()
    cursor.close()
    connect.close()
    user_markup = types.ReplyKeyboardMarkup()
    for beta in but:
        user_markup.row(str(results))
    msg = bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    bot.register_next_step_handler(msg, object_obj)

def object_end(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UseName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    cursor.execute("UPDATE Table_2 SET UserName=%r, Rights=%r, DateTime=%r, Action2=%r ,Message=' ' WHERE UserID=%s AND Message='Last'" %
                   (str(UseName_2), str(UserID_1), time.asctime(), message.text, int(message.chat.id)))
    conn.commit()
    cursor.close()
    connect.close()
    bot.send_message(message.chat.id, "Я запомню это")

def object_obj(message):
    connect = connect()
    cursor = connect.cursor()
    msg = bot.send_message(message.chat.id, "Что вы там делаете?")
    bot.register_next_step_handler(msg, object_end)
    cursor.execute("UPDATE Table_2 SET PlaceProject = %r WHERE UserID=%s AND Message='Last'" %
                   (str(message.text), int(message.chat.id)))
    conn.commit()
    connect.close()

def object_obj_2(message):
    connect = connect()
    cursor = connect.cursor()
    msg = bot.send_message(message.chat.id, "Что вы там делаете?")
    bot.register_next_step_handler(msg, object_end)
    but.append(message.chat.id)
    cursor.execute("INSERT INTO UserButtion VALUES(%s,'O',%r)" % (int(message.chat.id), message.text))
    cursor.execute("UPDATE Table_2 SET PlaceProject = %r WHERE UserID=%s AND Message='Last'" %
                   (message.text, int(message.chat.id)))
    conn.commit()
    cursor.close()
    connect.close()




# Развитие событий "В лаборотории"
@bot.message_handler(regexp="Я в лаборатории")
def mess(message):
    work = types.ReplyKeyboardMarkup(row_width=1)
    buttion_new = types.KeyboardButton(text="Я занимаюсь чем-то новым")
    buttion_old = types.KeyboardButton(text="Я все еще работаю над одним из старых проектов")
    work.add(buttion_new, buttion_old)
    connect = connect()
    cursor = connect.cursor()
    bot.send_message(message.chat.id, "Что вы там делаете?", reply_markup=work)
    cursor.execute("INSERT INTO Table_2(UserID,Action,Message) VALUES(%s,'Я в лаюоротории','Last')" % (int(message.chat.id)))
    conn.commit()
    cursor.close()
    connect.close()

@bot.message_handler(regexp="Я занимаюсь чем-то новым")
def new(message):
    msg = bot.send_message(message.chat.id, "Напишите название проекта. Если вы хотите удалить проект напишите 'Я хочу удалить проект'")
    bot.register_next_step_handler(msg, project_pro_2)

@bot.message_handler(regexp="Я все еще работаю над одним из старых проектов")
def handle_message_id(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("SELECT Buttion FROM UserButtion WHERE UserID=%i AND OP='P'" % (message.chat.id))
    [results] = cursor.fetchone()
    cursor.close()
    maxup = types.ReplyKeyboardMarkup()
    for beta in but:
        maxup.row(str(results))
    msg = bot.send_message(message.chat.id, "Напишите, чем именно вы сейчас заняты", reply_markup=maxup)
    cursor.close()
    connect.close()
    bot.register_next_step_handler(msg, project_pro)

def project_pro(message):
    msg = bot.send_message(message.chat.id, "Что вы там делаете?")
    connect = connect()
    cursor = connect.cursor()
    bot.register_next_step_handler(msg, object_end)
    cursor.execute("UPDATE Table_2 SET PlaceProject = %r WHERE UserID=%s AND Message='Last'" %
                   (str(message.text), int(message.chat.id)))
    conn.commit()
    cursor.close()
    connect.close()


def project_pro_2(message):
    msg = bot.send_message(message.chat.id, "Что вы там делаете?")
    bot.register_next_step_handler(msg, object_end)
    connect = connect()
    cursor = connect.cursor()
    but_p.append(message.chat.id)
    cursor.execute("INSERT INTO UserButtion VALUES(%s,'P',%r)" % (int(message.chat.id), str(message.text)))
    cursor.execute("UPDATE Table_2 SET PlaceProject = %r WHERE UserID=%s AND Message='Last'" %
                   (message.text, int(message.chat.id)))
    conn.commit()
    cursor.close()
    connect.close()


def project(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    cursor.execute(
        "UPDATE Table_2 UserName=%r, Rights=%r, DateTime=%r, Action2=%r ,Message=' ' WHERE UserID=%s AND Message='Last'" %
        (str(UserName_2), str(UserID_1), time.asctime(), message.text, int(message.chat.id)))
    conn.commit()
    cursor.close()
    connect.close()
    bot.send_message(message.chat.id, "Я запомню это")



# Реакция на "В дороге"
@bot.message_handler(regexp="Я в дороге")
def road_mess(message):
    connect = connect()
    cursor = connect.cursor()
    msg = bot.send_message(message.chat.id, "Куда вы едете?")
    cursor.execute("INSERT INTO Table_2(UserID,Message) VALUES(%s,'Last')" % (int(message.chat.id)))
    conn.commit()
    cursor.close()
    connect.close()
    bot.register_next_step_handler(msg, road_why)

def road(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    bot.send_message(message.chat.id, "Я запомню это")
    cursor.execute("UPDATE Table_2 SET UserName=%r, Rights=%r, DateTime=%r, Action='Я в Дороге', Action2='В дороге', ForRoad=%r, Message='Not Last' WHERE UserID=%s AND Message='Last'" %
                    (str(UserName_2), str(UserID_1), time.asctime(), message.text, int(message.chat.id)))
    conn.commit()
    cursor.close()
    connect.close()

def road_why(message):
    connect = connect()
    cursor = connect.cursor()
    msg = bot.send_message(message.chat.id, "Зачем?")
    cursor.execute("UPDATE Table_2 SET PlaceProject=%r WHERE UserID=%s AND Message='Last'" % (message.text, int(message.chat.id)))
    conn.commit()
    cursor.close()
    connect.close()
    bot.register_next_step_handler(msg, road)



# Реакция на "Другое"
@bot.message_handler(regexp="Другое")
def other(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    cursor.execute("INSERT INTO Table_2(UserName,UserID, Rights, DateTime,Action,Message) VALUES(%r,%s,%r,%r,%r,'Last')" % (str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), message.text))
    cursor.close()
    connect.close()
    msg = bot.send_message(message.chat.id, "Напишите.")
    bot.register_next_step_handler(msg, other_o)

def other_o(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("UPDATE Table_2 SET Action2=%r, Message=' ' WHERE UserID=%s AND Message='Last'" % (message.text, message.chat.id))
    conn.commit()
    cursor.close()
    connect.close()
    bot.send_message(message.chat.id,"Я запомню это")



# Реакция на "Дома"
@bot.message_handler(regexp="Я дома")
def other(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserName_2 = cursor.fetchall()
    cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
    UserID_1 = cursor.fetchall()
    action = message.text
    place = "0"
    cursor.execute("INSERT INTO Table_2 VALUES(%r,%i,%r,%r,%r,%r,%r,%r,%r)" %
                   (str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), action, place, "Я дома", "",""))
    conn.commit()
    cursor.close()
    connect.close()
    bot.send_message(message.chat.id, "Ок")



# Удаление проектов
@bot.message_handler(regexp="Я хочу удалить проект")
def delete(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("SELECT Buttion FROM UserButtion WHERE UserID=%i AND OP='P'" % (int(message.chat.id)))
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    for message.chat.id in but_p:
        maxup.add(cursor.fetchone())
    cursor.close()
    connect.close()
    msg = bot.send_message(message.chat.id, "Выберите проект на удаление", reply_markup=maxup)
    bot.register_next_step_handler(msg, delete_project)

def delete_project(message):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM UserButtion WHERE UserID=%i AND Buttion=%s" % (int(message.chat.id), message.text))



# Удаление объектов
@bot.message_handler(regexp="Я хочу удалить объект")
def delete(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("SELECT Buttion FROM UserButtion WHERE UserID=%i AND OP='P'" % (int(message.chat.id)))
    maxup = types.ReplyKeyboardMarkup(row_width=1)
    for message.chat.id in but:
        maxup.add(cursor.fetchone())
    cursor.close()
    connect.close()
    msg = bot.send_message(message.chat.id, "Выберите объект на удаление", reply_markup=maxup)
    bot.register_next_step_handler(msg, delete_object)


def delete_object(message):
    connect = connect()
    cursor = connect.cursor()
    cursor.execute("DELETE FROM UserButtion WHERE UserID=%i AND Buttion=%s" % (int(message.chat.id), message.text))
    cursor.close()
    connect.close()

e1 = threading.Event()

if __name__ == '__main__':
    t = threading.Thread(target=message_send)
    t.start()
    e1.set()
    bot.polling(none_stop=True)
