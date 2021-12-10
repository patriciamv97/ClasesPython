import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="Glade Layout")
        self.set_border_width(5)

        noteBook = Gtk.Notebook()
        self.add(noteBook)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(caixaV, Gtk.Label(label="Xeral"))

        caixaV1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(caixaV1, Gtk.Label(label="Empaquetado"))

        caixaV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(caixaV2, Gtk.Label(label="Comun"))

        caixaV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        noteBook.append_page(caixaV2, Gtk.Label(label="Sinais"))

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        # caixaV.add(caixaH)

        lblId = Gtk.Label(label="ID : ")
        self.entryId = Gtk.Entry()
        caixaH.pack_start(lblId, False, False, 0)
        caixaH.pack_start(self.entryId, True, True, 0)
        caixaV.pack_start(caixaH, True, True, 0)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        lblapariencia = Gtk.Label()
        lblapariencia.set_markup("<b>Apariencia</b>")
        lblapariencia.props.xalign = 0
        caixaV.pack_start(lblapariencia, True, True, 2)

        rede = Gtk.Grid()
        lblEtiqueta = Gtk.Label()
        lblEtiqueta.set_markup("<i>Etiqueta : </i>")
        rede.add(lblEtiqueta)
        caixa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        caixaV.pack_start(rede, True, True, 0)
        txvEtiqueta = Gtk.TextView()
        txvEtiqueta.set_size_request(300, 50)
        caixa.pack_start(txvEtiqueta, True, True, 0)
        botonEditarEtiqueta = Gtk.Button()
        imaxe = Gtk.Image.new_from_icon_name("preferences-other", Gtk.IconSize.BUTTON)
        botonEditarEtiqueta.set_image(imaxe)

        caixa.pack_start(botonEditarEtiqueta, True, False, 0)
        rede.attach_next_to(caixa, lblEtiqueta, Gtk.PositionType.RIGHT, 3, 2)

        rbtAtributes = Gtk.RadioButton(label="Atributos :")
        rede.attach(rbtAtributes, 0, 2, 1, 1)
        btnEditarAtributos = Gtk.Button(label="Editar atributos")
        rede.attach_next_to(btnEditarAtributos, rbtAtributes, Gtk.PositionType.RIGHT, 3, 1)
        rbtUsarMarcado = Gtk.RadioButton(label="Usar marcado")
        rede.attach(rbtUsarMarcado, 0, 3, 2, 1)

        rbtPatron = Gtk.RadioButton(label="Patron")
        rede.attach(rbtPatron, 0, 4, 1, 1)
        txtPatron = Gtk.Entry()
        rede.attach(txtPatron, 2, 4, 2, 1)

        lblapariencia = Gtk.Label()
        lblapariencia.set_markup("<b>Label Behaviour</b>")
        lblapariencia.props.xalign = 0
        caixaV.pack_start(lblapariencia, True, True, 2)

        rede = Gtk.Grid()
        caixaV.pack_start(rede, True, True, 0)

        chkButton = Gtk.CheckButton(label="Seleccionable")
        rede.attach(chkButton, 0, 1, 1, 1)
        chkButton = Gtk.CheckButton(label="Seguir los enlaces visitados")
        rede.attach(chkButton, 1, 1, 1, 1)
        chkButton = Gtk.CheckButton(label="Utilizar subrayado")
        rede.attach(chkButton, 0, 2, 1, 1)

        txtComportamentoEtiqueta = Gtk.Entry()
        rede.attach_next_to(txtComportamentoEtiqueta, chkButton, Gtk.PositionType.RIGHT, 1, 1)

        builder = Gtk.Builder()
        builder.add_from_file("Cadro.glade")
        caixaGlade = builder.get_object("caixaGlade")
        cmdElipsis = builder.get_object("cmdElipsis")

        sinais = {"on_cmdElipsis_changed": self.on_cmdElipsis_changed}
        builder.connect_signals(sinais)
        caixaV.pack_start(caixaGlade, True, True, 0)

        botonEditarEtiqueta.connect("clicked", self.on_btnEditarEtiqueta_clicked)
        cmdElipsis.append_text("Start")
        cmdElipsis.append_text("Midle")
        cmdElipsis.append_text("End")

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_cmdElipsis_changed(self, control):
        self.entryId.set_text(control.get_active_text())

    def on_btnEditarEtiqueta_clicked(self, control):
        self.entryId.set_text("Boton pulsado")


if __name__ == "__main__":
    Aplication()
    Gtk.main()
