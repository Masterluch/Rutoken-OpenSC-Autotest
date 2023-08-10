import subprocess
import sys

sys.path.append("..\\sources")
from ByteFileTool import ByteFileTool
from execute import execute


def test_GOST(reset_token, define_os):
    '''
    Тест ГОСТа.
    '''

    # Генерация файла in.txt
    ByteFileTool.generate_byte_file("./testing_data/in.txt", 245)

    # Выбор файла для парсинга в зависимости от ОС
    file_path = "./testing_data/allkeys_pkcs11-tool"
    if (define_os == "win32"): file_path += ".bat"
    elif (define_os == "linux"): file_path += ".sh"
    else: raise Exception("Unsupported OS")

    # Перебор параметров pkcs11-tool из файла allkeys_pkcs11-tool
    with open(file_path, "r") as file_keys:
        for arg in file_keys.readlines():
            if (arg == "\n"): continue

            cmd = arg.split()

            # Исправление путей к вспомогательным файлам
            for i in range(len(cmd)):
                if (len(cmd[i]) > 4):
                    if (cmd[i][len(cmd[i])-4:len(cmd[i])] == ".txt"):
                        cmd[i] = "./testing_data/"+cmd[i]

            execute(cmd, define_os)

    assert(True)
