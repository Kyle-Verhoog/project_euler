import pygtk
pygtk.require('2.0')
import gtk

clipboard = gtk.clipboard_get()
clipboard.set_text(str(s))
clipboard.store()