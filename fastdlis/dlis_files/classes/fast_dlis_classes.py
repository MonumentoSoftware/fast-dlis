# flake8: noqa E501

from dataclasses import dataclass
from typing import List, Optional
from dlisio import dlis


@dataclass
class BeloFastFrame:
    """
    Represents a frame in a DLIS file, holding metadata and channel information.
    The class is designed to use the __post_init__ method to populate attributes.

    Attributes:
        file_name (str): The name of the file containing the frame.
        well_name (Optional[str]): The name of the well associated with the frame.
        logical_file (Optional[str]): The logical file name in the DLIS file.
        channels (List[str]): A list of channel names in the frame.
        index_min (Optional[int]): The minimum index value of the frame data.
        index_max (Optional[int]): The maximum index value of the frame data.
        units (List[str]): Units for each channel in the frame.
        index_units (Optional[str]): Units for the index channel.
    """
    file_name: str
    well_name: Optional[str] = None
    logical_file: Optional[str] = None
    channels: List[str] = None
    index_min: Optional[int] = None
    index_max: Optional[int] = None
    units: List[str] = None
    index_units: Optional[str] = None

    def __post_init__(self, frame: dlis.Frame):
        self.logical_file = frame.logicalfile
        self.channels = [str(ch.name) for ch in frame.channels]
        self.index_min = frame.index_min
        self.index_max = frame.index_max
        self.units = [ch.units for ch in frame.channels]
        self.index_units = self.units[0] if self.units else None
        if 'INDEX' in self.channels[0]:
            self.channels[0] = 'DEPT'

    def as_dict(self) -> dict:
        """
        Converts the frame data to a dictionary, excluding the units attribute.

        Returns:
            dict: The frame data as a dictionary.
        """
        return {k: v for k, v in self.__dict__.items() if k != 'units'}


@dataclass
class BeloDlisFast:
    """
    Represents a collection of BeloFastFrame instances, providing methods for 
    creating and managing frame data from DLIS files.

    Attributes:
        file_name (str): The name of the DLIS file.
        frames (List[BeloFastFrame]): A list of BeloFastFrame instances.
    """
    file_name: str
    frames: List[BeloFastFrame]

    @classmethod
    def from_dlis_frames(cls, dlis_frames: List[dlis.Frame], well_name: Optional[str] = None, file_name: Optional[str] = None):  # noqa
        """"
        Class method is a factory method that instantiates the class 
        using DLIS frame data. This is a good use of class methods for alternative constructors.
        """

        fast_frames = [BeloFastFrame(frame, file_name, well_name)
                       for frame in dlis_frames]
        return cls(file_name=file_name, frames=fast_frames)

    def frame_dict_list(self) -> List[dict]:
        """
        Converts all frames in the collection to a list of dictionaries.

        Returns:
            List[dict]: A list of dictionaries representing each frame.
        """
        return [frame.as_dict() for frame in self.frames]


@dataclass
class DlisFileWrapper:
    """
    A wrapper class for DLIS files that stores file metadata and any errors encountered 
    during file processing.

    Attributes:
        filename (Optional[str]): Name of the DLIS file.
        well_name (Optional[str]): Name of the well associated with the file.
        physical (Optional[dlis.PhysicalFile]): The DLIS physical file instance.
        path (Optional[str]): The file path of the DLIS file.
        error (bool): Indicates if any error occurred during file processing.
        error_message (Optional[Exception]): The exception raised, if any.
    """
    filename: Optional[str] = None
    well_name: Optional[str] = None
    physical: Optional[dlis.PhysicalFile] = None
    path: Optional[str] = None
    error: bool = False
    error_message: Optional[Exception] = None
