#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""X（Twitter）自動投稿スクリプト - 作業着LP用"""

import os
import random
import requests
from requests_oauthlib import OAuth1
from datetime import datetime

# APIキー（GitHub Secretsから読み込み）
API_KEY = os.environ["X_API_KEY"]
API_SECRET = os.environ["X_API_SECRET"]
ACCESS_TOKEN = os.environ["X_ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["X_ACCESS_TOKEN_SECRET"]

LP_URL = "https://rakuten-sale-info.github.io/workwear-lp/"

# 投稿パターン（ローテーション）
TWEETS = [
    # 朝パターン
    [
        f"""☀️ 今日も現場お疲れさまです！

夏の作業現場で一番つらいのは「暑さ」じゃないですか？

空調服に変えてから「別世界」という声が続出中。
午後もバテずに動けるようになった人が急増中👷

👉 現場向け作業着まとめはこちら
{LP_URL}

#作業服 #現場仕事 #空調服 #夏対策""",

        f"""🌅 おはようございます！

現場で働く方へ、知っておきたい事実。

❌ 安い作業着 → すぐ破れて買い直し
✅ 機能性作業着 → 長持ちしてコスパ◎

最初から良いものを選ぶ方が結果的にお得です💡

👉 厳選アイテムをチェック
{LP_URL}

#作業着 #ワークウェア #楽天""",
    ],
    # 昼パターン
    [
        f"""🥵 真夏の現場、限界を感じていませんか？

【夏の現場あるある】
・午前中から汗だく
・午後は集中力ゼロ
・足がパンパンで帰宅

これ全部、作業着選びで解決できます。
機能性作業着に変えた人のリアルな声を紹介中👇

{LP_URL}

#夏 #現場作業 #熱中症対策 #作業服""",

        f"""💡 女性現場スタッフさんにも人気！

「動きやすいサイズ展開があって助かってます」
「腕を上げても引っかからない！」

ストレッチ作業服、男性だけじゃなく
女性にもめちゃくちゃ評判いいです👷‍♀️

詳しくはこちら→ {LP_URL}

#女性現場 #作業着女子 #ストレッチ作業服""",
    ],
    # 夜パターン
    [
        f"""🛒 楽天でお得に作業着を揃えるコツ

✅ お買い物マラソン中 → ポイント最大10倍
✅ 楽天カード払い → さらに+2倍
✅ まとめ買い → 送料節約にも◎

消耗品の作業着はセール時にまとめ買いが鉄則！

👉 おすすめアイテムはこちら
{LP_URL}

#楽天 #お買い物マラソン #節約 #作業着""",

        f"""🌙 今日の現場どうでしたか？

足が疲れてる方へ👟

「軽量安全靴に変えたら仕事終わりのむくみが減った」
という声が多数届いてます。

安全性もJIS規格クリア済み。
軽くて安全、いいことしかない。

{LP_URL}

#安全靴 #現場仕事 #足の疲れ #軽量""",
    ],
]

def post_tweet(text):
    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    response = requests.post(
        "https://api.twitter.com/2/tweets",
        json={"text": text},
        auth=auth
    )
    return response

def main():
    now = datetime.utcnow()
    hour = now.hour

    # 時間帯でパターンを選択
    if hour < 4:      # JST 朝8時
        pattern = 0
    elif hour < 8:    # JST 昼12時
        pattern = 1
    else:             # JST 夜8時
        pattern = 2

    tweet = random.choice(TWEETS[pattern])
    print(f"投稿パターン: {pattern}")
    print(f"投稿内容:\n{tweet}\n")

    response = post_tweet(tweet)

    if response.status_code == 201:
        print("✅ 投稿成功！")
    else:
        print(f"❌ エラー: {response.status_code}")
        print(response.text)
        exit(1)

if __name__ == "__main__":
    main()
