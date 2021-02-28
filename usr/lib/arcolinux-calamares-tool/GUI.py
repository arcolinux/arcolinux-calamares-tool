# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

def GUI(self, Gtk, GdkPixbuf, fn):

    # ======================================================================
    #                   CONTAINERS
    # ======================================================================

    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    self.add(self.vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # ======================================================================
    #                           BOX 1
    # ======================================================================

    lbl1 = Gtk.Label(label="Select your proferred filesystem: ")
    self.fileSystem = Gtk.ComboBoxText()
    self.fileSystem.set_size_request(280, 0)

    for i in range(len(fn.fs)):
        self.fileSystem.append_text(fn.fs[i])
    self.fileSystem.set_active(0)

    hbox1.pack_start(lbl1, False, False, 0)
    hbox1.pack_end(self.fileSystem, False, False, 0)

    # ======================================================================
    #                       BUTTONS
    # ======================================================================
    btnCancel = Gtk.Button(label="Close")
    btnCancel.connect('clicked', self.on_close_clicked)
    btnOK = Gtk.Button(label="Save")
    btnOK.connect('clicked', self.on_save_clicked)

    hbox2.pack_end(btnCancel, False, False, 0)
    hbox2.pack_end(btnOK, False, False, 0)

    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================

    self.vbox.pack_start(hbox1, False, False, 0)  # Options
    self.vbox.pack_end(hbox2, False, False, 7)  # Buttons
