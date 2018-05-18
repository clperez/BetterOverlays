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
        if (view.sel()[0]).empty(): 
            return ""
        else:
            return view.substr(view.word(view.sel()[0]))

    def focus_other_group(self):
        other_group = self.get_other_group()
        self.window.focus_group(other_group)

    def focus_or_move_to_other_group(self):
        view = self.window.active_view()
        if view == None:
            return
        other_group = self.get_other_group()
        self.window.focus_group(other_group)


class ShowOverlayWithSelectedText (ShowInOtherPaneCommand, WithSettings):        

    def run(self, overlay = "goto", prefix = "", show_files = True, in_other_panel= False):
        word = self.get_selected_text()
        if word == None:
            return
        
        if in_other_panel == True:
            self.focus_other_group()

        self.window.run_command("show_overlay", {"overlay": overlay, "text": prefix + word, "show_files": show_files})
