import os
import src.ral as ral
from src.calculators import CalculatorBridgeN, CalculatorBridgeY, CalculatorBridgeT, CalculatorBridgeYS

VERSION = "v-2.3 10.03.2024"

# текущий каталог
CWD = os.getcwd()

# файл логов
LOG_FILE = os.path.join(CWD, 'logging.log')

# таблица цветов
RAL_TABLE = ral.RAL_TABLE

# домашняя папка пользователя
HOMEDIR = os.path.expanduser('~')

# общий файл хранения настроек
SETTINGS_FILENAME = 'apollo_door_settings.json'

# каталоги с ресурсами
FOLDERS = {
    'icons': os.path.join(CWD, 'res', 'icons'),
    'images': os.path.join(CWD, 'res', 'images'),
    'logo_images': os.path.join(CWD, 'res', 'images', 'logo'),
    'open_view': os.path.join(CWD, 'res', 'images', 'open_view'),
    'open_preview': os.path.join(CWD, 'res', 'images', 'open_view', 'preview'),
    'back_view': os.path.join(CWD, 'res', 'images', 'back_view'),
    'back_preview': os.path.join(CWD, 'res', 'images', 'back_view', 'preview'),
    'frame_view': os.path.join(CWD, 'res', 'images', 'frame_view'),
    'frame_preview': os.path.join(CWD, 'res', 'images', 'frame_view', 'preview'),
    'sketchs': os.path.join(CWD, 'res', 'images', 'sketch'),
    'fonts': os.path.join(CWD, 'res', 'fonts'),
}

def get_filepath(folder, filename):
    return os.path.join(FOLDERS[folder], filename)

