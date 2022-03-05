#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
from PIL import ImageGrab
from pynput import keyboard

def screen_shot():
    # フルスクリーンで取得する
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.jpg')

def press(key):
    try:
        if key == keyboard.Key.print_screen:
            print('アルファベット {0} が押されました'.format(key.char))
    except AttributeError:
        if key == keyboard.Key.print_screen:
            screen_shot()

def release(key):
    if key == keyboard.Key.esc:     # escが押された場合
        return False    # listenerを止める

listener = keyboard.Listener(
    on_press=press,
    on_release=release)
listener.start()

root = tk.Tk()
root.title(u"Test Tools")
root.geometry("400x300")

# Ref Button
buttonRef = tk.Button(root, text = '参照')
buttonRef.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

root.mainloop()