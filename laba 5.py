class Http4XXHandler():
    def __init__(self):
        self.Http404Handler = Http404Handler()
        self.Http403Handler = Http403Handler()

    def handle(self, code):
        if code == 404:
            return self.Http404Handler.handle(code)
        if code == 403:
            return self.Http403Handler.handle(code)


class Http404Handler():
    def handle(self, code):
        return 'Страница не найдена'


class Http403Handler():
    def handle(self, code):
        return 'Доступ закрыт'


class Http500Handler():
    def handle(self, code):
        if code == 500:
            return 'Ошибка сервера'


class Client(object):
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print(f'Ответ: {msg}')
                break
        else:
            print('Код не обработан')


client = Client()
client.add_handler(Http4XXHandler())
client.add_handler(Http500Handler())
client.add_handler(Http403Handler())
client.response(400)
client.response(404)
client.response(500)
client.response(403)
