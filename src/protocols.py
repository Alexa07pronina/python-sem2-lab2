from typing import Protocol,runtime_checkable
from src.models import Task
from typing import List

@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> List[Task]:
        """Список задач"""
        ...

