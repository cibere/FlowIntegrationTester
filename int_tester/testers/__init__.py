from ..loader import PythonFile
from pathlib import Path
from .protocol import PluginTester

testers_dir = Path(__file__).parent


def fetch(name: str) -> type[PluginTester]:
    path = testers_dir / f"{name}.py"
    file = PythonFile(path)
    module = file.run()
    return module.tester
