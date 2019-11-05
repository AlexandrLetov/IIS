# Логи - фабрика генерирует тип сохранения (txt, xml)
# Строитель выдаёт алерты, например.


class Log(object):
    def write_log(self):
        pass

class Json(Log):
    def write_log(self):
        print('Типа записали лог в json')


class Txt(Log):
    def write_log(self):
        print('А тут мы в txt записали')


class Writer(object):
    def write_log(self, _type):
        pass


class Create_Writer(Writer):
    def write_log(self, _type):
        if _type == 'json':
            return(Json())
        if _type == 'txt':
            return(Txt())


log1 = Create_Writer()
log1.write_log('json').write_log()
log1.write_log('txt').write_log()
