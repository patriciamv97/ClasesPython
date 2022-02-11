import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class Aplication(Gtk.Window):
    def __init__(self):
        super().__init__(title="Exemplo TreeView con TreeStore")
        self.set_border_width(5)
        modelo = Gtk.TreeStore(str, int, str)

        for avo in range(5):
            punteiroAvo = modelo.append(None, ['Avo', avo, "Sen datos"])
            for pai in range(4):
                punteiroPadre = modelo.append(punteiroAvo, ['Pai', pai, "Lexitimo"])
                for fillo in range(6):
                    modelo.append(punteiroPadre, ['Fillo', fillo, "Lexitimo"])

        trvArboreXenealoxica = Gtk.TreeView(model=modelo)
        trvColumna = Gtk.TreeViewColumn('Parentesco')
        trvArboreXenealoxica.append_column(trvColumna)
        celda = Gtk.CellRendererText()

        celda.set_property("editable", True)
        celda.connect("edited", self.on_celda_edited, modelo)
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 0)
        trvColumna = Gtk.TreeViewColumn("Orde")
        trvArboreXenealoxica.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 1)

        tipoParentesco = Gtk.ListStore(str)
        tipoParentesco.append(["Sen datos"])
        tipoParentesco.append(["Lexitimo"])
        tipoParentesco.append(["Bastardo"])

        celdaCombo = Gtk.CellRendererCombo()
        celdaCombo.set_property("editable", True)
        celdaCombo.set_property("model", tipoParentesco)
        celdaCombo.set_property("text-column", 0)
        celdaCombo.set_property("has-entry", False)
        celdaCombo.connect("edited", self.on_celdaCombo_edited, modelo)
        trvColumnaCombo = Gtk.TreeViewColumn("Combo", celdaCombo, text=2)
        trvArboreXenealoxica.append_column(trvColumnaCombo)

        self.add(trvArboreXenealoxica)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_celdaCombo_edited(self, control, fila, texto, modelo):
        modelo[fila][2] = texto

    def on_celda_edited(self, control, fila, texto, modelo):
        modelo[fila][0] = texto


if __name__ == "__main__":
    Aplication()
    Gtk.main()
