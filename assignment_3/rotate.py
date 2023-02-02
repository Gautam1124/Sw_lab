#Imports
from PIL import Image

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''
    __slots__ = "_deg"
    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        self._deg = degrees

    def __call__(self, sample):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        self._img = sample.rotate(self._deg, PIL.Image.NEAREST, expand = 1)
        return self._img
