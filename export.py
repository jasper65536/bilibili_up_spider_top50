import pandas as pd


def save_excel(videos):

    if not videos:
        print("没有数据，跳过导出")
        return

    df = pd.DataFrame(videos)


    # 视频数据
    with pd.ExcelWriter("demo/bilibili_report.xlsx") as writer:

        df.to_excel(
            writer,
            sheet_name="视频数据",
            index=False
        )


        # 数据统计

        summary = {
            "视频数量": [len(videos)],
            "平均播放": [
                int(df["view"].mean())
            ],
            "最高播放": [
                df["view"].max()
            ]
        }


        summary_df = pd.DataFrame(summary)


        summary_df.to_excel(
            writer,
            sheet_name="数据统计",
            index=False
        )


        # Top10

        top10 = df.sort_values(
            by="view",
            ascending=False
        ).head(10)


        top10.to_excel(
            writer,
            sheet_name="热门排行",
            index=False
        )


    print("报告生成完成")