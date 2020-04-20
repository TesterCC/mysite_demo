# RPC基础

RPC 是两个子系统之间进行的直接消息交互，它使用操作系统提供的套接字来作为消息的载体，以特定的消息格式来定义消息内容和边界。

gRPC 是 Google 开源的基于 Protobuf 和 Http2.0 协议的通信框架，Google 深度学习框架 tensorflow 底层的 RPC 通信就完全依赖于 gRPC库。

[REF](https://blog.csdn.net/sunt2018/article/details/90176015)

## python安装相关依赖

```shell
pip install grpcio grpcio-tools protobuf
```

## 开发步骤

这个是一个最基本的`python + gRPC`实现demo，实际项目用应用更复杂，可能还要加入服务发现等功能，但是，万变不离其宗。

### 1.编写协议文件

vim compute.proto

### 2.用grpc_tools和.proto协议文件生成必要的代码

```shell
cd ~/grpc_demo/compute
python -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=./ compute.proto

# python_out目录指定 xxxx_pb2.py的输出路径，我们指定为./ 当前路径
# grpc_python_out指定xxxx_pb2_grpc.py文件的输出路径,我们指定为./ 当前路径
# grpc_tools.protoc 这是我们的工具包，刚刚安装的
# -I参数指定协议文件的查找目录，我们都将它们设置为当前目录./
# compute.proto  是协议文件
```

生成的文件为：xxx_pb2_grpc.py 和 xxx_pb2.py , 这两个文件内容不要改动。
如果.proto内容更新，只要需要重新利用grpc_tools和.proto协议文件重新生成这两个文件。（会覆盖原来的内容）

```shell
-> ls
compute_pb2_grpc.py  compute_pb2.py  compute.proto

# compute.proto 协议文件
# compute_pb2.py 里面有消息序列化类
# compute_pb2_grpc.py 包含了服务器 Stub 类和客户端 Stub 类，以及待实现的服务 RPC 接口。
```

### 3.编写服务器代码
server.py

### 4.编写客户端代码
client.py

### 5.运行程序，先启动server.py，然后启动client.py

命令行运行时注意路径问题：

```python
import os
import sys
print(os.getcwd())
sys.path.append(os.getcwd())   # IDE自动加入，命令行运行需要加入
```



