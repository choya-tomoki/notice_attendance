# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response
import socket
import trollius as asyncio
from trollius import From
import pickle
from threading import Thread
import time

from Camera import Camera


app = Flask(__name__)

#index.htmlを返す
@app.route('/')
def index():
    return render_template('index.html')

#カメラ映像を配信する
@asyncio.coroutine
@app.route('/video')
def video():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#カメラオブジェクトから静止画を取得する
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def build_server():
    host = "" # TODO server ip adress
    port = 8478 # TODO number of port
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind((host,port))
    serversock.listen(10) 
    print 'Waiting for connections...'
    clientsock, client_address = serversock.accept()
    return clientsock

# @asyncio.coroutine
def slackServer(sock, camera):
    while True:
        print "waiting recv"
        rcvmsg = sock.recv(1024)
        purpose = rcvmsg.split(" ")[0]
        print 'Received -> %s' % (rcvmsg)
        if rcvmsg == '':
            break
        can_bye = None
        if purpose == "delete":
            camera.delete(rcvmsg.split(" ")[1])
        elif purpose == "add":
            camera.add(rcvmsg.split(" ")[1])
        elif purpose == "bye":
            can_bye = camera.bye(rcvmsg.split(" ")[1])
            
        
        if can_bye == None:
            s_msg = pickle.dumps(camera.attendance)
        else:
            s_msg = can_bye
        if s_msg == '':
            break
        
        sock.sendall(s_msg)
    sock.close()

def asyloop(loop, sock, camera):
    asyncio.set_event_loop(loop)
    tasks = [
        # asyncio.async(video()),
        asyncio.async(slackServer(sock, camera)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))

#カメラスレッドを生成してFlaskを起動する
if __name__ == '__main__':
    threaded=True
    clientsock = build_server()
    # video()　　# ブラウザで動画をリアルアイムで確認する用
    # loop = asyncio.new_event_loop()
    # p = Thread(target=asyloop, args=(loop, clientsock, Camera()))
    p = Thread(target=slackServer, args=(clientsock, Camera()))
    p.start()
    app.run(host="0.0.0.0",port=80)
