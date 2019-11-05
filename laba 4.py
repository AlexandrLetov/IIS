# Логи - фабрика генерирует тип сохранения (txt, xml)
# Строитель выдаёт алерты, например.


class Log(object):
    def write_log(self):
        pass


class Json(Log):
    def write_log(self):
        self.tp = 'json'
        print('Типа записали лог в json')


class Txt(Log):
    def write_log(self):
        self.tp = 'txt'
        print('А тут мы в txt записали')


class Create_Writer():
    def __init__(self, _type):
        self._type = _type

    def Create(self):
        if self._type == 'json':
            return(Json())
        if self._type == 'txt':
            return(Txt())


class Alert():
    def __init__(self):
        self._type = None
        self.text = None

    def __str__(self):
        return '{}  {}'.format(self._type, self.text)


class AbstractBuilder():
    def __init__(self):
        self.Alert = None

    def createNewAlert(self):
        self.Alert = Alert()


class Json_Builder(AbstractBuilder):

    def add_type(self):
        self.Alert._type = "Critical"

    def add_text(self):
        self.Alert.text = "У вас критическая ошибка"


class Txt_Builder(AbstractBuilder):

    def add_type(self):
        self.Alert._type = "Just error"

    def add_text(self):
        self.Alert.text = "Ошибочка"


class Director():
    def __init__(self, builder):
        self._builder = builder

    def constructAlert(self):
        self._builder.createNewAlert()
        self._builder.add_type()
        self._builder.add_text()

    def getAlert(self):
        return self._builder.Alert


Json_Builder = Json_Builder()
director = Director(Json_Builder)
director.constructAlert()
AlertOne = director.getAlert()


Json_Builder = Txt_Builder()
director = Director(Json_Builder)
director.constructAlert()
AlertTwo = director.getAlert()


json_fabric = Create_Writer('json')
log = json_fabric.Create()
log.write_log()

if log.tp == 'json':
    print("Алёрта: ", AlertOne)

txt_fabric = Create_Writer('txt')
log = txt_fabric.Create()
log.write_log()

if log.tp == 'txt':
    print("Алёрта: ", AlertTwo)
