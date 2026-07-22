from crawler import get_videos
from export import save_excel
from chart import create_chart


mid = "输入你的mid"

COOKIE = "输入你的cookie"

MAX_VIDEOS = 50


videos = get_videos(mid, cookie=COOKIE, max_videos=MAX_VIDEOS)


print("视频数量:", len(videos))


if not videos:
    print("未获取到视频数据，请检查 mid 和 Cookie 是否正确")
else:
    for video in videos:
        print("----------------")
        print("标题:", video["title"])
        print("BV号:", video["bvid"])
        print("播放:", video["view"])
        print("弹幕:", video["danmaku"])
        print("发布时间:", video["pubdate"])
        print("链接:", video["url"])

    save_excel(videos)
    create_chart(videos)
