import pathlib
import sys
__version__ = '1.0.3'

sys.path.append('..\\')
DIR = pathlib.Path(__file__).parent.resolve()

from headpose.headpose import PoseEstimator
