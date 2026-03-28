class TaskValidationError(Exception):
    """ Базовый класс оишбок """
    pass

class InvalidPriorityError(TaskValidationError):
    """ Некорректный приоритет задачи """
    pass
class InvalidStatusError(TaskValidationError):
    """ Некорректный статус задачи """
    pass

class InvalidDescriptionError(TaskValidationError):
    """ Некорректное описание задачи """
    pass