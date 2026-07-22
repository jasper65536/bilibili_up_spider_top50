from crawler import get_videos
from export import save_excel
from chart import create_chart


mid = "519872016"

COOKIE = "buvid3=3161A2A6-117F-843B-744F-7ABFF7140E8168267infoc; b_nut=1784682868; _uuid=EEB15C1010-7426-B29E-101D9-8F57ABAF6A8468721infoc; lang=zh-Hans; buvid4=B603929E-DECD-590B-C5CB-3D7AC1D8BA0170454-026072209-RQ/ZuATPpQcdyOyYiRKm8A%3D%3D; buvid_fp=8116f6fb9b2503f208e3b8ebbaa0876f; CURRENT_QUALITY=0; rpdid=|(u~)YRJkkRu0J'u~)RY)k)~~; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODQ5NDI4OTAsImlhdCI6MTc4NDY4MzYzMCwicGx0IjotMX0.FKzI34zSFCLsdQgVOAtKSI_JDaOQ9q247OFyezveOac; bili_ticket_expires=1784942830; home_feed_column=5; browser_resolution=1850-966; SESSDATA=a5fa7637%2C1800260765%2C0f8ce%2A71; bili_jct=6097b7950fb002a0c49b3785a5d220c6; DedeUserID=3546748521810214; DedeUserID__ckMd5=2e2c37c344f678b8; theme-tip-show=SHOWED; sid=86lx7kpc; CURRENT_FNVAL=2000; theme-avatar-tip-show=SHOWED; bp_t_offset_3546748521810214=1227828023466655744; b_lsid=E7338886_19F8944C6CC"

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
