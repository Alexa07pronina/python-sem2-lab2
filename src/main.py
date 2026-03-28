from src.loader import fetch_tasks
from src.source.file_source import FileSource
from src.source.generate_source import GeneratorSource
from src.source.fake_api_source import FakeApiSource
from pathlib import Path

def main() -> None:
    """Точка входа"""
    project_root = Path(__file__).parent.parent
    file_path = project_root/"file_source.txt"
    if not file_path.exists():
        file_path.touch()
    list_tasks1 = fetch_tasks(FileSource(str(file_path)))
    list_tasks2 = fetch_tasks(GeneratorSource(2,seed=1))
    list_tasks3 = fetch_tasks(FakeApiSource("https://example.com"))
    print("from file: ")
    for s in list_tasks1:
        print(s)
    print("from generator: ")
    for s in list_tasks2:
        print(s)
    print("from fake api: ")
    for s in list_tasks3:
        print(s)

if __name__ == "__main__":
    main()
