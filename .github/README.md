# AIWolfLogAnalyzer

## 概要
[RandomTalkAgent](https://github.com/aiwolfdial/RandomTalkAgent)や[AIWolfNLGameServer](https://github.com/aiwolfdial/AIWolfNLGameServer)で対戦した際に生成されるログファイルを解析することを助けるプログラムです。`lib/column.py`や`analyze.py`を変更してご自身の目的に合ったプログラムに変更してご使用ください。デフォルトのまま`analyze.py`を実行すると`./log/`以下のログファイルを読み込み、各エージェントの勝率を算出します。

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
- `action.py`\
ログファイルの各列2行目に当たる、どの行動をしているのかを示すものを定義しているファイルです。
- `column.py`\
行動ごとに各列が持つ意味が異なるので、それぞれの行動ごとに定義しているファイルです。また、各列を`,`で区切りlistを渡して目的の物を取り出すメソッドの実装もしています。
- `count.py`\
勝率を計算するためにログから勝った回数や負けた回数をカウントするためにカウント用のクラスを定義しているファイルです。
- `role.py`\
AIWolfで使用される役職を定義しています。
- `util.py`\
色々な場所で使う関数を定義する場所です。

### res
`config.ini`: 様々な設定を記述します。(詳細は後述します)

## res/config.ini
```
[log]
path = ./log/
save_to_file = true
output_file_name = count_result.txt
ratio_flag = false
ratio_digit = 10

[agent]
classify_by_number = false
```

### log
- `path`\
ログファイルがどのパスにあるか指定する物です。
- `save_to_file`: 勝率の出力先を指定します。\
    - `true`: ファイルに出力    
    - `false`: 標準出力に出力
- `output_file_name`\
`save_to_file=true`の時に使用されます。出力する際のファイル名を指定します。
- `ratio_flag`: 勝敗の割合を求めるか個数を求めるかを決定します。 
    - `true`: 割合を求めます。
    - `false`: 個数を求めます。
- `ratio_digit`\
`ratio_flag=true`の時に使用されます。割合を小数点以下何位まで求めるか指定します。

### agent
- `classify_by_number`: エージェント名に数字が含まれている場合に数字もエージェント名の一部とみなし数字の違いはエージェントの違いを示すこととするか、数字を除去して数字が違う場合でも同一エージェントとみなすかを決定します。
    - `true`: 数字もエージェント名の一部とみなします。エージェント名から数字は除去されません。
    - `false`: 数字が違う場合でも同一のエージェントとみなします。エージェント名から数字が除去されます。