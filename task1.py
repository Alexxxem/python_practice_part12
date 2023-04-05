"""
Задание:

Создайте класс "Friends", который должен содержать данные о людях (их имена) и о связях между ними. Имена представлены в
 виде текстовых строк, чувствительных к регистру. Связи не имеют направлений, то есть, если существует связь "sofia" с
 "nikola", это справедливо и в обратную сторону.

class Friends(connections)

Возвращает новый объект, экземпляр класса Friends. Параметр "connections" имеет тип "итерируемый объект", содержащий
множества (set) с двумя элементами в каждом. Каждая связь содержит два имени в виде текстовых строк. Связи могут
повторяться в параметре инициализации, но в объекте хранятся только уникальные пары. Каждая связь имеет только два
состояния - присутствует или не присутствует.

# >>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
# >>> Friends([{"1", "2"}, {"3", "1"}])

add(connection)

Добавляет связь в объект. Параметр "connection" является множеством (set) из двух имен (строк). Возвращает True, если
заданная связь новая и не присутствует в объекте. Возвращает False, если заданная связь уже существует в объекте.

# >>> f = Friends([{"1", "2"}, {"3", "1"}])
# >>> f.add({"1", "3"})
False
# >>> f.add({"4", "5"})
True

remove(connection)

Удаляет связь из объекта. Параметр "connection" является множеством (set) из двух имен (строк). Возвращает True, если
заданная связь существует в объекте. Возвращает False, если заданная связь не присутствует в объекте.

# >>> f = Friends([{"1", "2"}, {"3", "1"}])
# >>> f.remove({"1", "3"})
True
# >>> f.remove({"4", "5"})
False

names()

Возвращает множество (set) имён. Множество содержит имена, которые имеют хотя бы одну связь.

# >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"})
# >>> f.names()
{"a", "b", "c", "d"}
# >>> f.remove({"d", "c"})
True
# >>> f.names()
{"a", "b", "c"}

connected(name)

Возвращает множество (set) имён, которые связаны с именем, заданным параметром "name". Если "name" не присутствует в
объекте, возвращается пустое множество (set).

# >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"})
# >>> f.connected("a")
{"b", "c"}
# >>> f.connected("d")
set()
# >>> f.remove({"c", "a"})
True
# >>> f.connected("c")
{'b'}

"""


class Friends:
    def __init__(self, connections):
        self.connections = []
        for connection in connections:
            if len(connection) == 2:
                self.add(connection)

    def __repr__(self):
        return f"Friends({self.connections})"

    def add(self, connection):
        if connection in self.connections:
            return False
        self.connections.append(connection)
        return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        return False

    def names(self):
        name_set = set()
        for connection in self.connections:
            name_set.update(connection)
        return name_set

    def connected(self, name):
        connected_set = set()
        for connection in self.connections:
            if name in connection:
                connected_set.update(connection - {name})
        return connected_set


print(Friends([{"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}]))
print(Friends([{"1", "2"}, {"3", "1"}]))

# Add connections
f1 = Friends([{'1', '2'}, {'3', '1'}])
print(f1.add({'1', '3'}))
print(f1.add({'4', '5'}))

# Remove connections
f2 = Friends([{'1', '2'}, {'3', '1'}])
print(f2.remove({'1', '3'}))
print(f2.remove({'4', '5'}))

# Get names that have at least one relationship.
f3 = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
print(f3.names())
print(f3.remove({"d", "c"}))
print(f3.names())

# Get names that have at least one relationship.
f4 = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
print(f4.connected("a"))
print(f4.remove({"c", "a"}))
print(f4.connected("c"))

