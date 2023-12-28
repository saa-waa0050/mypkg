# mypkg
[![test](https://github.com/saa-waa0050/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/saa-waa0050/robosys2023.ver2/actions/workflows/test.yml)

このリポジトリは千葉工業大学　ロボットシステム学の授業用・学習用リポジトリです。
ここではROS 2について学習しています。
## 機能（ノード）について
各機能はROS 2ノードにまとまっており、利用できる各機能（ノード）は以下の通りです。
>- 0.5秒毎に整数値を１増加させ、数値を出力する。（初期値０）
>- 入力（整数値）をターミナル上に出力する。

<br>

## インストール
インストールしたいディレクトリで、以下のコードを実行してください。
>```
>git clone https://github.com/saa-waa0050/mypkg.git
>```
>実行結果
>```
>Cloning into 'mypkg'...
>remote: Enumerating objects: 353, done.
>remote: Counting objects: 100% (113/113), done.
>remote: Compressing objects: 100% (78/78), done.
>remote: Total 353 (delta 69), reused 65 (delta 29), pack-reused 240
>Receiving objects: 100% (353/353), 97.77 KiB | 1.46 MiB/s, done.
>Resolving deltas: 100% (217/217), done.
>```
>このような文章が返ってくればインストールは完了です。

コマンドが入ったディレクトリに移動するため、続けて以下のコードを実行してください。
```
cd mypkg/
```
>このディレクトリで、以下に紹介するコマンドを実行することで、各機能を利用することができます。
<br>

## 各機能（ノード）の使い方

### 0.5秒毎に整数値を１増加させ、数値を出力
>```
>ros2 run mypkg talker
>```
>初期値０から0.5秒毎に整数値（１６ビット符号付き）を１ずつ増加させ、その数値をトピック`countup`にパブリッシュします。

>####  実行例
>`コマンド1`
>```
>ros2 run mypkg talker

>`コマンド2（コマンド1とは別端末で実行）`
>```
>ros2 topic echo countup #
>```

>`結果`
>```
>data: 0
>---
>data: 1
>---
>data: 2
>---
>data: 3
>---
>...
>```

### 入力（整数値）をターミナル上に出力
>```
>ros2 run mypkg listener
>```
>トピック`countup`から整数値（１６ビット符号付き）のメッセージをサブスクライブし、ターミラルヘ出力します。

>####  実行例
>`コマンド1`
>```
>ros2 run mypkg  listener

>`コマンド2（コマンド1とは別端末で実行）`
>```
>ros2 run mypkg talker
>```

>`結果`
>```
>[INFO] [1703719348.714483643] [listener]: Listen:0
>[INFO] [1703719349.206618994] [listener]: Listen:1
>[INFO] [1703719349.706984029] [listener]: Listen:2
>[INFO] [1703719350.207299896] [listener]: Listen:3
>...
>```
>ここでは`talker`と組み合わせて使用しています。このようにすることで、異なる機能（ノード）間で数値のやりとり（通信）をすることが出来ます。
>また、以下コマンドを使用することで、１つの端末上でノード間の通信ができます。
>>####  実行例
>>`コマンド`
>>```
>>ros2 launch mypkg talk_listen.launch.py

>>`結果`
>>```
>>[INFO] [launch]: All log files can be found below /home/saawaa/.ros/log/2023-12-28-08-25-44-524810-localhost-14446
>>[INFO] [launch]: Default logging verbosity is set to INFO
>>[INFO] [talker-1]: process started with pid [14448]
>>[INFO] [listener-2]: process started with pid [14450]
>>[listener-2] [INFO] [1703719545.314192281] [listener]: Listen:0
>>[listener-2] [INFO] [1703719545.808679446] [listener]: Listen:1
>>[listener-2] [INFO] [1703719546.308801233] [listener]: Listen:2
>>[listener-2] [INFO] [1703719546.808630130] [listener]: Listen:3
>>...
>

<br>

## 必要なソフトウェア
* ROS 2
* Python
## テスト環境
* Ubuntu20.24 on Windows
* ROS 2 foxy

## 権利
- このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布及び使用が許可されます。
- このパッケージのコードは，下記のスライド群（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
>rhttps://ryuichiueda.github.io/my_slides/robosys_2022/lesson11.html#/6
>https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/4
>https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/22
- © 2023 Shusuke Osawa
