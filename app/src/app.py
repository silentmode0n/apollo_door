import PySimpleGUI as sg
import tkinter as tk
import os
import subprocess
import sys
import config as cfg
from src.pdf_creator import PDFCreator
import logging


# ------------------------ view --------------------------------


def create_layout():
    order_left_col = [
        get_form('order'),
        get_form('customer')
    ]
    order_right_col = [
        get_form('date'),
        get_form('engineer')
    ]
    main_left_col = [
        get_form('width'),
        get_form('height', submit=True),
        get_form('open'),
        get_form('side'),
        get_form('bridge', submit=True),
        get_form('frame_type'),
        get_form('cliarance'),
        get_form('bridge_height'),
        get_form('frame_color'),
        get_form('color_type'),
    ]
    main_right_col = [
        get_form('fill'),
        get_form('fill_color_out'),
        get_form('fill_color_in'),
        get_form('lock', True),
        # get_form('steelwire'),
        get_form('handle_in'),
        get_form('handle_out'),
        get_form('flexible_tube'),
        get_form('auto_closer'),
        get_form('batten', True),
        get_form('batten_lenght'),
        get_form('batten_num'),
    ]
    order_layout = [
        [sg.Column(order_left_col, pad=cfg.GUI['form_padding']),
            sg.Column(order_right_col, pad=cfg.GUI['form_padding'])],
    ]
    main_layout = [sg.vtop(
        [sg.Column(main_left_col, pad=cfg.GUI['form_padding']),
            sg.Column(main_right_col, pad=cfg.GUI['form_padding'])]),
    ]
    comment_layout = [
        get_form('comments'),
    ]
    layout = [
        [sg.Frame('Информация о заказе', order_layout)],
        [sg.Frame('Параметры калитки', main_layout)],
        [sg.Frame('Комментарий', comment_layout)],
        [
            sg.Button('> Чертёж <', key='-SUBMIT-', button_color=cfg.GUI['submit_color']),
            sg.Checkbox('Для клиента', default=True, k='for_client'),
            sg.Checkbox('Для производства', default=True, k='for_manufacture'),
        ],
    ]
    return layout


def get_form(_id, submit=False):
    form = []
    element = cfg.WIDGETS[_id]
    text = element['text']
    if text:
        s_txt = cfg.GUI['size_text']
        form.append(sg.Text(text, size=s_txt, pad=(1, 4)))
    values = element.get('values')
    if not values:
        s_inp = cfg.GUI['size_input']
        form.append(sg.Input(size=s_inp, key=_id, change_submits=submit))
    elif values == '>Text<':
        s_mul = cfg.GUI['size_multiline']
        form.append(sg.Multiline(size=s_mul, key=_id, change_submits=False))
    elif values == '>Boolean<':
        form.append(sg.Checkbox('', key=_id, change_submits=submit))
    elif isinstance(values, (list, tuple)):
        s_cmb = cfg.GUI['size_combo']
        form.append(sg.Combo(values, size=s_cmb, default_value=' ', key=_id,
                             change_submits=submit))
    return form


def start_file(filepath):
    """ Открывает файл внешней программой """
    if sys.platform == 'win32':
        os.startfile(filepath)
    else:
        subprocess.call(['xdg-open', filepath])


def setup_gui(options, theme):
    """ Настраивает внешний вид интерфейса"""
    sg.SetOptions(**options)
    sg.theme(theme)

def check_state_widgets(window):
    """Проверяет и устанавливает принудительные состояния элементов в зависимости от значений других элементов"""
    check_height(window)
    check_batten(window)
    check_bridge(window)
    check_lock_without_handles(window) # не изменять значения ручек

def check_bridge(window):
    if window['bridge'].get() != cfg.BRIDGE_T:
        window['bridge_height'].update('0', disabled=True)
    else:
        window['bridge_height'].update(disabled=False)
    if window['bridge'].get() == cfg.BRIDGE_N:
        window['auto_closer'].update(cfg.NO, disabled=True)
    else:
        window['auto_closer'].update(disabled=False)
    if window['bridge'].get() == cfg.BRIDGE_YS:
        window['cliarance'].update('0', disabled=True)
    else:
        window['cliarance'].update(disabled=False)

def check_batten(window):
    if window['batten'].get() == cfg.NO:
        window['batten_lenght'].update('0', disabled=True)
        window['batten_num'].update('0', disabled=True)
    else:
        window['batten_lenght'].update(window['height'].get(), disabled=False)
        window['batten_num'].update('2', disabled=False)

