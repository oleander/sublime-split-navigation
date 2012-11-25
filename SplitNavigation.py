import sublime, sublime_plugin

def focusNext(win):
	act = win.active_group()
	num = win.num_groups()
	act += 1

	if act >= num:
		act = 0
	
	win.focus_group(act)

	if len(win.views_in_group(act)) == 0:
		focusNext(win)

def focusPrev(win):
	act = win.active_group()
	num = win.num_groups()
	act -= 1

	if act < 0:
		act = num - 1
	
	win.focus_group(act)

	if len(win.views_in_group(act)) == 0:
		focusPrev(win)


class SplitNavigationCommand(sublime_plugin.TextCommand):

	def run(self, edit, direction):
		win = self.view.window()
		if direction == "up":
			focusNext(win)
		else:
			focusPrev(win)
