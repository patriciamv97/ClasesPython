import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class Aplication(Gtk.Window):
    def __init__(self):
        super().__init__(title="Exemplo TreeView con TreeStore")
        self.set_border_width(5)
        modelo = Gtk.TreeStore(str, int)

        for avo in range(5):
            punteiroAvo = modelo.append(None, ['Avo', avo])
            for pai in range(4):
                punteiroPadre = modelo.append(punteiroAvo, ['Pai', pai])
                for fillo in range(6):
                    modelo.append(punteiroPadre, ['Fillo', fillo])

        trvArboreXenealoxica = Gtk.TreeView(model=modelo)
        trvColumna= Gtk.TreeViewColumn('Parentesco')
        trvArboreXenealoxica.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 0)
        trvColumna = Gtk.TreeViewColumn("Orde")
        trvArboreXenealoxica.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 1)

        self.add(trvArboreXenealoxica)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplication()
    Gtk.main()
