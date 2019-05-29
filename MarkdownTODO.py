import re
import sublime
import sublime_plugin


class MarkdownTodoAddOrDeleteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.line(self.view.sel()[0])  # sel() 返回光标位置. line() 返回光标所在行的 Region, 需要传递光标位置
        text = self.view.substr(region)  # substr() 返回指定 Region 包含的文本
        new_text, ok = re.subn(r'. \[.\] ', '', text)  # 使用正则替换旧文本
        if ok:
            self.view.replace(edit, region, new_text)  # 替换 sublime view 区域展示内容
        else:
            new_text, ok = re.subn(r'^( *)', r'\1- [ ] ', text)
            if ok:
                self.view.replace(edit, region, new_text)  # 替换 sublime view 区域展示内容
            else:
                new_text = '- [ ] ' + text
                self.view.replace(edit, region, new_text)


class MarkdownTodoSwitchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.line(self.view.sel()[0])  # sel() 返回光标位置. line() 返回光标所在行的 Region, 需要传递光标位置
        text = self.view.substr(region)  # substr() 返回指定 Region 包含的文本
        if " [ ] " in text:
            new_text = text.replace(" [ ] ", " [x] ")
            self.view.replace(edit, region, new_text)
        elif " [x] " in text:
            new_text = text.replace(" [x] ", " [ ] ")
            self.view.replace(edit, region, new_text)