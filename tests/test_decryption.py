import subprocess
import sys

sys.path.append("..\\sources")
from ByteFileTool import ByteFileTool


def test_decryption(reset_token):
    '''
    Тест Расшифрования.
    '''

    # Генерация ключевой пары для шифрования
    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-init.exe",
                              "-G", "rsa/2048",
                              "--auth-id", "02",
                              "-u", "decrypt",
                              "--id", "42",
                              "--pin", "12345678",
                              "-v", "-r3"],
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    # Извлечение открытого ключа
    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-tool.exe",
                              "--read-public-key", "42",
                              "-o", "./testing_data/public_key.pem",
                              "-v", "-r3"],
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    # Генерация файла размером 245 байт
    # ByteFileTool.generate_byte_file("./testing_data/test_data", 245)

    # Шифрование в OpenSSL
    process = subprocess.run(["openssl", "pkeyutl",
                              "-inkey", "./testing_data/public_key.pem",
                              "-pubin", "-encrypt",
                              "-in", "./testing_data/test_data",
                              "-out", "./testing_data/enc_data"],
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    # Расшифрование
    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-crypt.exe",
                              "--decipher",
                              "--input", "./testing_data/enc_data",
                              "--pkcs1", "--raw",
                              "-k", "42",
                              "--output", "./testing_data/dec_data",
                              "--pin", "12345678",
                              "-v", "-r3"],
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    # Сравненеие файлов test_data и dec_data
    assert(ByteFileTool.comparsion_files_by_bytes("./testing_data/test_data", "./testing_data/dec_data"))
