# simple_Server.py

import socket
import thread

HOST = 'localhost'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket open
s.bind( (HOST, PORT) ) # .bind?
s.listen(1) # s를 읽겠다.

conn, addr = s.accept()
print('Connected by', addr)
data = ''\

def pr_msg() :
    while 1 :
        data = conn.recv(1024)
        if data :
            print(data.upper())

thread.start_new_thread( pr_msg, () )

while 1:
    send_data = raw_input()
    if send_data[:4] in ['quit', 'Quit', 'QUIT']:
        conn.send('Server Quit')
        thread.exit()
        conn.close()
    conn.send('Server : ' + send_data)
    
