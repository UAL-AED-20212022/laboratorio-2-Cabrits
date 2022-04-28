from LinkedList import LinkedList

class controller:
    def __init__(self):
        self.paises = LinkedList()


    def insert(self, pais_novo, position):
        if position == "start":
            self.paises.insert_at_start(pais_novo)
        elif position == "end":
            self.paises.insert_at_end(pais_novo)
        else:
            self.paises.insert_at_index(position,pais_novo)

    def insert_relative(self,pais_novo, position, elemento):
        if position == "after":
            self.paises.insert_after_item(elemento,pais_novo)
        elif position == "before":
            self.paises.insert_before_item(elemento,pais_novo)

    def print_list(self):
        if self.paises.start_node is None:
            return ""
        n = self.paises.start_node
        s = ""
        while n is not None:
            s += n.get_item() + "\n"
            n = n.ref
        return s


    def check_size(self):
        return self.paises.get_count()


    def delete(self,position):
        if position == "start":
            elim = self.paises.start_node.get_item()
            self.paises.delete_at_start()
            return elim
        elif position == "end":
            elim = self.paises.get_last_node()
            self.paises.delete_at_end()
            return elim
        else:
            elim = position
            self.paises.delete_element_by_value(position)
        return elim

    def isInList(self, pais):
        return self.paises.search_item(pais)