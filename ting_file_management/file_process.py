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


def remove(instance: Queue):
    removed_name = instance.dequeue()
    if removed_name is None:
        print('Não há elementos', file=sys.stdout)
    else:
        print(f"Arquivo {removed_name} removido com sucesso", file=sys.stdout)


def file_metadata(instance: Queue, position):
    if not (0 <= position < len(instance)):
        print('Posição inválida', file=sys.stderr)
    else:
        path_file = instance.queue[position]
        content_list = txt_importer(path_file)
        file_dict = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(content_list),
            'linhas_do_arquivo': content_list,
        }
        print(file_dict, file=sys.stdout)
