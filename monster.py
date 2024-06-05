import PySimpleGUI as sg
import random
sg.theme("DarkBrown3")

layout = [[sg.T("あなたの名前を入力してください。")],
          [sg.T("名前"),sg.I(k="input")],
          [sg.B(" 実行 ", k="btn"), sg.T(k="txt")]]
win = sg.Window("あなたをモンハンのモンスターに例えます", layout,
                font=(None,14), size=(500,300))

def monster():
    monsters = ["リオレウス", "ジンオウガ", "ディノバルド", "ティガレックス",
                "クシャルダオラ", "テオテスカトル", "バルハザク", "ネルギガンテ",
                "イヴェルカーナ"]
    name = random.choice(monsters)
    win["txt"].update(name)

while True:
    e, v = win.read()
    if e == "btn" and v["input"] == "":
      sg.popup("名前を入力してください")
      continue
    if e == "btn":
      monster()
    if e == None:
      break
win.close()