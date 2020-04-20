#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-20 11:29'

import time

import os
import sys
print(os.getcwd())
sys.path.append(os.getcwd())   # IDE自动加入，命令行运行需要加入

import grpc
from concurrent import futures

import compute_pb2, compute_pb2_grpc  # 导入根据proto文件生成的两个文件, 不用管IDE报错
# from grpc_demo.compute import compute_pb2, compute_pb2_grpc  # 导入根据proto文件生成的两个文件, 不用管IDE报错

class ComputeServicer(compute_pb2_grpc.ComputeServicer):
    def SayHello(self, request, ctx):
        max_len = str(len(request.helloworld))
        content = "Hello, your words length is: {}".format(max_len)
        return compute_pb2.HelloReply(result=content)


def main():
    # 多线程服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    # 实例化 计算len的类
    servicer = ComputeServicer()
    # 注册本地服务,方法ComputeServicer 只有这个是变的
    compute_pb2_grpc.add_ComputeServicer_to_server(servicer, server)
    # 监听端口
    server.add_insecure_port('127.0.0.1:19999')
    # 开始接收请求进行服务
    server.start()
    # 使用 ctrl+c 可以退出服务
    print()
    try:
        print("Server launch...")
        print("running...")
        time.sleep(100)

        # 如果想要一直等待，可以用下面的代码
        # while True:
        #     time.sleep(186400)
    except KeyboardInterrupt:
        print("stopping...")
        server.stop(0)


if __name__ == '__main__':
    main()