def check_height(window):
    if not window['batten_lenght'].Disabled:
        window['batten_lenght'].update(window['height'].get())

def check_lock(window):
    lock = window['lock'].get()
    handle_in = cfg.LOCKS[lock]['handle_in']
    handle_out = cfg.LOCKS[lock]['handle_out']
    flexible_tube = cfg.LOCKS[lock]['flexible_tube']
    window['handle_in'].update(handle_in)
    window['handle_out'].update(handle_out)
    window['flexible_tube'].update(flexible_tube)

def check_lock_without_handles(window):
    lock = window['lock'].get()
    flexible_tube = cfg.LOCKS[lock]['flexible_tube']
    window['flexible_tube'].update(flexible_tube)

def run(condition=None):
    """ Создает главное окно программы и запускает событийный цикл """
    setup_gui(cfg.GUI['options'], cfg.GUI['theme'])
    window = sg.Window(cfg.GUI['title'], create_layout())
    # отрисовать окно
    window.Finalize()
    # заполнить поля первичными данными
    if condition:
        window.Fill(condition)
        check_state_widgets(window)
    # главный событийный цикл
    while True:
        event, values = window.Read()
        if event is None:
            break   # закрыть программу
        elif event == 'bridge':
            check_bridge(window)
        elif event == 'batten':
            check_batten(window)
        elif event == 'height':
            check_height(window)
        elif event == 'lock':
            check_lock(window)

        elif event == '-SUBMIT-':
            print(event)
            print(values)
            execute(values)
    window.Close()  # exit


def show_result(filepath):
    """ Показывает итоговый файл """
    if os.path.isfile(filepath):
        start_file(filepath)
    else:
        message = 'Файл {} не найден!'.format(filepath)
        show_errors([message, ])


def show_errors(errors):
    """ Выводит вплывающее окно со списком ошибок """
    if errors:
        sg.popup(*errors, title='Ошибки', keep_on_top=True)


def ask_saveas_filename(initial_name='result'):
    """ return file name """
    file_types = (('Document PDF', '*.pdf'), )
    filepath = tk.filedialog.asksaveasfilename(title='Сохранить как',
                                               filetypes=file_types,
                                               initialdir=cfg.HOMEDIR,
                                               initialfile=initial_name,
                                               defaultextension='.pdf')
    return filepath


# --------------------- model --------------------------------


def execute(data):
    """ Главный метод обработки данных """
    errors = initial_verification(data)
    if errors:
        show_errors(errors)
        return
    filepath = ask_saveas_filename(get_default_filename(data))
    if not filepath:
        return
    update_data(data) # must have errors!

    logging.info('Заказ: {} | Заказчик: {} | Инженер: {}'.format(data['order'], 
                                                                 data['customer'], 
                                                                 data['engineer']))

    try:
        pdf = PDFCreator(cfg.PDF, data)
        if data['for_client']:
            pdf.create_page_for_client()
        if data['for_manufacture']:
            pdf.create_page_for_manufacture()
        pdf.save(filepath)
        show_result(filepath)
    except FileNotFoundError as e:
        error_message = 'Не найден файл - {}'.format(e.filename)
        logging.error(error_message)
        show_errors([error_message,])


def update_data(data):
    data['frame_color_name'] = get_name_color(data['frame_color'])
    data['fill_color_in_name'] = get_name_color(data['fill_color_in'])
    data['fill_color_out_name'] = get_name_color(data['fill_color_out'])

    design_schema = get_design_schema(data['fill'], data['open'], data['side'], data['bridge'])
    data['sketch_file'] = get_sketch_file(design_schema)
    data['open_view_file'] = get_open_view_file(design_schema)
    data['back_view_file'] = get_back_view_file(design_schema)

    Calculator = design_schema['calc']
    Calculator(data,
                design_schema['frame_tube'],
                design_schema['door_tube'],
                ).run()


def get_default_filename(data):
    """Формирует имя файла по умолчанию"""
    order = data.get('order', 'XXX')
    customer = data.get('customer', 'XXXXXXXX')
    filename = '{}-{}.pdf'.format(order, customer)
    return filename


def initial_verification(data):
    """Запускает проверку значений полей формы"""
    errors = []
    module = sys.modules[__name__]
    # Пройти по всем методам валидации данных
    for validator in [v for k, v in module.__dict__.items() if k.startswith('validate_of_')]:
        errors += validator(data)
    return errors


