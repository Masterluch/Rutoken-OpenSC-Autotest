# Rutoken-OpenSC-Autotest

В данном репозитории представлен набор OpenSC-тестов для тестирования устройств [Rutoken ECP](https://www.rutoken.ru/products/all/) на операционных системах Windows и Linux. Для тестирования используется python-библиотека pytest.

# Перечень тестов

- Тест расшифрования: `test_decryption.py`;
- Тест подписи: `test_sign.py`;
- Тест работы с двоичными файлами: `test_work_with_binary_files.py`;
- Тест работы с сертификатами: `test_work_with_certificates.py`;
- Тест ГОСТа: `test_GOST.py`.

# Запуск тестов

1. Установите [OpenSC](https://github.com/OpenSC/OpenSC) и [OpenSSL](https://github.com/openssl/openssl).
2. Для операционной системы Linux понадобится библиотека [librtpkcs11ecp.so](https://www.rutoken.ru/support/download/pkcs/).
3. Установка всех необходимых python библиотек (в том числе pytest)
    
    ```bash
    Rutoken-OpenSC-Autotest> pip install -r requirements.txt
    ```
    
4. Запуск всех тестов
    
    ```bash
    Rutoken-OpenSC-Autotest> cd tests
    Rutoken-OpenSC-Autotest\tests> pytest
    ```
    

# Справка

### Особенность использования библиотек c `pkcs11-tool` в тестах

Если в тесте необходимо использовать библиотеки rtpkcs11ecp.dll (Windows) или librtpkcs11ecp.so (Linux) то вместо наименования самой библиотеки использовать “rtpkcs11ecp”. Функция `execute()` подставит нужное наименование в зависимости от операционной системы.

Пример использования

```python
execute(["pkcs11-tool", "--module", "./rtpkcs11ecp"], define_os)
```