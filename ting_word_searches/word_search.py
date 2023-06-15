from ting_file_management.queue import Queue
from ting_file_management.file_process import create_dict


def exists_word(word: str, instance: Queue):
    files_list = []
    for index in range(len(instance)):
        path_file = instance.search(index)
        file_dict = create_dict(path_file)
        file_lines = file_dict["linhas_do_arquivo"]
        lines = []

    for i, line in enumerate(file_lines):
        if word.lower() in str(line).lower():
            line_dict = {"linha": i + 1}
            lines.append(line_dict)

    finded_dict = {
        "palavra": word.lower(),
        "arquivo": path_file,
        "ocorrencias": lines,
    }

    if len(lines) == 0:
        return []

    files_list.append(finded_dict)
    return files_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
