"""
This module holds all the classes and functions that are used to search
and explore directories.
"""


import pathlib


class Searcher:
    """
    Main class for Searching geo files.
    Try Searcher.SearchExtensions for a more flexible approach.
    """

    @staticmethod
    def search_lis(folder_path: str):
        """Searcher for .lis files extension."""
        EXTENSIONS = {'.lis', '.LIS'}
        path = pathlib.Path(folder_path)
        return [path for path in path.glob(r'**/*') if path.suffix in EXTENSIONS]  # noqa

    @staticmethod
    def search_dlis(folder_path: str) -> list[pathlib.Path]:
        """Searcher for .dlis files extension."""
        EXTENSIONS = {'.dlis', '.DLIS'}
        path = pathlib.Path(folder_path)
        return [path for path in path.glob(r'**/*') if path.suffix in EXTENSIONS]  # noqa

    @staticmethod
    def search_las(folder_path: pathlib.Path) -> list[pathlib.Path]:
        """Searcher for .las files extension."""

        EXTENSIONS = {'.las'}
        path = pathlib.Path(folder_path)
        return [path for path in path.glob(r'**/*') if path.suffix in EXTENSIONS]  # noqa

    @staticmethod
    def search_combo(folder_path: str) -> list[pathlib.Path]:
        '''Searcher for .las, .lis e .dlis files.'''

        EXTENSIONS = {'.dlis', '.lis', '.las'}
        path = pathlib.Path(folder_path)
        return [path for path in path.glob(r'**/*') if path.suffix in EXTENSIONS]  # noqa

    @staticmethod
    def search_extensions(folder_path: str, extensions: set[str]) -> list[pathlib.Path]:  # noqa
        '''
        Search in all folders an files inside a given path for files
        with a given extension.
        '''
        path = pathlib.Path(folder_path)
        return [path for path in path.glob(r'**/*') if path.suffix in extensions]  # noqa

    @staticmethod
    def search_txt(folder_path: str, name_: str) -> list[pathlib.Path]:
        """
        Essa função pega um PATH e uma LISTA de nomes
        e retorna uma lista contendo os arquivos que correspondem
        aos arquivos de nome encontrados.
        """
        folder_paths = pathlib.Path(folder_path)
        filelist_name = []
        name_ = name_.upper()
        EXTENSIONS = {'.txt'}
        for path in folder_paths.glob(r'**/*'):
            # De Pure Path para String
            pathname = str(pathlib.PurePath(path.name)).upper()
            if name_ in pathname and path.is_file() and path.suffix in EXTENSIONS:  # noqa
                filelist_name.append(path)

        return filelist_name
