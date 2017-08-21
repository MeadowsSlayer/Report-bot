from ff import *


def message_send():
    while True:
        now_time = datetime.datetime.now()
        if (now_time.hour == 10 and now_time.minute == 24) or (now_time.hour == 9) or (now_time.hour == 13) or (now_time.hour == 18):
            for beta in user:
                buttions(beta)

e1 = threading.Event()


if __name__ == '__main__':
    t = threading.Thread(target=message_send, args=(buttions, e1))
    t.start()
    e1.set()
