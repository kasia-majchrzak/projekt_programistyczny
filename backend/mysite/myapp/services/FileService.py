from msilib.schema import File


def get_data_from_file(file: File) -> str:
    data = file.read()
    text_data = data.decode('utf-8')
    return str(text_data)


class FileService:

    def __init__(self, file: File):
        self._file = file
