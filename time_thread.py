from bot import *


def message_send():
	a=0
	while True:
		cursor = conn.cursor()
		cursor.execute("SELECT UserID FROM User ORDER BY UserID")
		result = cursor.fetchone()
		results = cursor.fetchall()
		conn.commit()
		cursor.close()
		now_time = datetime.datetime.now()
		if (now_time.hour == 9) or (now_time.hour == 13) or (now_time.hour == 18):
			if a==0:
				for beta in result:
					buttion(beta)
					print(results)
					a=1
		if (now_time.hour == 10) or (now_time.hour == 14) or (now_time.hour == 19):
			a=0
