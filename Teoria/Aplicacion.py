import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# Creamos o obxeto ventana

class Aplicacion:

    def __init__(self):
        # Recolle a descricion en Glade y lanza os obxetos y crea o interfaz o mostra e o ten en memoria
        builder = Gtk.Builder()
        builder.add_from_file("Aplicacion.glade")
        fiestra = builder.get_object("fiestra")
        self.txtsaudo = builder.get_object("txtsaudo")
        self.saudo = builder.get_object("saudo")
        self.label = builder.get_object("label")

        sinais = {
            "on_fiestra_destroy": Gtk.main_quit,
            "on_saudo_clicked": self.onSaudoClicked,
            "on_txtsaudo_activate": self.ontxtsaudoActivated
        }

        builder.connect_signals(sinais)
        fiestra.show_all()

    def onSaudoClicked(self, boton):
        nome = self.txtsaudo.get_text()
        self.label.set_text("Me voi ah suisidá" + nome)

    def ontxtsaudoActivated(self, control):
        """


        """


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
# descargar PyGObject en setting project interpreter
