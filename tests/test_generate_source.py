from src.source.generate_source import GeneratorSource


def test_generate_source():
    """ тест генеративного источника"""
    source = GeneratorSource(5)
    assert len(source.get_tasks())==5
    assert 1<=source.get_tasks()[0].priority<=5
