from typing import List
from src.protocols import TaskSource
from src.models import Task

def fetch_tasks(source: TaskSource) -> List[Task]:
    """Получение задач из любого допустимого источника"""
    if not isinstance(source, TaskSource):
        raise TypeError(f"{source} не соответствует контракту TaskSource")
    return source.get_tasks()

