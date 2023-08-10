import subprocess
import sys

sys.path.append("..\\sources")
from execute import execute


def test_sign(reset_token, define_os):
    '''
    Тест Подписи.
    '''
    
    # Хеширование в OpenSSL
    process = execute(["openssl", "dgst",
                       "-sha256", "-binary", "./testing_data/test_data"],
                       define_os, stdout=subprocess.PIPE)

    with open("./testing_data/test_data.dgst", "wb") as file_dgst:
            file_dgst.write(process.stdout)
    
    # Генерация ключевой пары для подписи
    execute(["pkcs15-init",
             "-G", "rsa/2048",
             "--auth-id", "02",
             "--id", "45",
             "--pin", "12345678",
             "-v"], define_os)

	# Подпись
	# Для ввода пин-кода ипользуется файл user_pin, который подаётся на stdin
    file_user_pin = open("./testing_data/user_pin.txt")
	# Параметр "--pin -" позволяет считывать пин-код из stdin
    process = execute(["pkcs15-crypt",
                       "-s", "-k", "45",
                       "-i", "./testing_data/test_data.dgst",
                       "-o", "./testing_data/sign_data",
                       "--sha-256","--signature-format", "openssl",
                       "--pkcs1", "--pin", "-",
                       "-v"], define_os, stdin=file_user_pin)

    assert(process.returncode == 0)
