# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     实现一个简单的HTTP服务器
   Description :
   Author :       bing
   date：          2021/6/2
-------------------------------------------------
   Change Activity:
                   2021/6/2:
-------------------------------------------------
"""
__author__ = 'bing'
import socket


    # 主程序乳肉

# 1. 创建套接字
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定
tcp_server.bind(('127.0.0.1', 8080))
# 3. 变为监听套接字
tcp_server.listen(128)
# 4. 等待新客户端的连接
conn, addr = tcp_server.accept()
# 5. 为这个客户端服务
conn.recv(1024)
conn.send('HTTP/1.1 200 OK\r\n\r\n<h1>hmb</h1>'.encode('utf8')) # 在程序中\r\n表示换行。（为了兼容windows）
conn.close()
