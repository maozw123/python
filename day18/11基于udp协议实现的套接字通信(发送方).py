"""
传输层传输协议：
    UDP

    TCP

套接字通信(socket)

UDP
1.发送方
    1.创建套接字(指定的用的传输协议)
    2.发送给谁
    3.关闭套接字


2.接收方

"""
import socket
#1  创建套接字
#socket.AF_INET :表示ipV4  socket.SOCK_DGRAM:表示使用UDP协议
socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address=('10.10.116.144',7777)
while True:
    data=input('请输入一段话').encode(encoding='utf-8')

    #2  发送
    socket.sendto(data,address)
    #接收回复的消息
    v=socket.recvfrom(4094)
    a=v[0].decode(encoding='utf-8')
    print(f'接收到回复的消息:{a}')
socket.close()