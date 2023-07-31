import subprocess
import sys

sys.path.append("..\\sources")
from ByteFileTool import ByteFileTool


def test_work_with_certificates(reset_token):
    '''
    Тест Работа с сертификатами.
    '''

    # Подготовка сертификата пользователя tester.crt в формате PEM с помощью OpenSSL
    process = subprocess.run(["openssl", "genrsa",
                              "-out", "./testing_data/rootCA.key", "2048"],
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    file_certificate_info = open("./testing_data/certificate_info.txt")
    process = subprocess.run(["openssl", "req",
                              "-x509", "-new", "-nodes",
                              "-key", "./testing_data/rootCA.key",
                              "-sha256", "-days", "1024",
                              "-out", "./testing_data/tester.crt"],
                              stdin=file_certificate_info,
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    # Запись сертификата на токен
    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-init.exe",
                              "--store-certificate", "./testing_data/tester.crt",
                              "--auth-id", "02",
                              "--id", "1",
                              "--format", "pem",
                              "--pin", "12345678",
                              "-v", "-r3"],
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    # Чтение сертификата с токена
    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-tool.exe",
                                "--read-certificate", "1", "-r3"],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    with open("./testing_data/certificate_from_token.crt", "wb") as file_certificate_from_token:
            file_certificate_from_token.write(process.stdout)

    # Сравнение записанного сертификата (tester.crt) и прочитанного с токена (certificate_from_token.crt)
    assert(ByteFileTool.comparsion_files_by_bytes("./testing_data/tester.crt", "./testing_data/certificate_from_token.crt"))

    assert(True)
