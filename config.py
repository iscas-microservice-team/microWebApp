import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'aeaacf6364624879572615793'
    # 从系统环境变量中读出 DB_MANAGER 的相关配置信息，方便 k8s 和 docker 运行
    DB_MANAGER_IP = os.environ.get('DB_MANAGER_IP')
    DB_MANAGER_PORT = os.environ.get('DB_MANAGER_PORT')
    # DB_CONNECTOR_URL = '174.137.53.55:9090'
    DB_CONNECTOR_URL = str(DB_MANAGER_IP) + ":" + str(DB_MANAGER_PORT)

    
# 简单测试
if __name__ == '__main__':
    DB_MANAGER_IP = os.environ.get('DB_MANAGER_IP')
    DB_MANAGER_PORT = os.environ.get('DB_MANAGER_PORT')
    # DB_CONNECTOR_URL = '174.137.53.55:9090'
    DB_CONNECTOR_URL = str(DB_MANAGER_IP) + ":" + str(DB_MANAGER_PORT)
    print(DB_CONNECTOR_URL)
