# -*- coding: utf-8 -*-
from flask import Flask, redirect

app = Flask(__name__)

# 后端跳转接口：前端请求该地址，后端返回302重定向到目标链接
@app.route('/jump')
def jump_to_target():
    # 真实目标链接（可替换为任意需要隐藏的链接）
    target_link = "https://m.tb.cn/h.Spd9RfKLoRnwZ2M"
    # 返回302临时重定向，Location头指向真实链接
    return redirect(target_link, code=302)

if __name__ == '__main__':
    # 适配部署平台的端口要求（使用环境变量或默认5000）
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)