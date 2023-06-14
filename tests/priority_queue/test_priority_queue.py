import pytest


from ting_file_management.priority_queue import PriorityQueue


priority_dict = {
    "nome_do_arquivo": "fake/path/test.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [
        "line 1",
        "line 2",
        "line 3",
    ],
}


fake_queue = [
    {
        "nome_do_arquivo": "fake/path/queue.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "line 1",
            "line 2",
            "line 3",
            "line 4",
            "line 5",
            "line 6",
        ],
    },
    {
        "nome_do_arquivo": "fake/path/queue_2.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": [
            "line 1",
            "line 2",
            "line 3",
            "line 4",
            "line 5",
        ],
    },
]


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue(fake_queue[0])
    queue.enqueue(fake_queue[1])
    assert len(queue) == 2
    # assert queue[0] == fake_queue[0]
    # assert queue[1]["qtd_linhas"] == 5

    queue.dequeue()
    assert len(queue) == 1
    # assert queue[0]["qtd_linhas"] == 5

    queue.enqueue(priority_dict)
    first = queue.search(0)
    assert len(queue) == 2
    assert first == priority_dict

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(5)
