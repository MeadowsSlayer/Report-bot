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
admins = [372111586, 27390261,167315364]
but=[372111586]
but_p=[372111586]

bot = telebot.TeleBot(config.token)




class BotModel:
    def __init__(self, message, parent = None):
        self.text = message.text
        self.chat_id = message.from_user.id
        self.name = message.from_user.first_name

    def function(uid):
        for beta in admins:
            if uid == beta:
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
        if BotModel.function(message.chat.id):
            bot.send_message(message.chat.id,
                             "Вы являетесь админом и можете давать пользователям права админов с помощью комманды /newadmin.")
        BotController.add_user(message)

    def delete_object(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("DELETE FROM UserButtion WHERE UserID=%i AND Buttion=%r" % (int(message.chat.id), str(message.text)))
        cursor.close()
        connects.close()
        bot.send_message(message.chat.id , "Объект удален")
    
    def new_user_name(message):
        bot.send_message(message.chat.id, "Пользователь отныне администратор")
        bot.send_message(int(message.text),
                             "Вы являетесь админом и можете давать пользователям права админов с помощью комманды /newadmin.")
        admins.append(int(message.text))

    def object_end(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
        UseName_2 = cursor.fetchall()
        cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
        UserID_1 = cursor.fetchall()
        cursor.execute("UPDATE Table_2 SET UserName=%r, Rights=%r, DateTime=%r, Action2=%r ,Message=' ' WHERE UserID=%s AND Message='Last'" %
                       (str(UseName_2), str(UserID_1), time.asctime(), message.text, int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()
        bot.send_message(message.chat.id, "Я запомню это")

    def object_obj(message):
        connects = connect()
        cursor = connects.cursor()
        msg = bot.send_message(message.chat.id, "Что вы там делаете?")
        bot.register_next_step_handler(msg, BotModel.object_end)
        cursor.execute("UPDATE Table_2 SET PlaceProject = %r WHERE UserID=%s AND Message='Last'" %
                       (str(message.text), int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()
        

    def object_obj_2(message):
        connects = connect()
        cursor = connects.cursor()
        msg = bot.send_message(message.chat.id, "Что вы там делаете?")
        bot.register_next_step_handler(msg, BotModel.object_end)
        but.append(message.chat.id)
        cursor.execute("INSERT INTO UserButtion VALUES(%s,'O',%r)" % (int(message.chat.id), message.text))
        cursor.execute("UPDATE Table_2 SET PlaceProject = %r WHERE UserID=%s AND Message='Last'" %
                       (message.text, int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()

    def project_pro(message):
        msg = bot.send_message(message.chat.id, "Над чем вы работаете?")
        connects = connect()
        cursor = connects.cursor()
        bot.register_next_step_handler(msg, BotModel.object_end)
        cursor.execute("UPDATE Table_2 SET PlaceProject = %r WHERE UserID=%s AND Message='Last'" %
                       (str(message.text), int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()


    def project_pro_2(message):
        msg = bot.send_message(message.chat.id, "Что именно вы делаете?")
        bot.register_next_step_handler(msg, BotModel.object_end)
        connects = connect()
        cursor = connects.cursor()
        but_p.append(message.chat.id)
        cursor.execute("INSERT INTO UserButtion VALUES(%s,'P',%r)" % (int(message.chat.id), str(message.text)))
        cursor.execute("UPDATE Table_2 SET PlaceProject = %r WHERE UserID=%s AND Message='Last'" %
                       (message.text, int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()


    def project(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
        UserName_2 = cursor.fetchall()
        cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
        UserID_1 = cursor.fetchall()
        cursor.execute(
            "UPDATE Table_2 UserName=%r, Rights=%r, DateTime=%r, Action2=%r ,Message=' ' WHERE UserID=%s AND Message='Last'" %
            (str(UserName_2), str(UserID_1), time.asctime(), message.text, int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()
        bot.send_message(message.chat.id, "Я запомню это")

    def road(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
        UserName_2 = cursor.fetchall()
        cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
        UserID_1 = cursor.fetchall()
        bot.send_message(message.chat.id, "Я запомню это")
        cursor.execute("UPDATE Table_2 SET UserName=%r, Rights=%r, DateTime=%r, Action='Я в Дороге', Action2='В дороге', ForRoad=%r, Message='Not Last' WHERE UserID=%s AND Message='Last'" %
                        (str(UserName_2), str(UserID_1), time.asctime(), message.text, int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()

    def road_why(message):
        connects= connect()
        cursor = connects.cursor()
        cursor.execute("UPDATE Table_2 SET PlaceProject=%r WHERE UserID=%s AND Message='Last'" % (message.text, int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()
        msg = bot.send_message(message.chat.id, "Зачем?")
        bot.register_next_step_handler(msg, BotModel.road)

    def other_o(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("UPDATE Table_2 SET Action2=%r, Message=' ' WHERE UserID=%s AND Message='Last'" % (message.text, message.chat.id))
        connects.commit()
        cursor.close()
        connects.close()
        bot.send_message(message.chat.id,"Я запомню это")

    def delete_project(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("DELETE FROM UserButtion WHERE UserID=%i AND Buttion=%r" % (int(message.chat.id), str(message.text)))
        connects.commit()
        cursor.close()
        connects.close()
        bot.send_message(message.chat.id , "Проект удален")




class BotView:
    def __init__( self, inController, inModel, parent = None ):
        self.mController = inController
        self.mModel = inModel




class BotController:
    def __init__(self,inModel,message, chater,parent = None):
        self.mModel = inModel
        self.chat_id = message
        self.cha = chater

    def add_user(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("SELECT UserID FROM User WHERE UserID=%s" % (int(message.chat.id)))
        result = cursor.fetchone()
        cursor.close()
        connects.close()
        if result is None:
            connects = connect()
            cursor = connects.cursor()
            cursor.execute("INSERT INTO User (UserName,UserID,LastMessage) VALUES(%r,%r,%i)" % (str(message.chat.first_name), str(message.chat.id),1))
            connects.commit()
            cursor.close()
            connects.close()

    # Удаление объектов
    @bot.message_handler(regexp="Я хочу удалить объект")
    def delete(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("SELECT Buttion FROM UserButtion WHERE UserID=%i AND OP='O'" % (int(message.chat.id)))
        if cursor.fetchone() is not None:
            [results] = cursor.fetchone()
        maxup = types.ReplyKeyboardMarkup(row_width=1)
        for message.chat.id in but:
            maxup.row(str(results))
        cursor.close()
        connects.close()
        msg = bot.send_message(message.chat.id, "Выберите объект на удаление", reply_markup=maxup)
        bot.register_next_step_handler(msg, BotModel.delete_object)    

    # Добавление пользователей
    @bot.message_handler(commands=["newadmin"])
    def new(message):
        if BotModel.function(message.from_user.id):
            msg = bot.send_message(message.chat.id, "ID:")
            bot.register_next_step_handler(msg, BotModel.new_user_name)

    # Развитие событий "Я на объекте"
    @bot.message_handler(regexp="Я на объекте")
    def handle_message(message):
        connects = connect()
        cursor = connects.cursor()
        workup = types.ReplyKeyboardMarkup()
        workup.add('Объект новый', 'Я уже записывал этот объект')
        bot.send_message(message.chat.id, "На каком объекте?", reply_markup=workup)
        cursor.execute("INSERT INTO Table_2(UserID,Action,Message) VALUES(%s,'Я на объекте','Last')" % (int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()

    @bot.message_handler(regexp="Объект новый")
    def handle_message_id(message):
        msg = bot.send_message(message.chat.id, "Напишите название объекта. Если вы хотите удалить объект напишите 'Я хочу удалить объект'")
        bot.register_next_step_handler(msg, BotModel.object_obj_2)

    @bot.message_handler(regexp="Я уже записывал этот объект")
    def answer_text(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("SELECT Buttion FROM UserButtion WHERE UserID=%i AND OP='O'" % (message.chat.id))
        if cursor.fetchone() is not None:
            [results] = cursor.fetchone()
        cursor.close()
        connects.close()
        user_markup = types.ReplyKeyboardMarkup()
        for beta in but:
            user_markup.row(str(results))
        msg = bot.send_message(message.from_user.id, "Укажите какой это объект", reply_markup=user_markup)
        bot.register_next_step_handler(msg, BotModel.object_obj)

    # Развитие событий "В лаборотории"
    @bot.message_handler(regexp="Я в лаборатории")
    def mess(message):
        work = types.ReplyKeyboardMarkup(row_width=1)
        buttion_new = types.KeyboardButton(text="Я занимаюсь чем-то новым")
        buttion_old = types.KeyboardButton(text="Я все еще работаю над одним из старых проектов")
        work.add(buttion_new, buttion_old)
        connects = connect()
        cursor = connects.cursor()
        bot.send_message(message.chat.id, "Что вы там делаете?", reply_markup=work)
        cursor.execute("INSERT INTO Table_2(UserID,Action,Message) VALUES(%s,'Я в лаюоротории','Last')" % (int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()

    @bot.message_handler(regexp="Я занимаюсь чем-то новым")
    def new(message):
        msg = bot.send_message(message.chat.id, "Напишите название проекта. Если вы хотите удалить проект напишите 'Я хочу удалить проект'")
        bot.register_next_step_handler(msg, BotModel.project_pro_2)

    @bot.message_handler(regexp="Я все еще работаю над одним из старых проектов")
    def handle_message_id(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("SELECT Buttion FROM UserButtion WHERE UserID=%i AND OP='P'" % (message.chat.id))
        [results] = cursor.fetchone()
        cursor.close()
        maxup = types.ReplyKeyboardMarkup()
        for beta in but:
            maxup.row(str(results))
        msg = bot.send_message(message.chat.id, "Напишите, чем именно вы сейчас заняты", reply_markup=maxup)
        cursor.close()
        connects.close()
        bot.register_next_step_handler(msg, BotModel.project_pro)

    # Реакция на "В дороге"
    @bot.message_handler(regexp="Я в дороге")
    def road_mess(message):
        connects = connect()
        cursor = connects.cursor()
        msg = bot.send_message(message.chat.id, "Куда вы едете?")
        cursor.execute("INSERT INTO Table_2(UserID,Message) VALUES(%s,'Last')" % (int(message.chat.id)))
        connects.commit()
        cursor.close()
        connects.close()
        bot.register_next_step_handler(msg, BotModel.road_why)

    # Реакция на "Другое"
    @bot.message_handler(regexp="Другое")
    def other(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
        UserName_2 = cursor.fetchall()
        cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
        UserID_1 = cursor.fetchall()
        cursor.execute("INSERT INTO Table_2(UserName,UserID, Rights, DateTime,Action,Message) VALUES(%r,%s,%r,%r,%r,'Last')" % (str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), message.text))
        cursor.close()
        connects.close()
        msg = bot.send_message(message.chat.id, "Напишите.")
        bot.register_next_step_handler(msg, BotModel.other_o)

    # Реакция на "Дома"
    @bot.message_handler(regexp="Я дома")
    def other(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("SELECT UserName FROM User WHERE UserID = %i" % (int(message.chat.id)))
        UserName_2 = cursor.fetchall()
        cursor.execute("SELECT Rights FROM User WHERE UserID = %i" % (int(message.chat.id)))
        UserID_1 = cursor.fetchall()
        action = message.text
        place = "0"
        cursor.execute("INSERT INTO Table_2 VALUES(%r,%i,%r,%r,%r,%r,%r,%r,%r)" %
                       (str(UserName_2), message.chat.id, str(UserID_1), time.asctime(), action, place, "Я дома", "",""))
        connects.commit()
        cursor.close()
        connects.close()
        bot.send_message(message.chat.id, "Ок")

    # Удаление проектов
    @bot.message_handler(regexp="Я хочу удалить проект")
    def delete(message):
        connects = connect()
        cursor = connects.cursor()
        cursor.execute("SELECT Buttion FROM UserButtion WHERE UserID=%i AND OP='P'" % (int(message.chat.id)))
        maxup = types.ReplyKeyboardMarkup(row_width=1)
        if cursor.fetchone() is not None:
            [results] = cursor.fetchone()
        for message.chat.id in but_p:
            maxup.row(str(results))
        cursor.close()
        connects.close()
        msg = bot.send_message(message.chat.id, "Выберите проект на удаление", reply_markup=maxup)
        bot.register_next_step_handler(msg, BotModel.delete_project)

e1 = threading.Event()

if __name__ == '__main__':
    t = threading.Thread(target=message_send)
    t.start()
    e1.set()
    bot.polling(none_stop=True)
