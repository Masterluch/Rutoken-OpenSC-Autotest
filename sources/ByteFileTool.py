import os


class ByteFileTool:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_byte_file(file_name: str = "test_data", file_size_in_bytes: int = 245) -> None:
        '''
        Генерация байтового файла, заданного размера.
        '''
        with open(file_name, 'wb') as file:
            file.write(os.urandom(file_size_in_bytes))

    @staticmethod
    def comparsion_files_by_bytes(file_name_1: str, file_name_2: str) -> bool:
        '''
        По-байтовое сравнение двух файлов.
        return: 1 - файлы индентичны, 0 - файлы отличаются.
        '''
        with open(file_name_1, "rb") as file1, open(file_name_2, "rb") as file2:
            ba_file1 = bytearray(file1.read())
            ba_file2 = bytearray(file2.read())

            if len(ba_file1) != len(ba_file2): return False

            for i in range(len(ba_file1)):
                if ba_file1[i] != ba_file2[i]: return False

            return True
