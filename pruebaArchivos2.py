from abc import(ABCMeta)

class RestoAbs(ABCMeta):

    # Metodo estatico
    @staticmethod
    def evaluarOperadores(numero1, numero2, numero3):
        sonIguales = False
        if numero2 == 0:
            sonIguales = False
        elif numero1 % numero2 == numero3 or numero2 % numero1 == numero3:
            sonIguales = True
        return sonIguales

class pruebaArchivos2:

    def leerArchivo(self, archivo):
        file = open(archivo, 'r')
        lineas = []
        lineas_archivo = []
        for linea in file.readlines():
            lineas.append(linea.replace('\n', '').split("#"))
        file.close()
        for f in range(0, len(lineas)):
            try:
                lineas_archivo.append([int(lineas[f][0]), int(lineas[f][1]), int(lineas[f][2])])
            except ValueError:
                lineas_archivo.append([0, 0, 0])
        return lineas_archivo

    def evaluarOperadores(self, lista):
        resultados = []
        for f in range(0, len(lista)):
            resultados.append(RestoAbs.evaluarOperadores(lista[f][0], lista[f][1], lista[f][2]))
        return resultados

    def guardarResultados(self, entrada, resultados):
        file = open("resultados.csv", 'w')
        file.write('numero1#numero2#numero3\n')
        for f in range(0, len(entrada)):
            linea = str(entrada[f][0]) + ',' + \
                    str(entrada[f][1]) + ',' + str(entrada[f][2]) + \
                    ',' + str(resultados[f]) + '\n'
            file.write(linea)
        file.close()

if __name__ == "__main__":
    prueba = pruebaArchivos2()
    archivo = []
    archivo = prueba.leerArchivo("LISTASDELACLASERESTO.txt")
    resultado = prueba.evaluarOperadores(archivo)
    prueba.guardarResultados(archivo, resultado)