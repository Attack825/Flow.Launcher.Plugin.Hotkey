import urllib.parse

testMsg = [
    {
        "Title": "HotKey's Context",
        "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
        "IcoPath": "Images/app.png",
        "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": [""]
        }
    }
]

errorMsg = [
    {
        "Title": "Error",
        "SubTitle": "Please enter the correct format",
        "IcoPath": "Images/app.png",
        "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": [""]
        }
    }
]


class MessageDTO:
    def __init__(self, title="title", subtitle="subtitle", icopath="Images/app.png", method="open_url", parameters=[""]) -> None:
        self.title = title
        self.subtitle = subtitle
        self.icopath = icopath
        self.method = method
        self.parameters = parameters

    def asFlowMessage(self) -> list:
        return [{
            "Title": urllib.parse.unquote(self.title),
            "SubTitle": self.subtitle,
            "IcoPath": self.icopath,
            "jsonRPCAction": {
                "method": self.method,  # 自定义插件的方法
                "parameters": self.parameters  # 自定义插件类的参数
            }
        }]


if __name__ == '__main__':
    res = MessageDTO("title", "subtitle", "Images/app.png",
                     "method", "parameters")
    # print(res.asFlowMessage())
    app = "e"
    keyword = "a"
    print(MessageDTO(title=app, subtitle=keyword).asFlowMessage())