# параметры окна
GUI = {
    'title': 'Калитка ПРЕСТИЖ | ' + VERSION,
    'size_text': [24, 1],
    'size_input': [30, 1],
    'size_combo': [28, 1],
    'size_multiline': [54, 5],
    'size_preview_open': (120, 150),
    'size_preview_back': (120, 150),
    'size_preview_frame': (120, 150),
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
IN = 'во двор'
OUT = 'на улицу'
OPEN = (
    IN,
    OUT,
)

# да, нет
NO = 'НЕТ'
YES = 'ДА'

# сторона петель
LEFT = 'слева'
RIGHT = 'справа'
SIDE = (
    LEFT,
    RIGHT,
)

# типы рам
BRIDGE_Y = 'с перемычкой'
BRIDGE_YS = 'с перемычкой и с порогом'
BRIDGE_N = 'без перемычки'
BRIDGE_T = 'с фрамугой'
BRIDGES = (
    BRIDGE_N,
    BRIDGE_Y,
    BRIDGE_YS,
    BRIDGE_T,
)

# типы покраски
COLOR_TYPES = (
    'шагрень',
    'матовый',
    'глянец'
)

#нащельники
BATTENS = (
    NO,
    '30х30 (сталь)',
    'AES 30x20 (алюминий)',
)


# ручки
HANDLES = (
    NO,                                 #0
    'Грибок в цвет',                    #1
    'Скоба в цвет',                     #2
    'Изогнутая 330мм в цвет',           #3
    'Изогнутая 330мм нерж.',            #4
    'Штанга квадрат 1200мм в цвет',     #5
    'Штанга квадрат 600мм в цвет',      #6
    'Штанга цилиндр 400мм нерж.',       #7
    'Штанга цилиндр 500мм в цвет',      #8
    'Dorma Pure нажимная (изогнутая)',  #9
    'Dorma Pure нажимная (прямая)',     #10
    'Dorma Pure (шар)',                 #11
    '(Заказчика)',                      #12
)

# гибкие переходы
FLEXIBLE_TUBES = (
    NO,     # 0
    YES,    # 1
)

#замки
LOCKS = {
    NO: {
        'handle_in': HANDLES[1],
        'handle_out': HANDLES[1],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
    'накладной электромех. (Италия)': {
        'handle_in': HANDLES[0],
        'handle_out': HANDLES[6],
        'flexible_tube': FLEXIBLE_TUBES[1],
    },
    'накладной электромех. ПОЛИС': {
        'handle_in': HANDLES[1],
        'handle_out': HANDLES[1],
        'flexible_tube': FLEXIBLE_TUBES[1],
    },
    'врезной электромех. (Италия)': {
        'handle_in': HANDLES[10],
        'handle_out': HANDLES[11],
        'flexible_tube': FLEXIBLE_TUBES[1],
    },
    'электромеханическая защелка': {
        'handle_in': HANDLES[10],
        'handle_out': HANDLES[11],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
    'врезной механический (ключ/барашек)': {
        'handle_in': HANDLES[10],
        'handle_out': HANDLES[10],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
    'врезной механический (ключ/ключ)': {
        'handle_in': HANDLES[10],
        'handle_out': HANDLES[10],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
    'электромагнитный ML-395': {
        'handle_in': HANDLES[1],
        'handle_out': HANDLES[1],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
    'Площадка под замок': {
        'handle_in': HANDLES[0],
        'handle_out': HANDLES[0],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
    'Заказчика': {
        'handle_in': HANDLES[0],
        'handle_out': HANDLES[0],
        'flexible_tube': FLEXIBLE_TUBES[0],
    },
}

# тип коробки
FR_DIRECT = 'торцевая'
FR_ANGEL = 'угловая'
FRAME_TYPES = (
    FR_DIRECT,
    FR_ANGEL,
)

# файлы вида рамы
FRAME_VIEW_FILENAMES = {
    FR_DIRECT: 'direct.png',
    FR_ANGEL: 'angel.png',
}

# файлы вида открытия
OPEN_VIEW_FILENAMES = {
    LEFT+IN: 'left_in.png',
    LEFT+OUT: 'left_out.png',
    RIGHT+IN: 'right_in.png',
    RIGHT+OUT: 'right_out.png',
}

# файлы общего вида
BACK_VIEW_FILENAMES = {
    BRIDGE_N+LEFT: 'bridge_n_left_direct.png',
    BRIDGE_N+RIGHT: 'bridge_n_right_direct.png',
    BRIDGE_Y+LEFT: 'bridge_y_left_direct.png',
    BRIDGE_Y+RIGHT: 'bridge_y_right_direct.png',
    BRIDGE_YS+LEFT: 'bridge_ys_left_direct.png',
    BRIDGE_YS+RIGHT: 'bridge_ys_right_direct.png',
    BRIDGE_T+LEFT: 'bridge_t_left_direct.png',
    BRIDGE_T+RIGHT: 'bridge_t_right_direct.png',
}

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
        'sketch': 'f20_out_left_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+LEFT+BRIDGE_N: {
        'sketch': 'f20_out_left_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+LEFT+BRIDGE_T: {
        'sketch': 'f20_out_left_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+LEFT+BRIDGE_YS: {
        'sketch': 'f20_out_left_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    # out+right
    F20+OUT+RIGHT+BRIDGE_Y: {
        'sketch': 'f20_out_right_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+RIGHT+BRIDGE_N: {
        'sketch': 'f20_out_right_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+RIGHT+BRIDGE_T: {
        'sketch': 'f20_out_right_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+OUT+RIGHT+BRIDGE_YS: {
        'sketch': 'f20_out_right_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    # in+left
    F20+IN+LEFT+BRIDGE_Y: {
        'sketch': 'f20_in_left_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+LEFT+BRIDGE_N: {
        'sketch': 'f20_in_left_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+LEFT+BRIDGE_T: {
        'sketch': 'f20_in_left_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+LEFT+BRIDGE_YS: {
        'sketch': 'f20_in_left_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    # in+right
    F20+IN+RIGHT+BRIDGE_Y: {
        'sketch': 'f20_in_right_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+RIGHT+BRIDGE_N: {
        'sketch': 'f20_in_right_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+RIGHT+BRIDGE_T: {
        'sketch': 'f20_in_right_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    F20+IN+RIGHT+BRIDGE_YS: {
        'sketch': 'f20_in_right_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (50, 50),
        'door_tube': (40, 20),
        'inner_frame_tube': (20, 20),
    },
    # f2020
    # out+left
    F2020+OUT+LEFT+BRIDGE_Y: {
        'sketch': 'f2020_out_left_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+LEFT+BRIDGE_N: {
        'sketch': 'f2020_out_left_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+LEFT+BRIDGE_T: {
        'sketch': 'f2020_out_left_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+LEFT+BRIDGE_YS: {
        'sketch': 'f2020_out_left_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # out+right
    F2020+OUT+RIGHT+BRIDGE_Y: {
        'sketch': 'f2020_out_right_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+RIGHT+BRIDGE_N: {
        'sketch': 'f2020_out_right_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+RIGHT+BRIDGE_T: {
        'sketch': 'f2020_out_right_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+OUT+RIGHT+BRIDGE_YS: {
        'sketch': 'f2020_out_right_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # in+left
    F2020+IN+LEFT+BRIDGE_Y: {
        'sketch': 'f2020_in_left_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+LEFT+BRIDGE_N: {
        'sketch': 'f2020_in_left_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+LEFT+BRIDGE_T: {
        'sketch': 'f2020_in_left_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+LEFT+BRIDGE_YS: {
        'sketch': 'f2020_in_left_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # in+right
    F2020+IN+RIGHT+BRIDGE_Y: {
        'sketch': 'f2020_in_right_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+RIGHT+BRIDGE_N: {
        'sketch': 'f2020_in_right_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+RIGHT+BRIDGE_T: {
        'sketch': 'f2020_in_right_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F2020+IN+RIGHT+BRIDGE_YS: {
        'sketch': 'f2020_in_right_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # f40
    # out+left
    F40+OUT+LEFT+BRIDGE_Y: {
        'sketch': 'f40_out_left_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+LEFT+BRIDGE_N: {
        'sketch': 'f40_out_left_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+LEFT+BRIDGE_T: {
        'sketch': 'f40_out_left_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+LEFT+BRIDGE_YS: {
        'sketch': 'f40_out_left_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # out+right
    F40+OUT+RIGHT+BRIDGE_Y: {
        'sketch': 'f40_out_right_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+RIGHT+BRIDGE_N: {
        'sketch': 'f40_out_right_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+RIGHT+BRIDGE_T: {
        'sketch': 'f40_out_right_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+OUT+RIGHT+BRIDGE_YS: {
        'sketch': 'f40_out_right_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # in+left
    F40+IN+LEFT+BRIDGE_Y: {
        'sketch': 'f40_in_left_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+LEFT+BRIDGE_N: {
        'sketch': 'f40_in_left_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+LEFT+BRIDGE_T: {
        'sketch': 'f40_in_left_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+LEFT+BRIDGE_YS: {
        'sketch': 'f40_in_left_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # in+right
    F40+IN+RIGHT+BRIDGE_Y: {
        'sketch': 'f40_in_right_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+RIGHT+BRIDGE_N: {
        'sketch': 'f40_in_right_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+RIGHT+BRIDGE_T: {
        'sketch': 'f40_in_right_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    F40+IN+RIGHT+BRIDGE_YS: {
        'sketch': 'f40_in_right_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
        'inner_frame_tube': (20, 20),
    },
    # f60
    # out+left
    F60+OUT+LEFT+BRIDGE_Y: {
        'sketch': 'f60_out_left_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+LEFT+BRIDGE_N: {
        'sketch': 'f60_out_left_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+LEFT+BRIDGE_T: {
        'sketch': 'f60_out_left_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+LEFT+BRIDGE_YS: {
        'sketch': 'f60_out_left_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    # out+right
    F60+OUT+RIGHT+BRIDGE_Y: {
        'sketch': 'f60_out_right_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+RIGHT+BRIDGE_N: {
        'sketch': 'f60_out_right_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+RIGHT+BRIDGE_T: {
        'sketch': 'f60_out_right_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+OUT+RIGHT+BRIDGE_YS: {
        'sketch': 'f60_out_right_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    # in+left
    F60+IN+LEFT+BRIDGE_Y: {
        'sketch': 'f60_in_left_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+LEFT+BRIDGE_N: {
        'sketch': 'f60_in_left_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+LEFT+BRIDGE_T: {
        'sketch': 'f60_in_left_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+LEFT+BRIDGE_YS: {
        'sketch': 'f60_in_left_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    # in+right
    F60+IN+RIGHT+BRIDGE_Y: {
        'sketch': 'f60_in_right_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+RIGHT+BRIDGE_N: {
        'sketch': 'f60_in_right_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+RIGHT+BRIDGE_T: {
        'sketch': 'f60_in_right_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    F60+IN+RIGHT+BRIDGE_YS: {
        'sketch': 'f60_in_right_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (60, 40),
        'door_tube': (60, 40),
    },
    # fGR
    # out+left
    FGR+OUT+LEFT+BRIDGE_Y: {
        'sketch': 'fgr_out_left_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+LEFT+BRIDGE_N: {
        'sketch': 'fgr_out_left_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+LEFT+BRIDGE_T: {
        'sketch': 'fgr_out_left_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+LEFT+BRIDGE_YS: {
        'sketch': 'fgr_out_left_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    # out+right
    FGR+OUT+RIGHT+BRIDGE_Y: {
        'sketch': 'fgr_out_right_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+RIGHT+BRIDGE_N: {
        'sketch': 'fgr_out_right_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+RIGHT+BRIDGE_T: {
        'sketch': 'fgr_out_right_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+OUT+RIGHT+BRIDGE_YS: {
        'sketch': 'fgr_out_right_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    # in+left
    FGR+IN+LEFT+BRIDGE_Y: {
        'sketch': 'fgr_in_left_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+LEFT+BRIDGE_N: {
        'sketch': 'fgr_in_left_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+LEFT+BRIDGE_T: {
        'sketch': 'fgr_in_left_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+LEFT+BRIDGE_YS: {
        'sketch': 'fgr_in_left_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    # in+right
    FGR+IN+RIGHT+BRIDGE_Y: {
        'sketch': 'fgr_in_right_y.png',
        'calc': CalculatorBridgeY,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+RIGHT+BRIDGE_N: {
        'sketch': 'fgr_in_right_n.png',
        'calc': CalculatorBridgeN,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+RIGHT+BRIDGE_T: {
        'sketch': 'fgr_in_right_t.png',
        'calc': CalculatorBridgeT,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
    FGR+IN+RIGHT+BRIDGE_YS: {
        'sketch': 'fgr_in_right_ys.png',
        'calc': CalculatorBridgeYS,
        'frame_tube': (40, 40),
        'door_tube': (40, 40),
    },
}

# заполнения
FILLING = {
    'профиль AG/77': F20,
    'профиль PD/77': F20,
    'профиль AER55/S': F20,
    'профиль AER55m/S': F20,
    'профлист СС10 шагрень 1ст': F20,
    'Профлист 2ст': F2020,
    'жалюзи Аполло Z110': F60,
    'штакетник шагрень 1ст': F20,
    'штакетник шагрень 2ст': F2020,
    'металлосайдинг с 2 сторон': F2020,
    'сэндвич S-гофр DoorHan': F40,
    'панель Пластэк Декор': F40,
    'сетка сварная 3D': FGR,
    'обрешетка из трубы 20х20': FGR,
    'заказчика (20мм)': F20,
    'заказчика (20+20мм)': F2020,
    'заказчика (40мм)': F40,
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
