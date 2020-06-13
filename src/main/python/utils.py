import logging
from pathlib import *


# Directories

# Absolute path to dmd directory (where `fbs run` should be launched)
ROOT_DIR = Path(__file__).parent.parent.parent.parent
# Resource directory
RES_DIR = ROOT_DIR.joinpath('src/main/resources')
# Target directory for file output
TARGET_DIR = ROOT_DIR.joinpath('target')
# Cache directory
CACHE_DIR = ROOT_DIR.joinpath('cache')


def file_format(filename):
    """
    Find file format.

    :param filename: filename
    :return format: str of the file format
    """
    return Path(filename).suffix


def clear(directory: str):
    """
    Clear a directory

    :param directory: directory
    """
    if Path(directory).exists() and Path(directory).is_dir():
        for file in Path(directory).iterdir():
            try:
                if Path(file).is_dir():
                    clear(file)
                    Path(file).rmdir()
                else:
                    Path(file).unlink()
            except OSError:
                logging.error('OSError: PathError: failed to remove {0} from {1}.'.format(file, directory))


def clear_cache():
    """
    Clear cache directory.
    """
    clear(CACHE_DIR.as_posix())


def clear_target():
    """
    Clear target directory.
    """
    clear(TARGET_DIR.as_posix())


def reset_target():
    """
    Reset target working directory.
    """
    if TARGET_DIR.exists():
        clear_target()
    else:
        TARGET_DIR.mkdir()