def get_open_view_file(design_schema):
    return design_schema['open_view']


def get_back_view_file(design_schema):
    return design_schema['back_view']


def get_sketch_file(design_schema):
    return design_schema['sketch']


def get_design_schema(fill, open, side, bridge):
    design_name = cfg.FILLING[fill] + open + side + bridge
    return cfg.DESIGNS[design_name]


def get_name_color(ral):
    """Получает имя цвета по таблице RAL"""
    return cfg.RAL_TABLE.get(ral, '')


# --------------------- validators --------------------------------


def validate_of_int(data):
    """Проверяет, что значение поля формы является числом
    ключ содержит поле 'valid': ('int',)"""
    errors = []
    for key in cfg.WIDGETS.keys():
        if 'valid' in cfg.WIDGETS[key] and 'int' in cfg.WIDGETS[key]['valid']:
            if not data[key].isdigit():  # если не положительное число
                errors.append('[{}] имеет значение не число!'.format(
                    cfg.WIDGETS[key]['text']))
            elif 'min' in cfg.WIDGETS[key] and int(data[key]) < int(cfg.WIDGETS[key]['min']):
                errors.append('[{}] имеет значение менее {}!'.format(
                    cfg.WIDGETS[key]['text'],
                    cfg.WIDGETS[key]['min']))
            elif 'max' in cfg.WIDGETS[key] and int(data[key]) > int(cfg.WIDGETS[key]['max']):
                errors.append('[{}] имеет значение более {}!'.format(
                    cfg.WIDGETS[key]['text'],
                    cfg.WIDGETS[key]['max']))
    return errors


def validate_of_value(data):
    """Проверяет, что значение поля формы соответствует списку
    ключ содержит поле 'valid': ('in_list',)"""
    errors = []
    for key in cfg.WIDGETS.keys():
        if 'valid' in cfg.WIDGETS[key] and 'in_list' in cfg.WIDGETS[key]['valid']:
            if not data[key] in cfg.WIDGETS[key]['values']: # если не в списке
                errors.append('[{}] имеет не верное значение!'.format(
                    cfg.WIDGETS[key]['text']))
    return errors
    


# def validate_of_width(data):
#     errors = []
#     width = data['width']
#     if not width.isdigit():  # если не число
#         errors.append('[{}] имеет не верное значение!'.format(
#             cfg.WIDGETS['width']['text']))
#     return errors


# def validate_of_height(data):
#     errors = []
#     if not data['height'].isdigit():  # если не число
#         errors.append('[{}] имеет не верное значение!'.format(
#             cfg.WIDGETS['height']['text']))
#     return errors


# def validate_of_open(data):
#     errors = []
#     if not data['open'] in cfg.WIDGETS['open']['values']:  # если не в списке
#         errors.append('[{}] имеет не верное значение!'.format(
#             cfg.WIDGETS['open']['text']))
#     return errors


# def validate_of_side(data):
#     errors = []
#     if not data['side'] in cfg.WIDGETS['side']['values']:  # если не в списке
#         errors.append('[{}] имеет не верное значение!'.format(
#             cfg.WIDGETS['side']['text']))
#     return errors


# def validate_of_fill(data):
#     errors = []
#     if not data['fill'] in cfg.WIDGETS['fill']['values']:  # если не в списке
#         errors.append('[{}] имеет не верное значение!'.format(
#             cfg.WIDGETS['fill']['text']))
#     return errors


# def validate_of_bridge(data):
#     errors = []
#     if not data['bridge'] in cfg.WIDGETS['bridge']['values']:  # если не в списке
#         errors.append('[{}] имеет не верное значение!'.format(
#             cfg.WIDGETS['bridge']['text']))
#     return errors


# def validate_of_cliarance(data):
#     errors = []
#     if not data['cliarance'].isdigit():  # если не число
#         errors.append('[{}] имеет не верное значение!'.format(
#             cfg.WIDGETS['cliarance']['text']))
#     return errors


# def validate_of_bridge_hidht(data):
#     errors = []
#     if data['bridge'] == cfg.BRIDGE_T and not data['bridge_height'].isdigit():
#         errors.append('[{}] имеет не верное значение!'.format(
#             cfg.WIDGETS['bridge_height']['text']))
#     return errors
