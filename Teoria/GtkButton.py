import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion(Gtk.Window):
    def __init__(self):
        self.contador = 0
        super().__init__(title="Exemplo de uso de Gtk.Button")
        # self.set_title("Exemplo de uso de Gtk.Label")
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        # btnBoton = Gtk.Button(label="Etiqueta")
        # btnBoton = Gtk.Button.new_with_label("Etiqueta")

        btnBotonAbrir = Gtk.Button.new_with_mnemonic("_Abrir")
        btnBotonAbrir.connect("clicked", self.on_btnBoton_clicked)
        caixaH.pack_start(btnBotonAbrir, True, True, 0)

        self.add(caixaH)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_btnBoton_clicked(self, boton):
        print("O boton 'Abrir' foi pulsado ")


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
