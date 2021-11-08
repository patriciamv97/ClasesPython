import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__(title="Exemplo de uso de Gtk.Label")
        # self.set_title("Exemplo de uso de Gtk.Label")
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        caixaV_esquerda = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        caixaV_dereita = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        caixaH.pack_start(caixaV_esquerda, True, True, 0)
        caixaH.pack_start(caixaV_dereita, True, True, 0)

        etiqueta = Gtk.Label(label="Etiqueta normal")
        caixaV_esquerda.pack_start(etiqueta, True, True, 0)

        etiqueta2 = Gtk.Label(label="Etiqueta con texto xustificando a esquera.\nCon múltiples liñas \nAs liñas van a "
                                    "esquerda")
        etiqueta2.set_justify(Gtk.Justification.LEFT)
        caixaV_esquerda.pack_start(etiqueta2, True, True, 0)

        etiqueta3 = Gtk.Label(label="En este caso é etiqueta line-wraper.Esta "
                                    "o texto non nos colle no ancho "
                                    "poño varias cadeas de texto "
                                    "que van a ser unidas.\n"
                                    "Isto peromite múltiples parágrfos e engade "
                                    "bastantestes     espazos extras")
        etiqueta3.set_line_wrap(True)
        etiqueta3.set_max_width_chars(32)
        caixaV_dereita.pack_start(etiqueta3, True, True, 0)

        etiqueta4 = Gtk.Label(label="En este caso é etiqueta line-wraper.Esta "
                                    "o texto non nos colle no ancho "
                                    "poño varias cadeas de texto "
                                    "que van a ser unidas.\n"
                                    "Isto permite múltiples parágrfos e engade "
                                    "bastantestes     espazos extras")
        etiqueta4.set_line_wrap(True)
        etiqueta4.set_justify(Gtk.Justification.FILL)
        etiqueta4.set_max_width_chars(32)
        caixaV_dereita.pack_start(etiqueta4, True, True, 0)

        etiqueta5 = Gtk.Label()
        etiqueta5.set_markup("O texto pode ter <small>pequeno</small>, <big>grande</big>,"
                             "<b>negrita</b>, <i>cursiva</i>, e apuntar cara a"
                             '<a href="https://www.gtk.org"'
                             'title = Pulsa para saber mais">interrede</a>')
        caixaV_dereita.pack_start(etiqueta5, True, True,0)
        self.add(caixaH)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
