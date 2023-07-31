import subprocess


def test_sign(reset_token):
    '''
    Тест Подписи.
    '''
    
    # Хеширование в OpenSSL
    process = subprocess.run(["openssl", "dgst",
                              "-sha256", "-binary", "./testing_data/test_data"],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    with open("./testing_data/test_data.dgst", "wb") as file_dgst:
            file_dgst.write(process.stdout)
    
    # Генерация ключевой пары для подписи
    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-init.exe",
                              "-G", "rsa/2048",
                              "--auth-id", "02",
                              "--id", "45",
                              "--pin", "12345678",
                              "-v", "-r3"],
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    file_user_pin = open("./testing_data/user_pin.txt")
    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-crypt.exe",
                                "-s", "-k", "45",
                                "-i", "./testing_data/test_data.dgst",
                                "-o", "./testing_data/sign_data",
                                "--sha-256","--signature-format", "openssl",
                                "--pkcs1", "--pin", "-",
                                "-v", "-r3"],
                                stdin=file_user_pin,
                                stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    assert(process.returncode == 0)
