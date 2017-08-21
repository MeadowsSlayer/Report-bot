from ff import *


def message_send():
    now_time = datetime.datetime.now()
    while True:
        if now_time.hour == 19 and now_time.minute == 9:
            for beta in user:
                buttions(beta)

e1 = threading.Event()


if __name__ == '__main__':
    t = threading.Thread(target=message_send, args=(buttions, e1))
    t.start()
    e1.set()
