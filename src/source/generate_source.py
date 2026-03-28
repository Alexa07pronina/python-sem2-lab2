from src.models import Task
from typing import List,Optional
from src.constants import payloads_example
import random

class GeneratorSource:
    """генератор задач"""
    def __init__(self,count_task:int, seed: Optional[int] = None, priority: Optional[int] = None):
        self.count_task = count_task
        self._seed = seed
        self._priority = priority

    def get_tasks(self)->List[Task]:
        """ Генерация задач """
        if self._seed is not None:
            random.seed(self._seed)
        tasks=[]
        for i in range(self.count_task):
            task_payload = random.choice(payloads_example)
            priority = self._priority if self._priority is not None else random.randint(1,5)
            tasks.append(Task(payload=task_payload,priority=priority))
        return tasks
