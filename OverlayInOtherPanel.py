import sublime, sublime_plugin


class WithSettings:
 	_settings = None

# 	def settings(self):
# 		if self._settings is None:
# 			self._settings = sublime.load_settings('OverlayInOtherPanel.sublime-settings')
# 		return self._settings



class ShowInOtherPaneCommand (sublime_plugin.WindowCommand)

    def get_other_group(self):
        group = sublime.window.active_group()
        if group == None:
            # If we're in an empty group, there's no active group
            return

        num_groups = sublime.window.num_groups()
        return (group + 1) % num_groups

    def get_selected_text(self):
        view = self.window.active_view()
        sel = view.sel()[0]
        return view.substr(view.word(sel))

    def focus_other_group(self):
        other_group = get_other_group()
        self.window.focus_group(other_group)


class ShowFilesOverlayInOtherPane (ShowInOtherPaneCommand, WithSettings):        

	def run(self):
   		# if create_new_if_necessary is None:
		# create_new_if_necessary = self.settings().get('create_new_pane_if_necessary')
        
        word = self.get_selected_text()
        self.focus_other_group()

        self.window.run_command("show_overlay", {"overlay": "goto", "text": word, "show_files": True})


class GotoDefinitionInOtherPane (ShowInOtherPaneCommand, WithSettings):        

    def run(self):
        # if create_new_if_necessary is None:
        # create_new_if_necessary = self.settings().get('create_new_pane_if_necessary')
        word = self.get_selected_text()
        self.focus_other_group()

        self.window.run_command("goto_definition")


class GotoReferenceInOtherPane (ShowInOtherPaneCommand, WithSettings):        

    def run(self):
        # if create_new_if_necessary is None:
        # create_new_if_necessary = self.settings().get('create_new_pane_if_necessary')
        word = self.get_selected_text()
        self.focus_other_group()

        self.window.run_command("goto_reference")