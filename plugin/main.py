# -*- coding: utf-8 -*-
import webbrowser
from flowlauncher import FlowLauncher
import sys
import os
import json
from plugin.search import search_keywords
from plugin.message import testMsg, errorMsg, MessageDTO

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))


class HotKey(FlowLauncher):

    def query(self, query: str) -> list:
        with open('hotkey-zh.json', 'r', encoding="utf-8") as f:
            hotkey_zh = json.load(f)
        if (query == ""):
            return MessageDTO(title="begin", subtitle="Please enter the correct format").asFlowMessage()
        app = query.split(" ")[0]
        if (app not in hotkey_zh):
            return MessageDTO(title="Error", subtitle="Please enter the correct format").asFlowMessage()
        if (query.count(" ") == 0):
            keyword = ""
        else:
            keyword = query.split(" ")[1]
        data = hotkey_zh[app]
        results = search_keywords(keyword, data)

        # return MessageDTO(title=app, subtitle=keyword).asFlowMessage()
        response = []
        for item in results:
            response.append({
                "Title": item[1],
                "SubTitle": item[0],
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": [""]
                }
            })
        return response

    def context_menu(self, data):
        # 用于右键菜单
        return [
            {
                "Title": "HotKey's Context menu",
                "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/attack825/Flow.Launcher.Plugin.HotKey"]
                }
            }
        ]

    def open_url(self, url):
        # 用于打开网页
        webbrowser.open(url)

    def simulate_buttons(hotkey):
        # 用于模拟按键
        pass


if __name__ == "__main__":
    HotKey()
