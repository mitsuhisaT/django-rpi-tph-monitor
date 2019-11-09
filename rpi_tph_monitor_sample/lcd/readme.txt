RPiTPH Monitor基板用サンプルプログラム

【概要】
LCDへの文字表示と、LED点灯、スイッチ入力をするプログラムです。Raspbian Jessieでコンパイルしたバイナリとソースファイル一式および、Python3で記述したスクリプトです。


【ファイル構成 Python3】
rptph_ledsw.py : スイッチとLEDテスト用Python3スクリプト
lcdaqm.py : LCDモニタテスト用Python3スクリプト

【使い方 Python3】
ターミナルを開いて以下のように実行してください。
Python3 rptph_ledsw.py

SW1を押すと黄色LED、SW2を押すと緑色LED、SW3を押すと両方が点灯します。
プログラムを終了するにはキーボードからCtrl+Cを入力してください。


ターミナルを開いて以下のように実行してください。
Python3 lcdaqm.py

LCDモニタに文字が表示されれば成功です。


【ファイル構成 C++】
lcd : バイナリ実行ファイル
main.cpp : メインルーチン
LCDAQM.cpp : LCDを制御するクラスの実装ファイル
LCDAQM.h : LCDを制御するクラスのヘッダーファイル
Makefile : g++用メイクファイル

【使い方 C++】
I2Cを使用しますので、あらかじめ メニュー＞設定＞Raspberry Piの設定＞インターフェースよりI2Cを有効にしてください。
コマンドから設定する場合はsudo raspi-configコマンドをご利用ください。
ターミナルを開いて以下のように実行してください。
sudo ./lcd

LCDディスプレイに"TestStart"と表示されます。
その状態でSW1を押すとLED D4が、SW2を押すとLED D5が点灯します。スイッチを離すと消灯します。
プログラムを終了するにはキーボードからCtrl+Cを入力してください。


【更新履歴】
2017/10/23 : Python3のサンプルを追加しました。
