import json
# string = "add "
# app = string.split(" ")[0]
# keyword = string.split(" ")[1]

# print(app)
# print(keyword)
# # 输出string的空格数量
# print(string.count(" "))


# with open('hotkey-zh.json', 'r', encoding="utf-8") as f:
#     hotkey_zh = json.load(f)
# print(hotkey_zh)
# print(type(hotkey_zh))


dict1 = {"flow": {
    "Alt+Space": "打开搜索窗口（默认和可配置）",
    "Enter": "执行",
    "Ctrl+Enter": "打开包含的文件夹",
}, "s": {}, "fa": {"da": "da"}
}

app = "s"
# 判断app是否在dict1中
if (app not in dict1):
    print("app not in dict1")
else:
    print("app in dict1")
    data = dict1[app]
    print(data)
