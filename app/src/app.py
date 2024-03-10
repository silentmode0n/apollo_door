import PySimpleGUI as sg
import tkinter as tk
import os
import subprocess
import sys
import config as cfg
from src.pdf_creator import PDFCreator
import logging


def start_file(filepath):
    """ Открывает файл внешней программой """
    if sys.platform == 'win32':
        os.startfile(filepath)
    else:
        subprocess.call(['xdg-open', filepath])


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


class App():

    def __init__(self, condition=None) -> None:
        # сохраняем словарь начального состояния
        self.condition = condition
        # Объявляем путь хранения файла настройки
        sg.user_settings_filename(path=cfg.HOMEDIR, filename=cfg.SETTINGS_FILENAME)

    def run(self):
        """ Создает главное окно программы и запускает событийный цикл """
        self.setup_gui(cfg.GUI['options'], cfg.GUI['theme'])
        # создать главное окно
        window = sg.Window(cfg.GUI['title'], self.create_layout())
        # отрисовать главное окно
        window.Finalize()
        # заполнить поля виджетов окна первичными данными
        if self.condition:
            window.Fill(self.condition)
            self.check_state_widgets(window)
            self.redraw_preview(window)
        # главный событийный цикл
        while True:
            event, values = window.Read()
            print(event)
            if event is None:
                break   # закрыть программу
            elif event == 'bridge':
                self.check_bridge(window)
                self.redraw_preview(window)
            elif event == 'batten':
                self.check_batten(window)
            elif event == 'height':
                self.check_height(window)
            elif event == 'lock':
                self.check_lock(window)
            elif event == 'open' or event == 'side' or event == 'frame_type':
                self.redraw_preview(window)

            elif event == '-SUBMIT-':
                print(values)
                self.execute(values)

        window.Close()  # exit

    def setup_gui(self, options, theme):
        """ Настраивает внешний вид интерфейса"""
        sg.SetOptions(**options)
        sg.theme(theme)

    def create_layout(self):
        """Заполняет loyout виджетами окна"""
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
            get_form('open', submit=True),
            get_form('side', submit=True),
            get_form('bridge', submit=True),
            get_form('frame_type', submit=True),
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
        order_frame = [
            [sg.Column(order_left_col, pad=cfg.GUI['form_padding']),
             sg.Column(order_right_col, pad=cfg.GUI['form_padding'])],
        ]
        main_frame = [sg.vtop(
            [sg.Column(main_left_col, pad=cfg.GUI['form_padding']),
             sg.Column(main_right_col, pad=cfg.GUI['form_padding'])]),
        ]
        comment_frame = [
            get_form('comments'),
        ]
        preview_frame = [[
            sg.Canvas(key='preview_back', background_color='white', size=cfg.GUI['size_preview_back']),
            sg.Canvas(key='preview_frame', background_color='white', size=cfg.GUI['size_preview_frame']),
            sg.Canvas(key='preview_open', background_color='white', size=cfg.GUI['size_preview_open']),
        ]]
        buttons_frame = [[
            sg.Button('> Подготовить <', key='-SUBMIT-', button_color=cfg.GUI['submit_color']),
            sg.VerticalSeparator(color='grey', pad=(10, 0)),
            sg.Checkbox('Для клиента', default=True, k='for_client'),
            sg.Checkbox('Для производства', default=True, k='for_manufacture'),
        ]]
        layout = [
            [sg.Frame('Информация о заказе', order_frame)],
            [sg.Frame('Параметры калитки', main_frame)],
            [sg.vtop(
                [
                    sg.Column([
                        [sg.Frame('Комментарий', comment_frame, expand_x=True, expand_y=True)],
                        [sg.Frame('Чертеж', buttons_frame, expand_x=True, expand_y=True)],
                    ], expand_x=False, expand_y=True),
                    sg.Column([
                        [sg.Frame('Предпросмотр', preview_frame, expand_x=True, element_justification='center')],
                    ], expand_x=True, expand_y=True)
                ], expand_x=True, expand_y=True)
             ],
        ]
        return layout

    def check_state_widgets(self, window):
        """Проверяет и устанавливает принудительные состояния элементов в зависимости от значений других элементов"""
        self.check_height(window)
        self.check_batten(window)
        self.check_bridge(window)
        self.check_lock_without_handles(window)  # не изменять значения ручек

    def check_height(self, window):
        """Проверяет значение поля height"""
        if not window['batten_lenght'].Disabled:
            window['batten_lenght'].update(window['height'].get())

    def check_batten(self, window):
        """Проверяет значение поля batten"""
        batten = window['batten'].get()
        batten_num = window['batten_num'].get()
        if batten.upper() == cfg.NO or batten == '':
            window['batten_lenght'].update('0', disabled=True)
            window['batten_num'].update('0', disabled=True)
        else:
            window['batten_lenght'].update(window['height'].get(), disabled=False)
            if batten_num == '0':
                window['batten_num'].update('2', disabled=False)
            else:
                window['batten_num'].update(batten_num, disabled=False)

    def check_bridge(self, window):
        """Проверяет значение поля bridge"""
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

    def check_lock(self, window):
        """Проверяет значение поля lock"""
        lock = window['lock'].get()
        handle_in = cfg.LOCKS[lock]['handle_in']
        handle_out = cfg.LOCKS[lock]['handle_out']
        flexible_tube = cfg.LOCKS[lock]['flexible_tube']
        window['handle_in'].update(handle_in)
        window['handle_out'].update(handle_out)
        window['flexible_tube'].update(flexible_tube)

    def check_lock_without_handles(self, window):
        """Проверяет значение поля lock без изменения значений полей handle_in handle_out"""
        lock = window['lock'].get()
        if lock in cfg.LOCKS and cfg.LOCKS[lock].get('flexible_tube'):
            flexible_tube = cfg.LOCKS[lock]['flexible_tube']
            window['flexible_tube'].update(flexible_tube)


    def execute(self, data):
        """ Главный метод обработки данных """
        errors = initial_verification(data)
        if errors:
            self.show_errors(errors)
            return
        filepath = self.ask_saveas_filename(self.get_default_filename(data))
        if not filepath:
            return
        sg.user_settings_set_entry('-initialdir-', os.path.dirname(filepath))
        self.update_data(data)  # must have errors!
        print('update data:')
        print(data)

        logging.info('Версия: {} | Заказ: {} | Заказчик: {} | Инженер: {}'.format(cfg.VERSION,
                                                                                  data['order'],
                                                                                  data['customer'],
                                                                                  data['engineer']))

        try:
            pdf = PDFCreator(cfg.PDF, data)
            if data['for_client']:
                pdf.create_page_for_client()
            if data['for_manufacture']:
                pdf.create_page_for_manufacture()
            pdf.save(filepath)
            self.show_result(filepath)
        except FileNotFoundError as e:
            error_message = 'Не найден файл - {}'.format(e.filename)
            logging.error(error_message)
            self.show_errors([error_message, ])

    def update_data(self, data):
        data['frame_color_name'] = get_name_color(data['frame_color'])
        data['fill_color_in_name'] = get_name_color(data['fill_color_in'])
        data['fill_color_out_name'] = get_name_color(data['fill_color_out'])

        design_schema = get_design_schema(data['fill'], data['open'], data['side'], data['bridge'])
        data['sketch_file'] = get_sketch_filepath(design_schema)
        data['open_view_file'] = get_open_view_filepath(data['side'], data['open'])
        data['back_view_file'] = get_back_view_filepath(data['bridge'], data['side'])

        Calculator = design_schema['calc']
        Calculator(data,
                   design_schema['frame_tube'],
                   design_schema['door_tube'],
                   ).run()

    def show_errors(self, errors):
        """ Выводит вплывающее окно со списком ошибок """
        if errors:
            sg.popup(*errors, title='Ошибки', keep_on_top=True)

    def show_result(self, filepath):
        """ Показывает итоговый файл """
        if os.path.isfile(filepath):
            start_file(filepath)
        else:
            message = 'Файл {} не найден!'.format(filepath)
            self.show_errors([message, ])

    def ask_saveas_filename(self, initial_name='result'):
        """ return file name """
        file_types = (('Document PDF', '*.pdf'), )
        initialdir = sg.user_settings_get_entry('-initialdir-', '') or cfg.HOMEDIR
        filepath = tk.filedialog.asksaveasfilename(title='Сохранить как',
                                                   filetypes=file_types,
                                                   initialdir=initialdir,
                                                   initialfile=initial_name,
                                                   defaultextension='.pdf')
        return filepath

    def get_default_filename(self, data):
        """Формирует имя файла по умолчанию"""
        order = data.get('order', 'XXX')
        customer = data.get('customer', 'XXXXXXXX')
        filename = '{}-{}.pdf'.format(order, customer)
        return filename

    def redraw_preview(self, window):
        self.redraw_preview_back(window)
        self.redraw_preview_frame(window)
        self.redraw_preview_open(window)

    def redraw_preview_open(self, window):
        """Перерисовывает превью типа открывания"""
        window['preview_open'].TKCanvas.delete('all')
        filepath = get_open_preview_filepath(side=window['side'].get(),
                                             open=window['open'].get())
        if filepath:
            center_x = cfg.GUI['size_preview_open'][0] / 2
            center_y = cfg.GUI['size_preview_open'][1] / 2
            self.preview_open_image = tk.PhotoImage(file=filepath)
            window['preview_open'].TKCanvas.create_image(
                center_x, center_y, image=self.preview_open_image, anchor=tk.CENTER)

    def redraw_preview_back(self, window):
        """Перерисовывает превью общего вида"""
        window['preview_back'].TKCanvas.delete('all')
        filepath = get_back_preview_filepath(bridge=window['bridge'].get(),
                                             side=window['side'].get())
        if filepath:
            center_x = cfg.GUI['size_preview_back'][0] / 2
            center_y = cfg.GUI['size_preview_back'][1] / 2
            self.preview_back_image = tk.PhotoImage(file=filepath)
            window['preview_back'].TKCanvas.create_image(
                center_x, center_y, image=self.preview_back_image, anchor=tk.CENTER)

    def redraw_preview_frame(self, window):
        """Перерисовывает превью рамы"""
        window['preview_frame'].TKCanvas.delete('all')
        filepath = get_frame_preview_filepath(frame_type=window['frame_type'].get())
        if filepath:
            center_x = cfg.GUI['size_preview_frame'][0] / 2
            center_y = cfg.GUI['size_preview_frame'][1] / 2
            self.preview_frame_image = tk.PhotoImage(file=filepath)
            window['preview_frame'].TKCanvas.create_image(
                center_x, center_y, image=self.preview_frame_image, anchor=tk.CENTER)


