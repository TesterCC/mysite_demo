#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-29 00:24'

import sys

"""The Python implementation of the gRPC client."""

import grpc
from grpchello_pb2  import *    ## or import grpchello_pb2
from grpchello_pb2_grpc import *
## No grpcDemo!  from grpcDemo import grpchello_pb2, grpchello_pb2_grpc #error!

_PORT = '8188'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = gRPCStub(channel=conn)
    response = client.SayHello(HelloRequest(name='Lily'))
    print("received: " + response.message)


##
if __name__ == '__main__':

    if len(sys.argv)== 2:
        print (sys.argv[1])
        _HOST = sys.argv[1]
    else:
        _HOST = 'localhost'

    #
    run()
