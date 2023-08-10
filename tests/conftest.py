import pytest
import subprocess
import sys

sys.path.append("..\\sources")
from execute import execute


@pytest.fixture(scope="session")
def define_os() -> str:
    '''
    Определение ОС для корректной работы тестов.
    '''
    return sys.platform

@pytest.fixture()
def reset_token(define_os):
    '''
    Очистака и подготовка токена.
    '''

    execute(["pkcs15-init", "--erase-card", "-v"], define_os)
    
    execute(["pkcs15-init",
             "--create-pkcs15",
             "--so-pin", "87654321",
             "--so-puk", "",
             "--pin", "12345678", "-v"],
             define_os)

    execute(["pkcs15-init",
             "--store-pin",
             "--label", "User PIN",
             "--auth-id", "02",
             "--pin", "12345678",
             "--puk", "",
             "--so-pin", "87654321",
             "--finalize", "-v"],
             define_os)
    
    yield

    execute(["pkcs15-init", "--erase-card", "-v"], define_os)
