import sublime
import sublime_plugin


class MarkdownTodoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.line(self.view.sel()[0])  # sel() 返回光标位置. line() 返回光标所在行的 Region, 需要传递光标位置
        text = self.view.substr(region)  # substr() 返回指定 Region 包含的文本
        if "- [ ]" in text:
            new_text = text.replace("- [ ]", "- [x]")
            self.view.replace(edit, region, new_text)  # 替换区域所有内容
        elif "- [x]" in text:
            new_text = text.replace("- [x]", "- [ ]")
            self.view.replace(edit, region, new_text)
        else:
            new_text = "- [ ] " + text
            self.view.replace(edit, region, new_text)
