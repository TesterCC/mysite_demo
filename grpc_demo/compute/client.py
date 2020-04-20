#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-20 11:35'

import os
import sys
print(os.getcwd())
sys.path.append(os.getcwd())   # IDE自动加入，命令行运行需要加入

import grpc
import compute_pb2
import compute_pb2_grpc


_HOST = '127.0.0.1'
_PORT = '19999'

def main():
    with grpc.insecure_channel("{0}:{1}".format(_HOST, _PORT)) as channel:
        client = compute_pb2_grpc.ComputeStub(channel=channel)
        response = client.SayHello(compute_pb2.HelloRequest(helloworld="1234567"))
    print("received: " + response.result)


if __name__ == '__main__':
    main()
