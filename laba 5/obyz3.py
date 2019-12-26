import abc
from enum import IntEnum
from flask import Flask, render_template, request


class Params:
    def __init__(self):
        self.error_code = None


class Bad_Gateway_2():
    def handle_request(self):
        return f"{str(self)} Код ошибки 'ошибочный шлюз'."


class Errors(IntEnum):
    not_found = 404
    forbidden = 403
    bad_gateway = 502


class Errors_iterator(metaclass=abc.ABCMeta):
    def __init__(self):
        self.next_handler = None

    @abc.abstractmethod
    def handle_request(self, request):
        pass

    def set_next_handler(self, handler):
        self.next_handler = handler


class Not_Found(Errors_iterator):
    def handle_request(self, request):
        if request == Errors.not_found:
            return f"Код ошибки 'страница не найдена'."
        else:
            if self.next_handler is not None:
                return self.next_handler.handle_request(request)


class Forbidden(Errors_iterator):
    def handle_request(self, request):
        if request == Errors.forbidden:
            return f"Код ошибки 'доступ запрещён'"
        else:
            if self.next_handler is not None:
                return self.next_handler.handle_request(request)


class Bad_Gateway(Errors_iterator):
    def handle_request(self, request):
        if request == Errors.bad_gateway:
            return Bad_Gateway_2.handle_request("Делегируем другому обработчику.")
        else:
            if self.next_handler is not None:
                self.next_handler.handle_request(request)


def set_up_chain():
    not_found_handleer = Not_Found()
    forbidden_handler = Forbidden()
    bad_gateway_handler = Bad_Gateway()

    not_found_handleer.set_next_handler(forbidden_handler)
    forbidden_handler.set_next_handler(bad_gateway_handler)

    return not_found_handleer


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        error_code = int(request.form['error_code'])
        chain = set_up_chain()
        result = chain.handle_request(error_code)
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
