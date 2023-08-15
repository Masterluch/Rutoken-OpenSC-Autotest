import subprocess
import sys

sys.path.append("..\\sources")
from ByteFileTool import ByteFileTool
from execute import execute


def test_decryption(reset_token, define_os):
    '''
    Тест Расшифрования.
    '''

    # Генерация ключевой пары для шифрования
    execute(["pkcs15-init",
             "-G", "rsa/2048",
             "--auth-id", "02",
             "-u", "decrypt",
             "--id", "42",
             "--pin", "12345678",
             "-v"], define_os)

    # Извлечение открытого ключа
    execute(["pkcs15-tool",
             "--read-public-key", "42",
             "-o", "./testing_data/public_key.pem",
             "-v"], define_os)

    # Генерация файла размером 245 байт
    ByteFileTool.generate_byte_file("./testing_data/test_data", 245)

    # Шифрование в OpenSSL
    execute(["openssl", "pkeyutl",
             "-inkey", "./testing_data/public_key.pem",
             "-pubin", "-encrypt",
             "-in", "./testing_data/test_data",
             "-out", "./testing_data/enc_data"], define_os)

    # Расшифрование
    execute(["pkcs15-crypt",
             "--decipher",
             "--input", "./testing_data/enc_data",
             "--pkcs1", "--raw",
             "-k", "42",
             "--output", "./testing_data/dec_data",
             "--pin", "12345678",
             "-v"], define_os)

    # Сравненеие файлов test_data и dec_data
    assert(ByteFileTool.comparsion_files_by_bytes("./testing_data/test_data", "./testing_data/dec_data"))
