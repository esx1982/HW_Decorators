# Доработать декоратор logger в коде ниже. Должен получиться декоратор, который записывает в файл 'main.log' дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. Функция test_1 в коде ниже также должна отработать без ошибок.
import os
import datetime
from functools import wraps

def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        end = datetime.datetime.now()
        work_time = start - end
        print(f'имя функции = {old_function.__name__},\n'
              f'дата вызова = {start.date()},\n'
              f'время вызова = {start.hour}:{start.minute}:{start.second},\n'
              f'время работы функции = {work_time},\n'
              f'аргументы функции = {args}{kwargs},\n'
              f'возвращаемое значение = {result}.\n')
        with open("task1.log", 'a', encoding="utf-8") as f:
            f.write(f'имя функции = {old_function.__name__},\n'
                    f'дата вызова = {start.date()},\n'
                    f'время вызова = {start.hour}:{start.minute}:{start.second},\n'
                    f'время работы функции = {work_time},\n'
                    f'аргументы функции = {args}{kwargs},\n'
                    f'возвращаемое значение = {result}.\n\n')
        return result
    return new_function

def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()