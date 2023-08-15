import subprocess
import sys

sys.path.append("..\\sources")
from ByteFileTool import ByteFileTool
from execute import execute


def test_work_with_certificates(reset_token, define_os):
    '''
    Тест Работа с сертификатами.
    '''

    # Подготовка сертификата пользователя tester.crt в формате PEM с помощью OpenSSL
    execute(["openssl", "genrsa",
             "-out", "./testing_data/rootCA.key", "2048"], define_os)

    file_certificate_info = open("./testing_data/certificate_info.txt")
    execute(["openssl", "req",
             "-x509", "-new", "-nodes",
             "-key", "./testing_data/rootCA.key",
             "-sha256", "-days", "1024",
             "-out", "./testing_data/tester.crt"],
             define_os, stdin=file_certificate_info)

    # Запись сертификата на токен
    execute(["pkcs15-init",
             "--store-certificate", "./testing_data/tester.crt",
             "--auth-id", "02",
             "--id", "1",
             "--format", "pem",
             "--pin", "12345678",
             "-v"], define_os)

    # Чтение сертификата с токена
    process = execute(["pkcs15-tool", "--read-certificate", "1"],
                      define_os, stdout=subprocess.PIPE)

    with open("./testing_data/certificate_from_token.crt", "wb") as file_certificate_from_token:
            file_certificate_from_token.write(process.stdout)

    # Сравнение записанного сертификата (tester.crt) и прочитанного с токена (certificate_from_token.crt)
    assert(ByteFileTool.comparsion_files_by_bytes("./testing_data/tester.crt", "./testing_data/certificate_from_token.crt"))
