# 微服务组件 - Web UI 模块

本 web 应用完全基于微服务理念而设计，感受微服务的魅力吧！

剩余模块的组件在其他 repository 中。

## 优化了基于 Docker 和 Kubernetes 运行时的参数配置

通过启动容器或 yaml 中编写系统的环境变量，从而在容器外部设置各项待配置信息

- DB_MANAGER_IP  数据资源层服务的 IP 地址

- DB_MANAGER_PORT  数据资源层的端口号

示例如下:

    # for microappweb UI module
    DB_MANAGER_IP=24.101.157.243
    DB_MANAGER_PORT=9090
    export DB_MANAGER_IP
    export DB_MANAGER_PORT


## 使用 docker 运行本应用

1. 更改 microWebApp/ 中 config.py 内的配置信息

2. 利用 microWebApp/ 目录中的 Dockerfile 将应用容器化

	cd microWebApp/

	docker build -t microwebapp .

3. 启动 docker 容器

	docker run -it -d --rm -p 80:80 microwebapp

4. 访问服务器的 80 端口，即可看到微服务页面正在运行啦！

by XinyaoTian
