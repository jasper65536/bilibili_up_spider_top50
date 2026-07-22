import yt_dlp
import requests
import time
import random
import os
import tempfile
from datetime import datetime


def timestamp_to_date(timestamp):
    if not timestamp:
        return ""
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")


def write_cookie_file(cookie: str) -> str:
    cookie_lines = ["# Netscape HTTP Cookie File"]
    for item in cookie.split(";"):
        item = item.strip()
        if "=" in item:
            key, value = item.split("=", 1)
            cookie_lines.append(
                f".bilibili.com\tTRUE\t/\tFALSE\t0\t{key.strip()}\t{value.strip()}"
            )
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    tmp.write("\n".join(cookie_lines))
    tmp.close()
    return tmp.name


def get_video_detail(bvid: str, session: requests.Session) -> dict:
    resp = session.get(
        "https://api.bilibili.com/x/web-interface/view",
        params={"bvid": bvid}
    )
    data = resp.json()
    if data["code"] != 0:
        return {"title": "", "view": 0, "danmaku": 0, "duration": 0, "pubdate": ""}

    info = data["data"]
    stat = info.get("stat", {})
    return {
        "title": info.get("title", ""),
        "view": stat.get("view", 0),
        "danmaku": stat.get("danmaku", 0),
        "duration": info.get("duration", 0),
        "pubdate": timestamp_to_date(info.get("pubdate", 0))
    }


def get_videos(mid, cookie: str = "", max_videos: int = 0):
    print(f"开始获取 UP主 {mid} 的视频列表...")
    time.sleep(random.uniform(2, 5))

    url = f"https://space.bilibili.com/{mid}/video"

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "sleep_interval_requests": random.uniform(3, 6),
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Referer": "https://www.bilibili.com",
        }
    }

    if max_videos > 0:
        ydl_opts["playlistend"] = max_videos

    cookie_file = None
    if cookie:
        cookie_file = write_cookie_file(cookie)
        ydl_opts["cookiefile"] = cookie_file

    bvids = []

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)
            entries = result.get("entries", [])
            bvids = [e["id"] for e in entries if e.get("id")]
            print(f"共获取到 {len(bvids)} 个视频BV号，开始获取详情...")
    except Exception as e:
        print(f"获取视频列表失败: {e}")
    finally:
        if cookie_file and os.path.exists(cookie_file):
            os.unlink(cookie_file)

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer": "https://www.bilibili.com"
    })

    videos = []
    for i, bvid in enumerate(bvids, 1):
        detail = get_video_detail(bvid, session)
        videos.append({
            "title": detail["title"],
            "bvid": bvid,
            "aid": 0,
            "view": detail["view"],
            "danmaku": detail["danmaku"],
            "duration": detail["duration"],
            "pubdate": detail["pubdate"],
            "url": f"https://www.bilibili.com/video/{bvid}"
        })
        if i % 10 == 0:
            print(f"已获取 {i}/{len(bvids)} 条详情")
        time.sleep(random.uniform(0.5, 1.5))

    return videos
