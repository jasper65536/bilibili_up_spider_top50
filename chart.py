import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False

def create_chart(videos):

    titles = []
    views = []


    # 取播放最高10个
    top10 = sorted(
        videos,
        key=lambda x: x["view"],
        reverse=True
    )[:10]


    for video in top10:
        titles.append(
            video["title"][:10]
        )

        views.append(
            video["view"]
        )


    plt.figure(figsize=(12,6))


    plt.bar(
        titles,
        views
    )


    plt.xticks(
        rotation=45,
        ha="right"
    )


    plt.title(
        "Bilibili Top10 Videos"
    )

    plt.xlabel(
        "Video"
    )

    plt.ylabel(
        "Views"
    )


    plt.tight_layout()


    plt.savefig(
        "top10_views.png"
    )


    print("图表生成完成")