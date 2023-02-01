Imports
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''
    __slots__ = "_prop","_imageR"
    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self._prop = flip_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        if self._prop == "horizontal" :
            self._imageR = image.transpose(method=Image.FLIP_LEFT_RIGHT)
        else :
            self._imageR = image.transpose(method=Image.FLIP_TOP_BOTTOM)
        return self._imageR
