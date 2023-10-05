import os
import argparse

CWD = os.path.abspath(os.path.dirname(__file__))
os.chdir(CWD)

import logging
import config as cfg
import src.app as app


logging.basicConfig(level=logging.INFO, 
                    filename='logging.log', 
                    filemode='a', 
                    encoding='UTF-8',
                    format="%(asctime)s %(levelname)s %(message)s")

parser = argparse.ArgumentParser(prog='Калитка Престиж',
                                 description='Генерирует чертижи для калиток Аполло')
parser.add_argument('--debug', action='store_true', help='Режим отладки')
parser.add_argument('--order', help='Номер заказа')
parser.add_argument('--customer', help='Заказчик')
parser.add_argument('--date', help='Дата готовности')
parser.add_argument('--engineer', help='Инженер')
parser.add_argument('--width', help='Ширина калитки')
parser.add_argument('--height', help='Высота калитки')
parser.add_argument('--open', help='Направление открытия')
parser.add_argument('--side', help='Сторона петель')
parser.add_argument('--frame_type', help='Тип коробки')
parser.add_argument('--cliarance', help='Просвет под створкой')
parser.add_argument('--bridge', help='Тип перемычки')
parser.add_argument('--bridge_height', help='Высота фрамуги')
parser.add_argument('--fill', help='Тип заполнения')
parser.add_argument('--frame_color', help='Цвет рамы')
parser.add_argument('--color_type', help='Структура покраски рамы')
parser.add_argument('--fill_color_in', help='Цвет заполнения изнутри')
parser.add_argument('--fill_color_out', help='Цвет заполнения снаружи')
parser.add_argument('--lock', help='Замок')
parser.add_argument('--auto_closer', help='Доводчик')
parser.add_argument('--handle_in', help='Вид ручки изнутри')
parser.add_argument('--handle_out', help='Вид ручки снаружи')
parser.add_argument('--batten', help='Нащельник')
parser.add_argument('--comments', help='Комментарий')


debug_condition = {'order': '321',
                   'customer': 'Рога и копыта ООО',
                   'date': '02.04.2020',
                   'engineer': 'Иванов Иван',
                   'width': '1000',
                   'height': '2000',
                   'open': cfg.OUT,
                   'side': cfg.LEFT,
                   'frame_type': cfg.FRAME_TYPES[0],
                   'cliarance': '50',
                   'bridge': cfg.BRIDGE_Y,
                   'bridge_height': '0',
                   'fill': list(cfg.FILLING.keys())[0],
                   'frame_color': '7016',
                   'color_type': cfg.COLOR_TYPES[0],
                   'fill_color_in': '8014',
                   'fill_color_out': '8017',
                   'lock': tuple(cfg.LOCKS)[1],
                   'auto_closer': cfg.NO,
                   'flexible_tube': cfg.FLEXIBLE_TUBES[0],
                   'handle_in': cfg.HANDLES[0],
                   'handle_out': cfg.HANDLES[0],
                   'batten': cfg.NO,
                   'comments': 'comments  comments  comments  comments  comments  comments  comments  comments  comments  comments  comments  comments',
                   }

if __name__ == "__main__":
    args = parser.parse_args()
    condition = {key:value for (key, value) in vars(args).items() if value != None and key != 'debug'}
    if args.debug:
        debug_condition.update(condition)
        condition = debug_condition
        print()
        print('----- Run in DEBUG mode -----')
        print()
        print(condition)
    app.run(condition)
