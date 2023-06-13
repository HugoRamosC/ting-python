import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    if len(instance) != 0 and path_file in instance.queue:
        return

    content_list = txt_importer(path_file)
    file_dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(content_list),
        'linhas_do_arquivo': content_list,
    }
    instance.enqueue(file_dict['nome_do_arquivo'])
    print(file_dict, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
