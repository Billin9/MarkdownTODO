import sublime
import sublime_plugin
import re


class MarkdownTodoAddOrDeleteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.line(self.view.sel()[0])  # sel() 返回光标位置. line() 返回光标所在行的 Region, 需要传递光标位置
        text = self.view.substr(region)  # substr() 返回指定 Region 包含的文本
        new_text, ok = re.subn(r'<en-todo checked=".*"/>', '', text)
        if ok:
            self.view.replace(edit, region, new_text)  # 替换区域所有内容
        else:
            new_text = '<en-todo checked="false"/>' + text
            self.view.replace(edit, region, new_text)


class MarkdownTodoSwitchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.line(self.view.sel()[0])  # sel() 返回光标位置. line() 返回光标所在行的 Region, 需要传递光标位置
        text = self.view.substr(region)  # substr() 返回指定 Region 包含的文本
        if 'checked="false"' in text:
            new_text = text.replace('checked="false"', 'checked="true"')
            self.view.replace(edit, region, new_text)  # 替换区域所有内容
        elif 'checked="true"' in text:
            new_text = text.replace('checked="true"', 'checked="false"')
            self.view.replace(edit, region, new_text)