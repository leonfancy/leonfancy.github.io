---
title: Docker 基础知识
date: 2018-10-12 11:22:09
categories:
- DevOps
tags:
- AWS
---

Docker 是目前最流行的容器技术，它将开发和运维带入了一个新的时代。本文主要介绍 Docker 的一些基本概念和常用命令。

<!--more-->

### Image 
Image (镜像) 是一个不可变的文件。它好比是一个可执行程序文件，操作系统执行程序时，将程序文件加载到内存执行，成为系统中的一个进程。而 Docker 通过`docker run`命令加载镜像文件执行，成为 Docker Container (容器)。

开发者编写 Dockerfile 文件，然后使用`docker build`命令来创建镜像。开发者可以将自己的镜像通过`docker push`上传到 Docker Registry 上，分享给其他人使用。其他人通过`docker pull`拉取镜像。官方的 Docker Registry 是 [Docker Hub](https://hub.docker.com/)，也可以自己搭建私有的 Registry。

Docker Registry 就和 GitHub 一样，是大家共享 Docker Image 的地方。其管理方式也是建立 repository (仓库)，每个仓库里面放一个镜像，随着开发的不断进行，仓库里面的镜像会有多个版本，在 Docker Registry 里面“版本”也称作 Tag (标签)。

常用命令：
```bash
# 创建一个名为 helloworld 的镜像，"."代表在当前目录，里面要有 Dockerfile 文件
docker build -t helloworld .  

# 列出当前系统中的所有镜像
docker image ls

# 删除镜像
docker image rm 

# 登录 Docker Hub
docker login 

# 为了将本地镜像上传到 Docker Registry，要先按照规则给本地镜像加 tag
#   <image> 是本地镜像的名字
#   <username> 是在 Docker Registry 上注册的 Docker ID；
#   <repository> 是 Docker Registry 上的仓库的名称
#   <tag> 用来区分这个镜像的不同版本
docker tag <image> <username>/<repository>:<tag>

# 上传镜像到 Docker Register
docker push <username>/<repository>:<tag>

# 从 Docker Register 下载镜像到本地
docker pull <username>/<repository>:<tag>
```

### Container 

Container (容器) 就是执行中的镜像。之所以叫容器，是因为 Container 使用隔离技术，像“容器”一样，把容器中的文件和执行的进程与宿主系统隔离开来。虽然是与宿主机隔离的，进程还是执行在宿主机系统本地的。这与传统的一样虚拟机（VM）技术不一样，它的进程是执行在虚拟的操作系统中的，与宿主操作系统没关系。

![VM vs. Docker](/images/docker_basics_vm_and_docker_compare.png)

Container 这种“软”隔离得益于 Linux 内核的 namespace 技术，因此 Docker 只适用于 Linux 系统。使用 namespace 技术，意味着容器中的进程还是在宿主机的内核中执行，但是因为命名空间(namespace)和其它进程不同，因此它只能看到自己所属容器中的资源。

常用命令：
```bash
# 加载镜像 helloworld 到容器中运行，将容器中的 80 端口，映射到宿主系统的 4000 端口
docker run -p 4000:80 helloworld

# 同上，-d 选项使容器在后台执行
docker run -d -p 4000:80 helloworld

# 列出所有运行中的 Container 
docker container ls 

# 列出所有 Container，包括没有处于运行状态的 
docker container ls -a

# 正常停止 Container 
docker container stop <containerId>

# 强制停止 Container 
docker container kill <containerId>

# 删除 Container 
docker container rm <containerId>

# 删除所有不是运行状态的 Container 
docker container prune
```

### Swarm

Swarm 是多个运行 Docker 的主机组成的集群。集群中的主机又叫做 node (节点)，根据角色分为两类：Mananger 和 Worker。Mananger 通过 `docker swarm init`命令创建，负责管理整个集群的节点，在集群中执行 Docker 指令都是在 Manager 上执行的。Worker 通过 `docker swarm join`命令加入到集群中，Worker 负责执行任务，运行 Container。通过`docker stack`命令，可以将应用按照指定的方式部署在集群上。

常用命令：
```bash
# 创建一个 Docker Swarm 集群，并且让本机成为这个 Swarm 集群的 Manager
docker swarm init

# 让主机作为 Worker 加入到 Swarm
#   <token> 是创建 Swarm 的时候生成的认证 token，
#   <ip>:<port> 是 Manager 的地址
docker swarm join --token <token> <ip>:<port>

# 查看 join token，需要在 Manager 主机上执行
docker swarm join-token -q worker

# 一个 Swarm 可以有多个 Manager，让主机作为 Manager 加入到 Swarm 中
docker swarm join-token manager

# 查看集群中所有的节点
docker node ls 

# 查看某个节点的详情
docker node inspect <node ID>

# 在 Worker 主机上执行下面命令，离开集群
docker swarm leave

# 在 Manager 主机上执行下面命令，离开集群，如果只有一个 Manager，那么集群会被关闭
docker swarm leave -f
```

### Service 

Service 是运行同一个镜像的一组 Container，这些 Container 提供相同的服务。这是为了在产品环境中，让一个服务有多个运行实例做负载均衡，达到服务高可用的目的。Docker Service 是 Docker Swarm 中的概念，只能在 Swarm 中使用。

一个 Service 一般定义了需要使用什么端口、启动几个 Container、负载均衡的规则等等。

常用命令：
```bash
# 列出所有的 Service
docker service ls 

# 列出某个 service 下面的所有 Container
docker service ps <service name>
```

### Stack  

Stack 是在集群中由多个 Service 组成的完整应用。一个应用通常分为多个服务，例如一个前后端分离的网站，可能分为前端页面、后端API、数据库三个服务。在集群中部署的时候，我们需要定义这三个 Service，将三个 Service 的规则写到`docker-cloud.yml`，然后使用`docker stack`命令部署到集群中去。

Stack 的前身是 **docker-compose**，docker-compose 是以前用来启动多个 Container 的，它使用`docker-compose.yml`文件指定多个 Container 的执行规则。Docker Stack 现在替代了 Docker Compose 的功能，而且更强大，同时 Stack 也兼容`docker-compose.yml`文件。

常用命令：
```bash
# 部署应用到 Swarm，docker-cloud.yml 文件描述了 Stack 所有的 Service。
docker stack deploy -c docker-cloud.yml <app name>

# 列出所有的 stack
docker stack ls 

# 删除一个 Stack
docker stack rm <app name>
```