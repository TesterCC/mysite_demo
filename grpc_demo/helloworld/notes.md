## Install gRPC
### python -m pip install grpcio

## Install gRPC tools
### python -m pip install grpcio-tools googleapis-common-protos


## 1st, write helloworld.proto

#### cd xxxxx/mysite/grpc_demo/helloworld

## 2ed, compile .proto file to generate server code.
#### python -m grpc_tools.protoc  -I./ --python_out=. --grpc_python_out=. helloworld.proto

#### generate helloworld_pb2.py  helloworld_pb2_grpc.py

### 消息定义文件  helloworld_pb2.py

### grpc服务定义  helloworld_pb2_grpc.py

简单看下：
- 在grpc服务架手脚定义中，定义了gRPCStub，这是给client端使用，调用grpc服务的。
- 定义的服务类gRPCServicer，方法SayHello需要我们在子类中进行实现。定义的add_gRPCServicer_to_server方法，用于把实现的类和grpc API调用注册起来。

这里使用的几个主要方法（类）：
- grpc.server – Creates a Server with which RPCs can be serviced
- grpc.method_handlers_generic_handler – Creates a GenericRpcHandler from RpcMethodHandlers.
- grpc.unary_unary_rpc_method_handler – Creates an RpcMethodHandler for a unary-unary RPC method.


## 3rd, write  server and client python code


## REF:
#### https://blog.csdn.net/whereismatrix/article/details/78595550