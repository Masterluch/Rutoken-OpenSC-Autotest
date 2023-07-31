import pytest
import subprocess


@pytest.fixture()
def reset_token():
    '''
    Очистака и подготовка токена.
    '''

    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-init.exe",
                                "--erase-card",
                                "-v", "-r3"],
                                stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    
    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-init.exe",
                              "--create-pkcs15",
                              "--so-pin", "87654321",
                              "--so-puk", "",
                              "--pin", "12345678",
                              "-v", "-r3"],
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)
    
    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-init.exe",
                              "--store-pin",
                              "--label", "User PIN",
                              "--auth-id", "02",
                              "--pin", "12345678",
                              "--puk", "",
                              "--so-pin", "87654321",
                              "--finalize", "-v", "-r3"],
                              stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)
    
    yield

    process = subprocess.run(["C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\pkcs15-init.exe",
                                "--erase-card",
                                "-v", "-r3"],
                                stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)
