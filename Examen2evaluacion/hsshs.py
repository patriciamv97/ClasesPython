import gi
import ConsultaBD

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


class Aplication(Gtk.Window):
    def __init__(self):
        super().__init__(title="Aplicación/perfís")
        self.set_border_width(5)
        self.set_size_request(400, 300)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)

        caixaV.pack_start(caixaH, False, False, 0)

        lblNomes =Gtk.Label(label="Nomes")
        caixaH.pack_start(lblNomes, False, False, 2)

        modeloNomes = Gtk.ListStore(str)

        bbdd = ConsultaBD.ConexionBD("perfisUsuarios.bd")
        bbdd.conectaBD()
        bbdd.creaCursor()

        nomes = bbdd.consultaSenParametros("Select nomePerfil from perfis")
        #print(nomes)

        modeloNomes.append(0)
        for nome in nomes:
            print(nome)
            modeloNomes.append(nome)

        modeloTreeView = Gtk.ListStore(str, str, str)

        self.filtroActual=0
        filtro = modeloTreeView.filter_new()
        filtro.set_visible_func(self.filtroNomesUsuarios)

        twDetalles = Gtk.TreeView(model=filtro)
        detalles = bbdd.consultaSenParametros("select nome, dni, departamento from usuarios where dni in (select dniUsuario from perfisUsuario where idPerfil in(select idPerfil from perfis))")
        print(detalles)
        for datos in detalles:
            modeloTreeView.append(datos)

        for i, titulo in enumerate(["Nomes", "Dni", "Departamento"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(titulo, celda, text=i)
            twDetalles.append_column(columna)
        caixaV.pack_start(twDetalles, True, True, 0)

        comboNomes = Gtk.ComboBox.new_with_model(modeloNomes)
        comboNomes.connect("changed", self.changed_nomes, filtro, modeloTreeView)
        caixaH.pack_start(comboNomes, False, False, 0)
        celda = Gtk.CellRendererText()
        comboNomes.pack_start(celda, True)
        comboNomes.add_attribute(celda, "text", 0)

        btnCrearDocumento = Gtk.Button(label="Informe")
        btnCrearDocumento.connect("clicked", self.clickedButton, bbdd)
        caixaV.pack_start(btnCrearDocumento, False, True, 0)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def filtroNomesUsuarios(self, modelo, fila, datos):
        if(self.filtroActual==0 or None):
            return True
        else:
            return modelo[fila][0] == self.filtroActual

    def changed_nomes(self, combo, filtro, modelo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            nome = modelo[fila][0]
            self.filtroActual = str(nome)
        filtro.refilter()

    def clickedButton(self, boton, bbdd):
        doc = SimpleDocTemplate("Informe.pdf")
        elemento = []
        estilos = getSampleStyleSheet()
        estilo = estilos["Heading2"]
        estilo2 = estilos["Heading1"]
        parrafo = Paragraph("Informe: ", estilo2)
        elemento.append(parrafo)
        elemento.append(Spacer(0,10))
        cabeceras = bbdd.consultaSenParametros("Select "

if __name__ == "__main__":
    Aplication()
    Gtk.main()
