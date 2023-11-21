from rich.table import Table
from rich.progress import track
from typing import List, Dict

from fastdlis.utils.console import console


def display_dlis_files_info(files_data: List[Dict]):

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("File", style="dim", width=20)
    table.add_column("Well Name")
    table.add_column("Size")
    table.add_column("Error", justify="right")
    table.add_column("Logical Files", justify="right")

    for file_data in track(files_data, description="Processing..."):
        table.add_row(
            file_data['file'],
            file_data['well'],
            file_data['size'],
            "Yes" if file_data['error'] else "No",
            str(file_data['logical_files'])
        )

    console.print(table)
