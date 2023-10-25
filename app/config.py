import os
import src.ral as ral
from src.calculators import CalculatorBridgeN, CalculatorBridgeY, CalculatorBridgeT, CalculatorBridgeYS

VERSION = "v-2.0 25.09.23"

# текущий каталог
CWD = os.getcwd()

# файл логов
LOG_FILE = os.path.join(CWD, 'logging.log')

# таблица цветов
RAL_TABLE = ral.RAL_TABLE

# домашняя папка пользователя
HOMEDIR = os.path.expanduser('~')

# каталоги с ресурсами
FOLDERS = {
    'icons': os.path.join(CWD, 'res', 'icons'),
    'images': os.path.join(CWD, 'res', 'images'),
    'logo_images': os.path.join(CWD, 'res', 'images', 'logo'),
    'top_images': os.path.join(CWD, 'res', 'images', 'top'),
    'back_images': os.path.join(CWD, 'res', 'images', 'back'),
    'sketch_images': os.path.join(CWD, 'res', 'images', 'sketch'),
    'fonts': os.path.join(CWD, 'res', 'fonts'),
}

def get_filepath(folder, filename):
    return os.path.join(FOLDERS[folder], filename)

# параметры окна
GUI = {
    'title': 'Калитка ПРЕСТИЖ',
    'size_text': [24, 1],
    'size_input': [30, 1],
    'size_combo': [28, 1],
    'size_multiline': [54, 5],
    'options': {
        'font': [
            'calibri',
            '10'
        ],
        'margins': (2, 1),
        'element_padding': (0, 1),
        'icon': get_filepath('icons', 'logo.ico'),
    },
    'form_padding': (3, 0),
    'text_padding': (1, 4),
    'theme': 'Default1',
    'submit_color': 'red',
}

# параметры pdf файла
PDF = {
    'version': VERSION,
    'logo_file': get_filepath('logo_images', 'apollo_logo.png'),
    'font_file': get_filepath('fonts', 'JetBrainsMono-Regular.ttf'),
    'font_name': 'JetBrainsMono',
    'font_size_main': 10,
    'font_size_header': 16,
    'logo_size': 12,
    'table_line_h': 6,
    'table_label_w': 30,
    'text_line_h': 5,
    'text_indent': 5,
}

# направление открытия
IN = 'Во двор'
OUT = 'На улицу'
OPEN = (
    IN,
    OUT,
)

# да, нет
NO = 'НЕТ'
YES = 'ДА'

# сторона петель
LEFT = 'Слева'
RIGHT = 'Справа'
SIDE = (
    LEFT,
    RIGHT,
)

# типы рам
BRIDGE_Y = 'С перемычкой'
BRIDGE_YS = 'С перемычкой и порогом'
BRIDGE_N = 'Без перемычки'
BRIDGE_T = 'С фрамугой'
BRIDGES = (
    BRIDGE_N,
    BRIDGE_Y,
    BRIDGE_YS,
    BRIDGE_T,
)

# типы покраски
COLOR_TYPES = (
    'Шагрень',
    'Матовый',
    'Глянец'
)

#нащельники
BATTENS = (
    NO,
    '30х30 (сталь)',
    'AES 30х20 (алюм)',
)


# ручки
HANDLES = (
    NO,                 #0
    'Грибок',           #1
    'Скоба',            #2
    'Нажимная Dorma',   #3
    'Круглая Dorma',    #4
    'Заказчика',        #5
)

# гибкие переходы
FLEXIBLE_TUBES = (
    NO,     # 0
    YES,    # 1
)

