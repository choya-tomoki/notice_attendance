# -*- coding: utf-8 -*-
from slackbot.bot import listen_to, respond_to
import datetime
import socket
import pickle


host = "192.168.207.176"
port = 8478
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

@respond_to('誰')
@respond_to('出欠確認')
@respond_to('登校状況')
@respond_to('全員')
@listen_to('誰')
@listen_to('出欠確認')
@listen_to('登校状況')
@listen_to('全員')
def listen_func_all(message):
    print("called all出欠確認")
    massage = "check all attendance"
    attendance = b''
    today = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')

    client.send(massage.encode('utf-8')) 

    msg = client.recv(4096)
    attendance += msg
    attendance = pickle.loads(attendance)
    message.send('{0}現在の登校状況\n{1}'.format(today, ", ".join(attendance)))

@respond_to('D3')
@respond_to('D３')
@listen_to('D3')
@listen_to('D３')
def listen_func_d3(message):
    print("called d3出欠確認")
    massage = "check D3 attendance"
    attendance = b''
    today = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    D3_attendance = []

    client.send(massage.encode('utf-8')) 

    msg = client.recv(4096)
    attendance += msg
    attendance = pickle.loads(attendance)
    for p in attendance:
        if "D3" in p:
            D3_attendance.append(p)
    message.send('{0}現在のD3の登校状況\n{1}'.format(today, ", ".join(D3_attendance)))

@respond_to('D2')
@respond_to('D２')
@listen_to('D2')
@listen_to('D２')
def listen_func_d2(message):
    print("called d2出欠確認")
    massage = "check D2 attendance"
    attendance = b''
    today = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    D2_attendance = []

    client.send(massage.encode('utf-8')) 

    msg = client.recv(4096)
    attendance += msg
    attendance = pickle.loads(attendance)
    for p in attendance:
        if "D2" in p:
            D2_attendance.append(p)
    message.send('{0}現在のD2の登校状況\n{1}'.format(today, ", ".join(D2_attendance)))

@respond_to('D1')
@respond_to('D１')
@listen_to('D1')
@listen_to('D１')
def listen_func_d1(message):
    print("called d1出欠確認")
    massage = "check M1 attendance"
    attendance = b''
    today = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    D1_attendance = []

    client.send(massage.encode('utf-8')) 

    msg = client.recv(4096)
    attendance += msg
    attendance = pickle.loads(attendance)
    for p in attendance:
        if "D1" in p:
            D1_attendance.append(p)
    message.send('{0}現在のD1の登校状況\n{1}'.format(today, ", ".join(D1_attendance)))

@respond_to('M2')
@respond_to('M２')
@listen_to('M2')
@listen_to('M２')
def listen_func_m2(message):
    print("called m2出欠確認")
    massage = "check M1 attendance"
    attendance = b''
    today = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    M2_attendance = []

    client.send(massage.encode('utf-8')) 

    msg = client.recv(4096)
    attendance += msg
    attendance = pickle.loads(attendance)
    for p in attendance:
        if "M2" in p:
            M2_attendance.append(p)
    message.send('{0}現在のM2の登校状況\n{1}'.format(today, ", ".join(M2_attendance)))

@respond_to('M1')
@respond_to('M１')
@listen_to('M1')
@listen_to('M１')
def listen_func_m1(message):
    print("called M1出欠確認")
    send_massage = "check M1 attendance"
    attendance = b''
    today = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    M1_attendance = []

    client.send(send_massage.encode('utf-8')) 

    msg = client.recv(4096)
    attendance += msg
    attendance = pickle.loads(attendance)
    for p in attendance:
        if "M1" in p:
            M1_attendance.append(p)
    message.send('{0}現在のM1の登校状況\n{1}'.format(today, ", ".join(M1_attendance)))

@respond_to('B4')
@respond_to('B４')
@listen_to('B4')
@listen_to('B４')
def listen_func_b4(message):
    print("called b4出欠確認")
    send_massage = "check M1 attendance"
    attendance = b''
    today = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    B4_attendance = []

    client.send(send_massage.encode('utf-8')) 

    msg = client.recv(4096)
    attendance += msg
    attendance = pickle.loads(attendance)
    for p in attendance:
        if "B4" in p:
            B4_attendance.append(p)
    message.send('{0}現在のB4の登校状況\n{1}'.format(today, ", ".join(B4_attendance)))

@respond_to('B3')
@respond_to('B３')
@listen_to('B3')
@listen_to('B３')
def listen_func_b3(message):
    print("called b3出欠確認")
    send_massage = "check M1 attendance"
    attendance = b''
    today = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    B3_attendance = []

    client.send(send_massage.encode('utf-8')) 

    msg = client.recv(4096)
    attendance += msg
    attendance = pickle.loads(attendance)
    for p in attendance:
        if "B3" in p:
            B3_attendance.append(p)
    message.send('{0}現在のB3の登校状況\n{1}'.format(today, ", ".join(B3_attendance)))

@respond_to('はいません')
@respond_to('は居ません')
@listen_to('はいません')
@listen_to('は居ません')
def listen_func_miss1(message):
    print("called miss1")
    attendance = b''
    today = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    text = message.body['text']
    p = text.split("は")[0]
    send_massage = "delete {}".format(p)

    client.send(send_massage.encode('utf-8')) 

    msg = client.recv(4096)
    message.send('失礼しました')
    attendance += msg
    attendance = pickle.loads(attendance)
    message.send('{0}現在の登校状況\n{1}'.format(today, ", ".join(attendance)))

@respond_to('もいます')
@respond_to('も居ます')
@listen_to('もいます')
@listen_to('も居ます')
def listen_func_miss2(message):
    print("called miss2")
    attendance = b''
    today = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    text = message.body['text']
    p = text.split("も")[0]
    send_massage = "add {}".format(p)

    client.send(send_massage.encode('utf-8')) 

    msg = client.recv(4096)
    message.send('失礼しました')
    attendance += msg
    attendance = pickle.loads(attendance)
    message.send('{0}現在の登校状況\n{1}'.format(today, ", ".join(attendance)))

@respond_to('bye')
@respond_to('バイバイ')
@respond_to('ばいばい')
@respond_to('は帰')
@listen_to('bye')
@listen_to('バイバイ')
@listen_to('ばいばい')
@listen_to('は帰')
def listen_func_bye(message):
    print("called bye")
    display_name = message.user['profile']['display_name']
    send_massage = "bye {}".format(display_name)

    client.send(send_massage.encode('utf-8')) 

    msg = client.recv(4096)
    # flag = bool(int(msg.encode('hex'), 16))
    flag = msg.decode('utf-8')
    if flag == "ok":
        message.send('バイバイ {}'.format(display_name))
    else:
        message.send('あなたは既に研究室にいません')
#####################################################
##  隠れコマンド
#####################################################
@respond_to('井戸')
@respond_to('ido')
@respond_to('Ido')
@respond_to('いど')
@listen_to('井戸')
@listen_to('いど')
@listen_to('Ido')
@listen_to('ido')
def ido_react(message):
    print("called ido")
    message.react('fast_parrot')
    message.react('parrot_mix')
    message.react('party_ido')
    message.react('parrot_elastic')
    message.react('super_fast_parrot')


