import tempfile
import os

def write_temp_file(data: bytes, suffix: str = ".tmp") -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(data)
        tmp.flush()
        return tmp.name

def cleanup_file(path: str):
    if os.path.exists(path):
        os.remove(path)
