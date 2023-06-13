import sys


class FileExtensionError(Exception):
    def __init__(self, message):
        self.message = message


def txt_importer(path_file):
    try:
        with open(path_file, mode="r") as file:
            if str(path_file).split('.')[-1].lower() != "txt":
                raise FileExtensionError("Formato inválido")

            # lines = [line.strip('\n') for line in file]
            return file.read().splitlines()

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return
    except FileExtensionError as e:
        print(e.message, file=sys.stderr)
        return
