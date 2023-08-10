import subprocess
import sys

sys.path.append("..\\sources")
from ByteFileTool import ByteFileTool
from execute import execute


def test_work_with_binary_files(reset_token, define_os):
    '''
    Тест Работы с двоичными файлами.
    '''

    # Создание бинарного файла, доступ к которому осуществляется по пон-коду, на основе объекта данных test_data
    execute(["pkcs11-tool",
             "--module", "./rtpkcs11ecp.dll",
             "--login", "--pin", "12345678",
             "--write-object", "./testing_data/test_data",
             "--type", "data",
             "--id", "5",
             "--label", "data2", "--private"], define_os)

    # Чтение бинарного файла (Для Linux убрать --module) и запись резульата в файл data_from_token
    process = execute(["pkcs11-tool",
             "--module", "./rtpkcs11ecp.dll",
             "--login", "--pin", "12345678",
             "--read-object",
             "--type", "data",
             "--label", "data2"],
             define_os, stdout=subprocess.PIPE)

    with open("./testing_data/data_from_token", "wb") as file_data_from_token:
        file_data_from_token.write(process.stdout)

    # Сравнение записанного объекта данных (test_data) с полученным с токена объектом данных (data_from_token)
    assert(ByteFileTool.comparsion_files_by_bytes("./testing_data/test_data", "./testing_data/data_from_token"))
