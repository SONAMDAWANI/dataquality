"""
This is only to facilitate (and not necessary for) accessing the allowed constants.
Although for any methods in this project requiring objects of these types, one could
alter their arguments with 'str' instead, the classes below can be used to provide
options for each type, and prevent some mistakes.

Author: Azim Ahmadzadeh [aahmadzadeh@cs.gsu.edu], Georgia State University, 2019
"""


class AIA_WAVE:
    """
    The wavelength channel from which the image is captured. The physical units
    for this parameter is "Angstrom".
    """
    AIA_94 = "94"
    AIA_131 = "131"
    AIA_171 = "171"
    AIA_193 = "193"
    AIA_211 = "211"
    AIA_304 = "304"
    AIA_335 = "335"
    AIA_1600 = "1600"
    AIA_1700 = "1700"


class IMAGE_SIZE:
    """
    The available sizes in which the heatmaps of image parameters can be provided.
    """
    P2000 = "2k"
    P512 = "512"
    P128 = "256"


class IMAGE_PARAM:
    """
    The ids of the ten image parameters computed over each (4096 X 4096)-pixel image.
    """
    ENTROPY = '1'
    MEAN = '2'
    STD_DEVIATION = '3'
    FRACTAL_DIMENSION = '4'
    SKEWNESS = '5'
    KURTOSIS = '6'
    UNIFORMITY = '7'
    RELATIVE_SMOOTHNESS = '8'
    TAMURA_CONTRAST = '9'
    TAMURA_DIRECTIONALITY = '10'
