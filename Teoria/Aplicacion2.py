import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion:
    def __init__(self):
        wndFiestra = Gtk.Window()
        wndFiestra.set_title("A segunda aplicacion")
        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        wndFiestra.add(caixaV)
        self.txtNome = Gtk.Entry()
        self.txtNome.set_text("Escribe o teu nome")
        self.txtNome.connect("activate", self.ontxtNomeActivated)
        '''
        caixaV.pack_end(self.txtNome, True, False, 6)
        self.lblTexto = Gtk.Label()
        self.lblTexto.set_text("tu nombre")
        caixaV.pack_end(self.lblTexto, True, True, 6)
        self.btnSaudo = Gtk.Button()
        self.btnSaudo.set_label("Saudo")
        self.btnSaudo.connect("clicked", self.onBtnSaudoClicked)
        caixaV.pack_end(self.btnSaudo, False, False, 6)
        '''
        caixaV.pack_start(self.txtNome, True, False, 6)
        self.lblTexto = Gtk.Label()
        self.lblTexto.set_text("tu nombre")
        caixaV.pack_start(self.lblTexto, True, True, 6)
        self.btnSaudo = Gtk.Button()
        self.btnSaudo.set_label("Saudo")
        self.btnSaudo.connect("clicked", self.onBtnSaudoClicked)
        caixaV.pack_start(self.btnSaudo, False, False, 6)

        wndFiestra.connect("destroy", Gtk.main_quit)
        wndFiestra.show_all()

    # aqui el boton introduce el nombre en el label
    def onBtnSaudoClicked(self, boton):
        self.introducirNombreEnLabel()

    # aqui el txt introduce el nombre en el label
    def ontxtNomeActivated(self, control):
        self.introducirNombreEnLabel()

    def introducirNombreEnLabel(self):
        nome = self.txtNome.get_text()
        self.lblTexto.set_text("Hola ".upper() + nome.upper())


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
