import sublime, sublime_plugin

class WithSettings:
    _settings = None

class ShowInOtherPaneCommand (sublime_plugin.WindowCommand):

    def get_other_group(self):
        group = self.window.active_group()
        if group == None:
            return

        num_groups = self.window.num_groups()
        return (group + 1) % num_groups

    def get_selected_text(self):
        view = self.window.active_view()
        if view == None:
            return

        sel = view.sel()[0]
        return view.substr(view.word(sel))

    def focus_other_group(self):
        other_group = self.get_other_group()
        self.window.focus_group(other_group)


class ShowFilesOverlayInOtherPane (ShowInOtherPaneCommand, WithSettings):        

    def run(self):
        word = self.get_selected_text()
        if word == None:
            return

        self.focus_other_group()
        self.window.run_command("show_overlay", {"overlay": "goto", "text": word, "show_files": True})


class GotoDefinitionInOtherPane (ShowInOtherPaneCommand, WithSettings):        

    def run(self):
        word = self.get_selected_text()
        if word == None:
            return
        
        self.focus_other_group()
        self.window.run_command("goto_definition")


class GotoReferenceInOtherPane (ShowInOtherPaneCommand, WithSettings):        

    def run(self):
        word = self.get_selected_text()
        if word == None:
            return
        
        self.focus_other_group()
        self.window.run_command("goto_reference")