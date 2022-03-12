#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import os
import tkinter as tk
from PIL import ImageGrab
from pynput import keyboard
# import glob
from tkinter import filedialog

# スクリーンショット フルスクリーン
def screen_shot(path):
    screenshot = ImageGrab.grab()
    screenshot.save(path)

# キー押下時のコールバック関数
def press(key):
    if key == keyboard.Key.print_screen:
        path = sv_dir.get() + "/" + sv_big_item.get() + "-" + sv_mid_item.get() + "_" + str(iv_cnt.get()) + ".jpg"
        print(path)
        screen_shot(path)
        count_up()

# キーリリース時のコールバック関数
def release(key):
    if key == keyboard.Key.esc:     # escが押された場合
        return True    # listenerを止める

# ディレクトリ選択ダイアログ表示
def view_filedialog():
    sv_dir.set(tk.filedialog.askdirectory())

# 文字列検証関数
def validation(before_word, after_word):
    return ((after_word.isdecimal()) and (len(after_word)<=4)) or (len(after_word) == 0)

# カウンターリセット
def count_reset():
    # entry_cnt.delete(0,"end")
    # entry_cnt.insert(0, "0")
    iv_cnt.set(0)
    
# カウントアップ
def count_up():
    # entry_cnt.insert(0, int(entry_cnt.Get(0,"end")+1))
    iv_cnt.set(iv_cnt.get()+1)

# キー監視開始
listener = keyboard.Listener(
    on_press=press,
    on_release=release)
listener.start()

# ベースとなるウィンドウ生成
root = tk.Tk()
root.title(u"Test Tools")
root.geometry("400x300")

# カウンター
iv_cnt = tk.IntVar()
iv_cnt.set(0)
# 指定ディレクトリ
sv_dir = tk.StringVar()
sv_dir.set(os.path.expanduser("~"))

# 項目
sv_big_item = tk.StringVar()
sv_mid_item = tk.StringVar()
sv_sml_item = tk.StringVar()

# Dir Label
label_dir = tk.Label(root, textvariable=sv_dir)
label_dir.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)
# Ref Button
button_ref = tk.Button(root, text = '参照', command=view_filedialog)
button_ref.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

# 大項目
text_big = tk.Entry(root, width=10, textvariable=sv_big_item)
text_big.grid(column=1, row=1, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)
# 中項目
text_mid = tk.Entry(root, width=10, textvariable=sv_mid_item)
text_mid.grid(column=1, row=2, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)
# 小項目
text_sml = tk.Entry(root, width=10, textvariable=sv_sml_item)
text_sml.grid(column=1, row=3, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)


# カウンター
# スピンボックス設定
entry_cnt = tk.Spinbox(
    root,
    textvariable=iv_cnt,   #変数
    from_=0,          #下限値
    to=999,              #上限値
    increment=1,        #増減ステップ
    )
# entry_cnt = tk.Entry(root, textvariable=iv_cnt)
# # %s は変更前文字列, %P は変更後文字列を引数で渡す
# vcmd = (entry_cnt.register(validation), '%s', '%P')
# # Validationコマンドを設定（'key'は文字が入力される毎にイベント発火）
# entry_cnt.configure(validate='key', vcmd=vcmd)
entry_cnt.grid(column=1, row=4, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

root.mainloop()