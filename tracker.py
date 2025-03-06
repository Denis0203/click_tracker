from datetime import datetime,timedelta
import time
from pynput import mouse

actions = []

def on_move(x,y):
    actions.append(1)

def on_click(x,y,button, pressed):
    actions.append(1)

def on_scroll(x,y, dx, dy):
    actions.append(1)

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener_mode = 0
while True:
    # Получаем текущее время
    start = datetime.now()
    if listener_mode == 0:
        listener.start()
        listener_mode = 1
    time.sleep(5)
    end = datetime.now()
    with open('c.txt','a') as f:
            if len(actions) != 0:
                f.write(start.strftime("%Y-%m-%d %H:%M:%S") +","+ end.strftime("%Y-%m-%d %H:%M:%S"+","+str(len(actions))+'\n'))
                #f.write("Начало минуты" + start.strftime("%Y-%m-%d %H:%M:%S") +" Конец минуты "+ end.strftime("%Y-%m-%d %H:%M:%S"+" "+str(len(actions))+'\n'))
            else:
                f.write(start.strftime("%Y-%m-%d %H:%M:%S") +","+ end.strftime("%Y-%m-%d %H:%M:%S"+","+'0'+'\n'))
                #f.write("Начало минуты" + start.strftime("%Y-%m-%d %H:%M:%S") +" Конец минуты "+ end.strftime("%Y-%m-%d %H:%M:%S")+' 0'+'\n')
    actions = []












    # if start.strftime("%Y-%m-%d %H:%M:%S")[-2:] == '00':
    #     actions = []
    #     print("Начало минуты", start)
    #     time.sleep(1)
    #     while datetime.now()<start + timedelta(seconds=59):
    #         if listener_mode == 0:
    #             listener.start()
    #             listener_mode = 1
    #     end = datetime.now()
    #     print("Конец минуты", end)
    #     print(len(actions))
        
        