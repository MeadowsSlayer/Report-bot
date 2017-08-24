from bot import *


def message_send():
	a=0
	while True:
		cursor = conn.cursor()
		cursor.execute('SELECT UserID FROM User ORDER BY Rights LIMIT 100')
		result = cursor.fetchone()
		now_time = datetime.datetime.now()
		if (now_time.hour == 9) or (now_time.hour == 13) or (now_time.hour == 18):
			for beta in result:
				print(beta)
				buttion(beta)                                            
				cursor.close()
				time.sleep(3600)
