import re
import json


def search_keywords(keywords, data):
    result = []
    for key, value in data.items():
        regex_pattern = r'[^"]*{}[^"]*'.format(keywords)
        if (re.search(regex_pattern, value)):
            result.append((key, value))
    return result


if __name__ == '__main__':
    hotkey_zh = []
    # 读取json文件，加载hotkey_zh
    with open('hotkey-zh.json', 'r', encoding="utf-8") as f:
        hotkey_zh = json.load(f)

    data = hotkey_zh["vsc"]
    # # 示例搜索
    # while True:
    #     # 输入搜索关键词
    #     keywords = input("请输入搜索关键词：")
    #     if (keywords == 'q'):
    #         break
    #     results = search_keywords(keywords, data=data)
    #     print(results)

    res = search_keywords("打开", data)
    print(type(res[0]))
    for item in res:
        print(item[0])
        print(item[1])
        print(type(item[0]))
