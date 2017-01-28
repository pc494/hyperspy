import nose.tools as nt
import numpy as np

from hyperspy._signals.signal1d import Signal1D
from hyperspy._signals.signal2d import Signal2D


class Test2D:

    def setup_method(self, method):
        self.s = Signal1D(np.random.random((2, 3)))

    def test_to_signal2D(self):
        im = self.s.to_signal2D()
        assert isinstance(im, Signal2D)
        assert im.data.shape == self.s.data.T.shape
        assert im.data.flags["C_CONTIGUOUS"]


class Test3D:

    def setup_method(self, method):
        self.s = Signal1D(np.random.random((2, 3, 4)))

    def test_to_signal2D(self):
        im = self.s.to_signal2D()
        assert isinstance(im, Signal2D)
        assert im.data.shape == (4, 2, 3)
        assert im.data.flags["C_CONTIGUOUS"]


class Test4D:

    def setup_method(self, method):
        self.s = Signal1D(np.random.random((2, 3, 4, 5)))

    def test_to_signal2D(self):
        im = self.s.to_signal2D()
        assert isinstance(im, Signal2D)
        assert im.data.shape == (5, 2, 3, 4)
        assert im.data.flags["C_CONTIGUOUS"]
