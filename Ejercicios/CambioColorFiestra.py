import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__(title="Fiestra cambio color")

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("estilo.css")
        contexto = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        contexto.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        # Tamaño ventana
        # self.set_size_request(200, 150)
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        btnVerde = Gtk.Button(label="Verde")
        btnVerde.connect("clicked", self.on_btnColor_clicked, 'verde')
        caixaH.pack_start(btnVerde, False, False, 2)

        btnAzul = Gtk.Button(label="Azul")
        btnAzul.connect("clicked", self.on_btnColor_clicked, 'azul')
        caixaH.pack_start(btnAzul, False, False, 2)

        btnVermello = Gtk.Button(label="Vermello")
        btnVermello.connect("clicked", self.on_btnColor_clicked, 'vermello')
        caixaH.pack_start(btnVermello, False, False, 2)

        self.add(caixaH)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_btnColor_clicked(self, boton, color):
        if color == "verde":
            self.set_name("winFiestraPrincipal_verde")
        elif color == "azul":
            self.set_name("winFiestraPrincipal_azul")
        elif color == "vermello":
            self.set_name("winFiestraPrincipal_vermello")


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
