# -*- coding: utf-8 -*-
from flask import Flask, redirect
import os  # 提前导入os，避免在main中重复导入

app = Flask(__name__)

# 优化：根路径（/）直接触发重定向，访问域名即可跳转
@app.route('/')
def jump_to_taobao():
    target_link = "https://m.tb.cn/h.Spd9RfKLoRnwZ2M"
    # 302临时重定向（符合代码原意，若需永久重定向可改为code=301）
    return redirect(target_link, code=302)

if __name__ == '__main__':
    # 适配Render的端口要求（环境变量PORT由Render自动分配）
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
