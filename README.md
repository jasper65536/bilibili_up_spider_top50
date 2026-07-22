# Bilibili Analyzer

一个基于 Python 的 B站 UP 主视频数据分析工具。

自动获取 UP 主视频数据，并生成 Excel 数据分析报告。


## 功能

- 获取 UP 主视频列表
- 获取视频详细信息
- 视频播放量统计
- 弹幕数据统计
- 发布时间整理
- Excel 自动报告
- Top10 热门视频排行
- 播放量可视化


## 输出

运行后生成：

### bilibili_report.xlsx

包含：

- 视频数据
- 数据统计
- 热门排行


### top10_views.png

热门视频播放量图表。


## 安装


```bash
pip install -r requirements.txt



使用

修改 main.py：

mid = "你的UP主UID"

运行：

python main.py

如果需要访问限制内容：

填写：

COOKIE = "你的Cookie"