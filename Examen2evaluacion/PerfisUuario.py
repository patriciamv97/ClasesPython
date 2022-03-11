import gi

from Examen2evaluacion.ConsultaBD import ConexionBD

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplication(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Examen 2ª evaluacion")
        self.set_border_width(5)
        self.set_default_size(400, 200)
        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        caixaV.pack_start(caixaH, False, False, 0)

        self.bd = ConexionBD("perfisUsuarios.bd")
        self.bd.conectaBD()
        self.bd.creaCursor()
        nomesPerfis = self.bd.consultaSenParametros("SELECT idPefil,nomePerfil FROM perfis")
        modelo = Gtk.ListStore(int, str)

        for id, nome in nomesPerfis:
            print(id)
            modelo.append([id, nome])

        comboNomePerfis = Gtk.ComboBox.new_with_model(modelo)

        celda = Gtk.CellRendererText()
        comboNomePerfis.pack_start(celda, True)
        comboNomePerfis.add_attribute(celda, "text", 1)
        caixaH.pack_start(comboNomePerfis, False, False, 0)

        comboNomePerfis.connect("changed", self.on_comboNomePerfis_changed)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_comboNomePerfis_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            idPerfil = modelo[fila][0]
            print(idPerfil)
            dniUsuario = self.bd.consultaConParametros("SELECT dniUsuario FROM perfisUsuario WHERE idPerfil=?",
                                                       idPerfil)
            print(dniUsuario)

            if idPerfil == 2:
                datosUusario1 = self.bd.consultaConParametros("SELECT nome, departamento FROM usuarios WHERE dni=?", dniUsuario[0][0])
                print(datosUusario1)

            else:
                datosUusario3 = self.bd.consultaConParametros("SELECT nome, departamento FROM usuarios WHERE dni=?",dniUsuario[0][0])
                print(datosUusario3[0][1])


if __name__ == "__main__":
    Aplication()
    Gtk.main()
