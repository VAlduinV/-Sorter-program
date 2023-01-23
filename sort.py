import os

print(
    '''\n
                        V                     VH               HV                     V
                         V                   V H               H V                   V
                          V                 V  H               H  V                 V
                           V               V   H               H   V               V
                            V             V    H               H    V             V
                             V           V     H               H     V           V
                              V         V      HHHHHHHHHHHHHHHHH      V         V
                               V       V       H               H       V       V
                                V     V        H               H        V     V
                                 V   V         H               H         V   V
                                  V V          H               H          V V
                                   V           H               H           V  


Script: folder sorter
Instructions:
Метод os.scandir() у Python використовується для отримання ітератора об’єктів os.DirEntry,
що відповідають записам у каталозі, визначеному вказаним шляхом. 
(simple words: метод, який сканує директорію)
''')


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ_"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_")


TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

# print(TRANS)


def normalize(main_path):
    for k, v in TRANS.items():
        main_path = main_path.replace(chr(k), v)

    return main_path


main_path = r'C:\Users\prime\PycharmProjects\Мотлох'
normalize(main_path)
# os.mkdir(main_path + '\\Мотлох')

extensions = {  # імена ключів будуть іменами папок!

    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v',
              'h264', 'flv', 'rm', 'swf', 'vob'],

    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav',
             'tar', 'xml'],

    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
              'cda'],

    'images': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif',
               'tiff'],

    'archives': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],

    'documents': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

    'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],

    'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],

    'font': ['otf', 'ttf', 'fon', 'fnt'],

    'AnsysWorkbench': ['wbpj'],

    'Autocad': ['dwg'],

    'SolidWorks': ['iges', 'dxf', 'step', 'acis', 'stl', 'parasolid'],

    'python': ['py'],

    'matlab': ['m'],

    'C++': ['cpp'],

    'gif': ['gif'],

    'exe': ['exe'],

    'bat': ['bat'],

    'apk': ['apk']
}


def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:  # Шукаємо папку
        if not os.path.exists(f'{folder_path}\\{folder}'):  # Чи існує ця папка вже?
            os.mkdir(f'{folder_path}\\{folder}')  # Якщо не існує, то створюємо нову папку


def get_subfolder_paths(folder_path) -> list:  # Отримуємо шляхи підпапок та файлів
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def get_subfolder_names(folder_path) -> list:  # Функція отримання імен підпапок
    subfolder_paths = get_subfolder_paths(folder_path)
    subfolder_names = [f.split('\\')[-1] for f in subfolder_paths]

    return subfolder_names


def get_file_paths(folder_path) -> list:  # Отримати шляхи всіх файлів у папці
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


def get_file_names(folder_path) -> list:  # Функція отримання імен файлів
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    file_names = [f.split('\\')[-1] for f in file_paths]

    return file_names


def sort_files(folder_path):  # Функція сортування. Отримаємо список всіх файлів
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())
    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')


def remove_empty_folders(folder_path):  # Функція видалення порожніх папок
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)


if __name__ == "__main__":
    create_folders_from_list(main_path, extensions)
    print(get_subfolder_names(main_path))
    sort_files(main_path)
