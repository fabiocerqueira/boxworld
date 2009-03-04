#!/usr/bin/python
import sys

try:
    import pygtk
    pygtk.require("2.0")
except:
    pass

try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)

class MapEditor(object):
    def __init__(self):
        #Set the Glade file
        self.gladefile = "mapeditor.glade"
        self.wTree = gtk.glade.XML(self.gladefile)

        dic = {
                 "on_winMapEditor_destroy" : gtk.main_quit
            }

        self.wTree.signal_autoconnect(dic)


if __name__ == "__main__":
    hwg = MapEditor()
    gtk.main()


