import argparse
import os

from alive_progress import alive_bar
import dlisio
from fastdlis.dlis_files.rich_preview import display_dlis_files_info

from fastdlis.dlis_files.single_belo import SingleBeloProcessor
from fastdlis.utils.json_io import write_json
from fastdlis.utils import walker
from fastdlis.utils.paths import get_size
from fastdlis.utils.types import DlisFileDict


path_espirito_santo = r"C:\Users\Usuário\pedro\Monumento-master\POCO\Categoria-1"  # noqa


def get_general_file_info(path: str, output_name: str = 'output.json') -> None:
    """
    Gets all folders inside a directory, and then loops in each folder
    looking for .dlis files.\n
    It generates a JSON file with objects like this:
    ```json
    [
        {
            "file": "1-BRSA-412-ES_fmi.DLIS",
            "well": "1-BRSA-412-ES",
            "size": "64.6 MB",
            "error": false,
            "error_message": "",
            "logical_files": 2
        }
    ]
    ```

    Args:
        path (str): _description_
        output_name (str): _description_
    """
    path = os.path.normpath(path)
    initial_tuples = walker.get_file_tags(path, ['.dlis', '.DLIS'])
    dlis_files_dicts = []

    with alive_bar(len(initial_tuples), dual_line=True, title='Dlis General Info') as bar:  # noqa
        for tuple_ in initial_tuples:
            belo = SingleBeloProcessor.load_dlis_wrapper(tuple_[1])
            file_dict = DlisFileDict(
                file=tuple_[1].name,
                well=tuple_[0],
                size=get_size(tuple_[1]),
                error=belo.error,
                error_message=belo.error_message,
                logical_files=0,
            )
            if belo.physical is not None:
                # NOTE Gets the ammount of logical files
                *f, = belo.physical
                f: list[dlisio.dlis.LogicalFile]
                file_dict['logical_files'] = len(f)

            dlis_files_dicts.append(file_dict)
            bar()

    write_json(output_name, dlis_files_dicts)
    display_dlis_files_info(dlis_files_dicts)
    SingleBeloProcessor.plot_report(dlis_files_dicts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process .dlis files in a directory and output a summary as JSON.")  # noqa
    parser.add_argument('path', type=str, help="Path to the directory containing .dlis files")  # noqa
    args = parser.parse_args()

    get_general_file_info(args.path)
