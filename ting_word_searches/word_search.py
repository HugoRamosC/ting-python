from ting_file_management.queue import Queue
from ting_file_management.file_process import create_file_dict


def create_search_dict(word: str, instance: Queue, line_content: bool):
    for index in range(len(instance)):
        path_file = instance.search(index)
        file_dict = create_file_dict(path_file)
        file_lines = file_dict["linhas_do_arquivo"]
        lines = []

    for i, line in enumerate(file_lines):
        if word.lower() in str(line).lower():
            if line_content:
                line_dict = {"linha": i + 1, "conteudo": line}
            else:
                line_dict = {"linha": i + 1}
            lines.append(line_dict)

    finded_dict = {
        "palavra": word.lower(),
        "arquivo": path_file,
        "ocorrencias": lines,
    }

    return finded_dict


def exists_word(word, instance):
    files_list = []
    finded_dict = create_search_dict(word, instance, False)

    if len(finded_dict["ocorrencias"]) == 0:
        return []

    files_list.append(finded_dict)
    return files_list


def search_by_word(word, instance):
    files_list = []
    finded_dict = create_search_dict(word, instance, True)

    if len(finded_dict["ocorrencias"]) == 0:
        return []

    files_list.append(finded_dict)
    return files_list
