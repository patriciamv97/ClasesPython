import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ListBoxRowConDatos(Gtk.ListBoxRow):
    def __init__(self, palabra):
        super().__init__()
        self.palabra = palabra
        self.add(Gtk.Label(label=palabra))


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="Ex de uso de ListBox")
        self.set_border_width(5)

        caixaExterna = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(caixaExterna)

        ListBox = Gtk.ListBox()
        ListBox.set_selection_mode(Gtk.SelectionMode.NONE)
        caixaExterna.pack_start(ListBox, True, True, 0)

        fila = Gtk.ListBoxRow()
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila.add(caixaH)
        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixaH.pack_start(caixaV, True, True, 0)
        etiqueta1 = Gtk.Label(label="Data e hora automática", xalign=0)
        etiqueta2 = Gtk.Label(label="Require acceso a interrede2", xalign=0)
        caixaV.pack_start(etiqueta1, True, True, 0)
        caixaV.pack_start(etiqueta2, True, True, 0)

        conmutador = Gtk.Switch()
        conmutador.props.valign = Gtk.Align.CENTER

        caixaH.pack_start(conmutador, False, True, 0)
        ListBox.add(fila)

        fila2 = Gtk.ListBoxRow()
        caixaH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila2.add(caixaH2)

        etiqueta = Gtk.Label(label="Permitir actualizaciones automáticas", xalign=0)
        chkActualizacions = Gtk.CheckButton()
        caixaH2.pack_start(etiqueta, True, True, 0)
        caixaH2.pack_start(chkActualizacions, False, True, 0)
        ListBox.add(fila2)

        fila3 = Gtk.ListBoxRow()
        caixaH3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila3.add(caixaH3)

        etiqueta3 = Gtk.Label(label="Formato data", xalign=0)
        cmbformatoData = Gtk.ComboBoxText()
        cmbformatoData.insert(0, "0", "24-hour")
        cmbformatoData.insert(1, "1", "AM/PM")
        caixaH3.pack_start(etiqueta3, True, True, 0)
        caixaH3.pack_start(cmbformatoData, False, True, 0)

        ListBox.add(fila3)

        ListBox2 = Gtk.ListBox()
        elementos = "Esta é unha ListBox ordeada".split()

        for elemento in elementos:
            ListBox2.add(ListBoxRowConDatos(elemento))

        def ordear(fila1, fila2, datos, notify_destroy):
            return fila1.palabra.lower() > fila2.palabra.lower()

        def filtrar(fila, datos, notify_destroy):
            return False if fila.palabra == "ListBox" else True

        ListBox2.set_sort_func(ordear, None, False)
        ListBox2.set_filter_func(filtrar, None, False)
        ListBox2.connect("row-activated", self.on_row_activated)

        caixaExterna.pack_start(ListBox2, True, True, 0)
        ListBox2.show_all()

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_row_activated(self, ListBox2, fila):
        print(fila.palabra)


if __name__ == "__main__":
    Aplication()
    Gtk.main()
