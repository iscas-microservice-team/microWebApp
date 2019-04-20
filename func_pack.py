# -*- encoding:utf-8 -*-
import datetime
import random
import requests
import json


# 随机生成唯一编码
def create_random_hash():
    nowtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    hash_code = hash(nowtime)
    # 绝对值处理
    if hash_code < 0 :
        hash_code = str(abs(hash_code))
    else:
        hash_code = str(hash_code)
    # 再添加随机位确保哈希值不重复
    seed = "abcdef"
    title = ""
    for _ in range(6):
        title = title + random.choice(seed)
    return str(title + hash_code)


# 生成图像唯一编码
def create_pic_hash():
    return "pic" + create_random_hash()


# 生成记录唯一编码
def create_rec_hash():
    return "rec" + create_random_hash()


# 生成当前时间 格式为 %Y-%m-%d/%H:%M:%S
def get_current_time():
    return str(datetime.datetime.now().strftime("%Y-%m-%d/%H:%M:%S"))


# 判定上传文件类型是否为指定类型
# 若文件后缀为 set 中的任意一种，返回 True；否则返回 False
def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 将 bytes 转换为 string
def _bytes_to_str(bytes_info):
    return bytes_info.decode("utf-8")


# 将 requests.get 或 post 的结果 result 获取到的信息转为由 dict 构成的 list
def get_api_info(request_result):
    content_str = request_result.content.decode("utf-8")
    list_content = []
    # print("json.loads length=" + str(len(json.loads(content_str))))
    # 若 api 返回的是空值
    if json.loads(content_str) is None:
        # 返回空的 list
        return []
    # 否则对 api 信息进行处理
    else:
        for item in json.loads(content_str):
            list_content.append(item)
        # 返回处理好的 list
        return list_content


if __name__ == "__main__":
    pass
    # result = requests.get('http://127.0.0.1:9090/all-queries')
    # print(result.content)
    # list_api_info = get_api_info(result.content)
    # print(type(list_api_info))
    # for info in list_api_info:
    #     print(info, "type=", type(info))
    # print(result)
    # print(result.content)
    # print(type(result))
    # queries = result.content.decode("utf-8")
    # print(queries)
    # print(type(queries))
    # json1_data = json.loads(queries)[0]
    # print(json1_data)
    # print(type(json1_data))

