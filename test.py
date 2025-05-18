from futu import *

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)  # 创建行情对象
test = quote_ctx.get_market_snapshot('HK.00700')
# 将获取到的行情数据完成

quote_ctx.close()  # 关闭对象，防止连接条数用尽
