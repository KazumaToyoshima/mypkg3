# 概要
### ロボットシステム学　課題2
実行後の経過時間表記をさせるROSリポジトリです。
一秒ごとに0から偶数を表示し、10になると0にリセットされるプログラムです。

# 開発環境:
Ubuntu20.04

Raspberry Pi 4

ROSインストール後、実行してください。以下のURLからインストールできます。

https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server

# 実行

まず、以下のコマンドを実行します。

 ```
roscore &
 ```
 ```
chmod +x count.py
 ```
  ```
source ~/.bashrc
```

## 1. count.py 実行

 ```
rosrun mypkg count.py
 ```
 
## 2. min.py 実行

新しいタブを立ち上げます。

  ```
rosrun mypkg min.py
 ```

## 3. time.py 実行

新しいタブを立ち上げます。

  ```
rosrun mypkg time.py
  ```

## 出力を行う

新しいタブを立ち上げます。

 ```
rostopic echo /timer1
 ```

# ライセンス
Copyright (c) 2021 Ryuich Ueda

Copyright (c) 2021 Hiroyuki Matstuda

Copyright (c) 2021 Kazuma Toyoshima