#замки
LOCKS = {
    NO: {
        'handle_in': HANDLES[0],
        'handle_out': HANDLES[0],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
    'CISA/ISEO накладной': {
        'handle_in': HANDLES[0],
        'handle_out': HANDLES[1],
        'flexible_tube': FLEXIBLE_TUBES[1],
    },
    'ПОЛИС накладной': {
        'handle_in': HANDLES[1],
        'handle_out': HANDLES[1],
        'flexible_tube': FLEXIBLE_TUBES[1],
    },
    'CISA/ISEO врезной': {
        'handle_in': HANDLES[3],
        'handle_out': HANDLES[4],
        'flexible_tube': FLEXIBLE_TUBES[1],
    },
    'Эл.защелка': {
        'handle_in': HANDLES[3],
        'handle_out': HANDLES[4],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
    'Механический APEX': {
        'handle_in': HANDLES[3],
        'handle_out': HANDLES[3],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
    'Площадка под замок': {
        'handle_in': HANDLES[1],
        'handle_out': HANDLES[1],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
    'Заказчика': {
        'handle_in': HANDLES[0],
        'handle_out': HANDLES[0],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
}

# тип коробки
FR_DIRECT = 'Торцевая'
FR_ANGEL = 'Угловая'
FRAME_TYPES = (
    FR_DIRECT,
    FR_ANGEL,
)

# конструктивы рам
F20 = 'f20'
F2020 = 'f20+20'
F40 = 'f40'
F60 = 'f60'
FGR = 'fGR'

DESIGNS = {
    # f20
    # out+left
    F20+OUT+LEFT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f20_out_left_y.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_left_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+LEFT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f20_out_left_n.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_left_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+LEFT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f20_out_left_t.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_left_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+LEFT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f20_out_left_ys.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_left_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    # out+right
    F20+OUT+RIGHT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f20_out_right_y.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_right_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+RIGHT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f20_out_right_n.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_right_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+RIGHT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f20_out_right_t.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_right_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+RIGHT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f20_out_right_ys.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_right_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    # in+left
    F20+IN+LEFT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f20_in_left_y.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_left_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+LEFT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f20_in_left_n.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_left_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+LEFT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f20_in_left_t.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_left_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+LEFT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f20_in_left_ys.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_left_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    # in+right
    F20+IN+RIGHT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f20_in_right_y.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_right_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+RIGHT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f20_in_right_n.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_right_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+RIGHT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f20_in_right_t.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_right_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+RIGHT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f20_in_right_ys.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_right_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    # f2020
    # out+left
    F2020+OUT+LEFT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f2020_out_left_y.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_left_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+LEFT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f2020_out_left_n.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_left_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+LEFT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f2020_out_left_t.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_left_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+LEFT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f2020_out_left_ys.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_left_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # out+right
    F2020+OUT+RIGHT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f2020_out_right_y.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_right_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+RIGHT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f2020_out_right_n.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_right_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+RIGHT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f2020_out_right_t.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_right_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+RIGHT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f2020_out_right_ys.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_right_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # in+left
    F2020+IN+LEFT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f2020_in_left_y.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_left_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+LEFT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f2020_in_left_n.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_left_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+LEFT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f2020_in_left_t.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_left_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+LEFT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f2020_in_left_ys.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_left_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # in+right
    F2020+IN+RIGHT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f2020_in_right_y.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_right_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+RIGHT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f2020_in_right_n.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_right_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+RIGHT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f2020_in_right_t.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_right_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+RIGHT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f2020_in_right_ys.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_right_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # f40
    # out+left
    F40+OUT+LEFT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f40_out_left_y.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_left_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+LEFT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f40_out_left_n.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_left_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+LEFT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f40_out_left_t.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_left_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+LEFT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f40_out_left_ys.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_left_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # out+right
    F40+OUT+RIGHT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f40_out_right_y.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_right_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+RIGHT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f40_out_right_n.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_right_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+RIGHT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f40_out_right_t.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_right_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+RIGHT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f40_out_right_ys.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_right_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # in+left
    F40+IN+LEFT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f40_in_left_y.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_left_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+LEFT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f40_in_left_n.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_left_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+LEFT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f40_in_left_t.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_left_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+LEFT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f40_in_left_ys.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_left_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # in+right
    F40+IN+RIGHT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f40_in_right_y.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_right_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+RIGHT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f40_in_right_n.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_right_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+RIGHT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f40_in_right_t.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_right_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+RIGHT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f40_in_right_ys.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_right_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # f60
    # out+left
    F60+OUT+LEFT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f60_out_left_y.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_left_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+LEFT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f60_out_left_n.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_left_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+LEFT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f60_out_left_t.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_left_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+LEFT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f60_out_left_ys.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_left_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    # out+right
    F60+OUT+RIGHT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f60_out_right_y.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_right_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+RIGHT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f60_out_right_n.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_right_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+RIGHT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f60_out_right_t.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_right_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+RIGHT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f60_out_right_ys.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_right_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    # in+left
    F60+IN+LEFT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f60_in_left_y.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_left_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+LEFT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f60_in_left_n.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_left_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+LEFT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f60_in_left_t.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_left_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+LEFT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f60_in_left_ys.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_left_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    # in+right
    F60+IN+RIGHT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'f60_in_right_y.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_right_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+RIGHT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'f60_in_right_n.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_right_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+RIGHT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'f60_in_right_t.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_right_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+RIGHT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'f60_in_right_ys.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_right_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    # fGR
    # out+left
    FGR+OUT+LEFT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'fgr_out_left_y.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_left_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+LEFT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'fgr_out_left_n.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_left_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+LEFT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'fgr_out_left_t.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_left_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+LEFT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'fgr_out_left_ys.png'),
        'open_view': get_filepath('top_images', 't_view_out_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_left_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    # out+right
    FGR+OUT+RIGHT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'fgr_out_right_y.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_right_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+RIGHT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'fgr_out_right_n.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_right_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+RIGHT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'fgr_out_right_t.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_right_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+RIGHT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'fgr_out_right_ys.png'),
        'open_view': get_filepath('top_images', 't_view_out_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_right_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    # in+left
    FGR+IN+LEFT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'fgr_in_left_y.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_left_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+LEFT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'fgr_in_left_n.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_left_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+LEFT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'fgr_in_left_t.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_left_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+LEFT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'fgr_in_left_ys.png'),
        'open_view': get_filepath('top_images', 't_view_in_left.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_left_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    # in+right
    FGR+IN+RIGHT+BRIDGE_Y: {
        'sketch': get_filepath('sketch_images', 'fgr_in_right_y.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_y_right_direct.png'),
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+RIGHT+BRIDGE_N: {
        'sketch': get_filepath('sketch_images', 'fgr_in_right_n.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_n_right_direct.png'),
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+RIGHT+BRIDGE_T: {
        'sketch': get_filepath('sketch_images', 'fgr_in_right_t.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_t_right_direct.png'),
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+RIGHT+BRIDGE_YS: {
        'sketch': get_filepath('sketch_images', 'fgr_in_right_ys.png'),
        'open_view': get_filepath('top_images', 't_view_in_right.png'),
        'back_view': get_filepath('back_images', 'b_view_bridge_ys_right_direct.png'),
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
}

# заполнения
FILLING = {
    'AG/77': F20,
    'PD/77': F20,
    'AER55/S': F20,
    'AER55/mS': F20,
    'Профлист 1ст': F20,
    'Профлист 2ст': F2020,
    'Сайдинг': F2020,
    'сэндвич-панель S-гофр DH': F40,
    'Заказчика 10мм': F20,
    'Заказчика 20мм': F20,
    'Заказчика 20мм+20мм': F20,
    'Заказчика 40мм': F40
    }

# описание виджетов окна
WIDGETS = {
    'order': {
        'text': '№ Заказа',
        'values': None,
    },
    'engineer': {
        'text': 'Инженер',
        'values': None
    },
    'customer': {
        'text': 'Заказчик',
        'values': None
    },
    'date': {
        'text': 'Дата готовности',
        'values': None
    },
    'width': {
        'text': 'Ширина проема, мм',
        'values': None,
        'valid': ('int',),
    },
    'height': {
        'text': 'Высота полотна, мм',
        'values': None,
        'int': True,
        'valid': ('int',),
        'max': 3000,
    },
    'cliarance': {
        'text': 'Просвет, мм',
        'values': None,
        'int': True,
        'valid': ('int',),
    },
    'bridge': {
        'text': 'Перемычка',
        'values': BRIDGES,
        'valid': ('in_list',),
    },
    'bridge_height': {
        'text': 'Высота фрамуги, мм',
        'values': None,
        'valid': ('int',),
    },
    'frame_type': {
        'text': 'Тип рамы',
        'values': FRAME_TYPES,
        'valid': ('in_list',),
    },
    'open': {
        'text': 'Открытие',
        'values': OPEN,
        'valid': ('in_list',),
    },
    'side': {
        'text': 'Петли (вид со двора)',
        'values': SIDE,
        'valid': ('in_list',),
    },
    'frame_color': {
        'text': 'Цвет рамы',
        'values': None
    },
    'fill': {
        'text': 'Наполнение',
        'values': tuple(FILLING),
        'valid': ('in_list',),
    },
    'fill_color_in': {
        'text': 'Цвет наполнения внутри',
        'values': None
    },
    'fill_color_out': {
        'text': 'Цвет наполнения снаружи',
        'values': None
    },
    'color_type': {
        'text': 'Тип покраски',
        'values': COLOR_TYPES,
    },
    'lock': {
        'text': 'Замок',
        'values': tuple(LOCKS),
    },
    'steelwire': {
        'text': 'Сталька',
        'values': (YES, NO),
    },
    'flexible_tube': {
        'text': 'Гибкий переход',
        'values': FLEXIBLE_TUBES,
    },
    'auto_closer': {
        'text': 'Доводчик',
        'values': (YES, NO),
    },
    'handle_in': {
        'text': 'Ручка изнутри',
        'values': HANDLES,
    },
    'handle_out': {
        'text': 'Ручка снаружи',
        'values': HANDLES,
    },
    'batten': {
        'text': 'Нащельник',
        'values': BATTENS,
    },
    'batten_lenght': {
        'text': 'Длина нащельника, мм',
        'values': None
    },
    'batten_num': {
        'text': 'Количество нащельников, шт',
        'values': None
    },
    'comments': {
        'text': '',
        'values': '>Text<'
    }
}
