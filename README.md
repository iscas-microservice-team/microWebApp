# 微服务组件 - Web UI 模块

本 web 应用完全基于微服务理念而设计，感受微服务的魅力吧！

剩余模块的组件在其他 repository 中。

## 使用 docker 运行本应用

1. 更改 microWebApp/ 中 config.py 内的配置信息

2. 利用 microWebApp/ 目录中的 Dockerfile 将应用容器化

	cd microWebApp/

	docker build -t microwebapp .

3. 启动 docker 容器

	docker run -it -d --rm -p 80:80 microwebapp

4. 访问服务器的 80 端口，即可看到微服务页面正在运行啦！

by XinyaoTian
