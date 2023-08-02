import subprocess
import sys

sys.path.append("..\\sources")
from ByteFileTool import ByteFileTool


def test_GOST(reset_token):
    '''
    Тест ГОСТа.
    '''

    # Генерация файла in.txt
    ByteFileTool.generate_byte_file("./testing_data/in.txt", 245)

    # Перебор параметров pkcs11-tool из файла pkcs11_keys_gost.bat
    with open("./testing_data/allkeys_pkcs11-tool.bat", "r") as file_keys:
        for arg in file_keys.readlines():
            if (arg == "\n"): continue

            cmd = ["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs11-tool.exe"] + arg[12:len(arg)].split()

            # Исправление путей к вспомогательным файлам
            for i in range(len(cmd)):
                if (len(cmd[i]) > 4):
                    if (cmd[i][len(cmd[i])-4:len(cmd[i])] == ".txt"):
                        cmd[i] = "./testing_data/"+cmd[i]

            process = subprocess.run(cmd, stderr=subprocess.PIPE)
            if (process.returncode != 0): raise Exception(process.stderr)

    assert(True)
