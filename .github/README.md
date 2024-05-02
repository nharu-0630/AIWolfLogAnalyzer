# AIWolfLogAnalyzer

## 概要
[RandomTalkAgent](https://github.com/aiwolfdial/RandomTalkAgent)や[AIWolfNLGameServer](https://github.com/aiwolfdial/AIWolfNLGameServer)で対戦した際に生成されるログファイルを解析することを助けるプログラムです。デフォルトのまま`analyze.py`を実行すると`./log/`以下のログファイルを読み込み、各エージェントの勝率を算出します。

## ディレクトリ構成
```
.
├── analyze.py
├── lib
│   ├── __init__.py
│   ├── action.py
│   ├── column.py
│   ├── count.py
│   ├── role.py
│   └── util.py
└── res
    └── config.ini
```

### analyze.py
デフォルトのまま実行すると`./log/`以下のログファイルを読み込んで各エージェントの勝率を計算します。

### lib
`action.py`: ログファイルの各列2行目に当たる、どの行動をしているのかを示すものを定義しているファイルです。\
`column.py`: 行動ごとに各列が持つ意味が異なるので、それぞれの行動ごとに定義しているファイルです。また、各列を`,`で区切りlistを渡して目的の物を取り出すメソッドの実装もしています。\
`count.py`: 勝率を計算するためにログから勝った回数や負けた回数をカウントするためにカウント用のクラスを定義しているファイルです。\
`role.py`: AIWolfで使用される役職を定義しています。\
`util.py`: 色々な場所で使う関数を定義する場所です。

### res
`config.ini`: 様々な設定を記述します。(詳細は後述します)