# --------------------- validators --------------------------------


def initial_verification(data):
    """Запускает проверку значений полей формы"""
    errors = []
    module = sys.modules[__name__]
    # Пройти по всем методам валидации данных
    for validator in [v for k, v in module.__dict__.items() if k.startswith('validate_of_')]:
        errors += validator(data)
    return errors


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
            if not data[key] in cfg.WIDGETS[key]['values']:  # если не в списке
                errors.append('[{}] имеет не верное значение!'.format(
                    cfg.WIDGETS[key]['text']))
    return errors


def validate_of_frame_type(data):
    errors = []
    frame_type = data.get('frame_type')
    if frame_type != cfg.FR_DIRECT:
        errors.append('Создать чертеж возможно только для типа рамы: ТОРЦЕВАЯ!')
    return errors


def get_open_view_filepath(side, open):
    schema = side + open
    filename = cfg.OPEN_VIEW_FILENAMES.get(schema)
    if filename:
        return cfg.get_filepath('open_view', filename)


def get_open_preview_filepath(side, open):
    schema = side + open
    filename = cfg.OPEN_VIEW_FILENAMES.get(schema)
    if filename:
        return cfg.get_filepath('open_preview', filename)


def get_back_view_filepath(bridge, side):
    schema = bridge + side
    filename = cfg.BACK_VIEW_FILENAMES.get(schema)
    if filename:
        return cfg.get_filepath('back_view', filename)


def get_back_preview_filepath(bridge, side):
    schema = bridge + side
    filename = cfg.BACK_VIEW_FILENAMES.get(schema)
    if filename:
        return cfg.get_filepath('back_preview', filename)


def get_frame_preview_filepath(frame_type):
    filename = cfg.FRAME_VIEW_FILENAMES.get(frame_type)
    if filename:
        return cfg.get_filepath('frame_preview', filename)


def get_sketch_filepath(design_schema):
    filename = design_schema.get('sketch')
    if filename:
        return cfg.get_filepath('sketchs', filename)


def get_design_schema(fill, open, side, bridge):
    fill = cfg.FILLING.get(fill)
    if fill:
        design_name = fill + open + side + bridge
        return cfg.DESIGNS.get(design_name)


def get_name_color(ral):
    """Получает имя цвета по таблице RAL"""
    return cfg.RAL_TABLE.get(ral, '')
