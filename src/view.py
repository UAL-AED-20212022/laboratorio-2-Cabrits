from controller import controller


def choice():
    try:
        operation = input()
    except EOFError:
        return None
    if len(operation) == 0:
        return
    else:
        comandos = operation.split(" ")
        comandos[0] = comandos[0].upper()
    return comandos


def cli():
    cont = controller()
    while True:
        operation = choice()

        if operation[0] == "RPI":

            pais_novo = operation[1]
            position = "start"
            cont.insert(pais_novo,position)
            print(cont.print_list())

        elif operation[0] ==  "RPF":

            pais_novo = operation[1]
            position = "end"
            cont.insert(pais_novo,position)
            print(cont.print_list())

        elif operation[0] == "RPDE":

            pais_novo = operation[1]
            elemento = operation[2]
            position = "after"
            cont.insert_relative(pais_novo,position,elemento)
            print(cont.print_list())

        elif operation[0] == "RPAE":

            pais_novo = operation[1]
            elemento = operation[2]
            position = "before"
            cont.insert_relative(pais_novo,position,elemento)
            print(cont.print_list())

        elif operation[0] == "RPII":

            pais_novo = operation[1]
            position = int(operation[2])
            cont.insert(pais_novo,position)
            print(cont.print_list())

        elif operation[0] == "VNE":

            size = cont.check_size()
            print("O número de elemento são "+ str(size)+".")

        elif operation[0] == "VP":
            pais = operation[1]
            if cont.isInList(pais):
                print("O país "+pais+" encontra se na lista.")
            else:
                print("O país "+pais+" não se encontra na lista.")


        elif operation[0] == "EPE":
            elim = cont.delete("start")
            print("O país "+ elim +" foi eliminado da lista.")

        elif operation[0] == "EUE":
            elim = cont.delete("end")
            print("O país "+ elim +" foi eliminado da lista.")

        elif operation[0] == "EP":
            pais = operation[1]
            if cont.isInList(pais):
                elim = cont.delete(pais)
                print("O país "+elim+" foi eliminado da lista.")
            else:
                print("O país "+pais+" não se encontra na lista.")

        else:
            print("Instrucao invalida")
