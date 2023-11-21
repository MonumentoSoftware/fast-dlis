"""
This module is responsible for all the operations that contains paths.
"""


import os


def get_size(path: str) -> str:
    size = os.path.getsize(path)
    if size < 1024:
        return f"{size} bytes"
    elif size < 1024*1024:
        return f"{round(size/1024, 2)} KB"
    elif size < 1024*1024*1024:
        return f"{round(size/(1024*1024), 2)} MB"
    elif size < 1024*1024*1024*1024:
        return f"{round(size/(1024*1024*1024), 2)} GB"
