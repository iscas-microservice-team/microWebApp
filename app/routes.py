from app import app
from flask import render_template, flash, redirect
from app.forms.postForm import PostForm
import requests
from func_pack import create_rec_hash, get_current_time, get_api_info
from config import Config


@app.route('/', methods=['POST'])
def post():
    form = PostForm()
    # 处理 POST 的逻辑
    if form.validate_on_submit():
        # 发起请求的数据库操作 url
        insert_url = 'http://' + Config.DB_CONNECTOR_URL + '/insert-post/' + create_rec_hash()
        # 发送 POST 请求的数据
        post_data = {
            'username': form.username.data,
            'post': form.comment.data,
            'postTime': get_current_time()
        }
        # 发出 POST 请求
        result = requests.post(insert_url, data=post_data)
        if result.status_code is 200:
            # flash('Comment post success!{}'.format(form.username.data, form.comment.data))
            flash('Comment post success!')
        else:
            flash('Comment post failed!')
        return redirect('/')


# 获取最新评论消息
@app.route('/', methods=['GET'])
def welcome():
    form = PostForm()
    query_url = 'http://' + Config.DB_CONNECTOR_URL + '/all-queries'
    # 获取最新的 comments 信息
    result = requests.get(query_url)
    queries_list = get_api_info(result)
    # 逆序，将最新的留言放置最前
    queries_list.reverse()
    # 处理 GET 的逻辑
    return render_template('frontPage.html', title='Greetings!', comments=queries_list, form=form)
    pass


# 获取 username 为 admin 的用户所发出的信息
@app.route('/announcement', methods=['GET'])
def announcement():
    query_url = 'http://' + Config.DB_CONNECTOR_URL + '/queries/' + 'Administer'
    # 获取最新的 comments 信息
    result = requests.get(query_url)
    queries_list = get_api_info(result)
    # 逆序，将最新的留言放置最前
    queries_list.reverse()
    # 处理 GET 的逻辑
    return render_template('announcement.html', title='Rules', comments=queries_list)
    pass


