# flake8: noqa E501


from dlisio import dlis
import matplotlib.pyplot as plt

from fastdlis.dlis_files.classes.fast_dlis_classes import BeloDlisFast, DlisFileWrapper


class SingleBeloProcessor:
    """
    Provides static methods for processing single DLIS files, including loading files 
    and generating reports from them.

    This class is designed to work with BeloDlisFast and DlisFileWrapper objects,
    facilitating the handling and analysis of DLIS file data.
    """
    @staticmethod
    def load_dlis_wrapper(check_file: dlis.PhysicalFile) -> DlisFileWrapper:
        """
        Attempts to load a DLIS file and wraps it in a DlisFileWrapper.

        Args:
            check_file (dlis.PhysicalFile): The DLIS file to load.

        Returns:
            DlisFileWrapper: A wrapper for the DLIS file, containing file metadata and error information.
        """
        file_name = str(check_file.name)
        wrapper = DlisFileWrapper(filename=file_name)
        try:
            physical = dlis.load(check_file)
            wrapper.physical = physical
        except Exception as e:
            wrapper.error = True
            wrapper.error_message = e
        return wrapper

    @staticmethod
    def create_fast_report(dlis_wrapper: DlisFileWrapper) -> BeloDlisFast:
        """
        Generates a BeloDlisFast object from a DlisFileWrapper instance.

        Args:
            dlis_wrapper (DlisFileWrapper): The wrapper of the DLIS file to process.

        Returns:
            BeloDlisFast: An object representing processed frame data from the DLIS file.

        Raises:
            ValueError: If the DLIS file is not loaded in the wrapper.
        """
        if not dlis_wrapper.physical:
            raise ValueError("No physical file loaded in DlisFileWrapper")

        files = dlis_wrapper.physical
        frames = [frame for file in files for frame in file.find('FRAME')]
        return BeloDlisFast.from_dlis_frames(frames, dlis_wrapper.well_name, dlis_wrapper.filename)  # noqa

    @staticmethod
    def plot_report(dlis_files_data: list[dict]):
        # Extracting file names and the number of logical files
        file_names = [file['file'] for file in dlis_files_data]
        logical_files_count = [file['logical_files']
                               for file in dlis_files_data]

        # Creating the bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(file_names, logical_files_count, color='blue')

        plt.xlabel('DLIS File',  fontsize=12, weight='bold')
        plt.ylabel('Number of Logical Files', fontsize=12,  weight='bold')  # noqa
        plt.title('Logical Files in DLIS Files')
        # Rotates the x-axis labels to prevent overlapping
        plt.xticks(rotation=40,)

        plt.tight_layout()
        plt.show()
