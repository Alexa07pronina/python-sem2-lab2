from src.source.fake_api_source import FakeApiSource

def test_fake_api_source():
    """Тест источника API"""
    source = FakeApiSource("http://example2.com")
    tasks = source.get_tasks()
    assert len(tasks) == 3

    assert isinstance(tasks[0].id, str)
    assert len(tasks[0].id) == 36
    assert tasks[0].payload == {"role": "admin", "ip": "255.255.255.255"}
    assert tasks[0].priority == 5
    assert tasks[0].status == "pending"
