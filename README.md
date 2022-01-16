# 概要
### ロボットシステム学　課題2
0から数を1倍、2倍、5倍に増やしてゆくプログラムです。

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
 
## 2. twice.py 実行

新しいタブを立ち上げます。

  ```
rosrun mypkg twice.py
 ```

## 3. fifth.py 実行

新しいタブを立ち上げます。

  ```
rosrun mypkg fifth.py
  ```

## 出力を行う

新しいタブを立ち上げます。

数を1ずつ増やす
 ```
rostopic echo /count_up
 ```
 
 数を2（2倍）ずつ増やす
 ```
rostopic echo /twice
 ```
 
 数を５（５倍）ずつ増やす
 ```
rostopic echo /fifth
 ```

# ライセンス
Copyright (c) 2021 Ryuich Ueda

Copyright (c) 2021 Kazuma Toyoshima
