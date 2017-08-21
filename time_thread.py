from bot import *


def message_send():
	a=0
	while True:
		cursor = conn.cursor()
		cursor.execute("SELECT UserID FROM User")
		result = cursor.fetchone()
		cursor.close()
		now_time = datetime.datetime.now()
		if (now_time.hour == 9) or (now_time.hour == 15 and now_time.minute == 18) or (now_time.hour == 18):
			if a == 0:
				for beta in user:
					buttion(beta)
					a=1
		if (now_time.hour == 11 and now_time.minute == 47) or (now_time.hour == 10) or (now_time.hour == 14) or (now_time.hour == 19):
			if a == 1:
				a=0

e1 = threading.Event()


if __name__ == '__main__':
    t = threading.Thread(target=message_send, args=(buttions, e1))
    t.start()
    e1.set()
