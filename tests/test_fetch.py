from src.loader import fetch_tasks
from src.models import Task
import pytest


class TestSource:
    def get_tasks(self):
        return [Task(payload={}),Task(payload={"status":"ok"})]

class FakeSource:
    pass

def test_fetch_tasks():
    """ Тест функции приема задач на валидность источника"""
    source_true=TestSource()
    source_fake=FakeSource()
    tasks=fetch_tasks(source_true)
    assert len(tasks)==2
    with pytest.raises(TypeError):
        fetch_tasks(source_fake)
