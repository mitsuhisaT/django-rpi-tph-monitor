"""Data container classes."""
import logging
from django.utils import timezone

logger = logging.getLogger(__name__)


class BME280dc():
    """Data Container for BME280 model."""

    def __init__(self, t: float, p: float, h: float):
        """
        Constractor.

        Params:
            t (float): temperature 気温
            p (float): pressure 気圧
            h (float): humidity 湿度
        """
        self.__t = t
        self.__p = p
        self.__h = h
        self.__mdt = timezone.now()

    @property
    def t(self):
        """Get temperature."""
        return self.__t

    @t.setter
    def t(self, t):
        """Set temperature."""
        self.__t = t

    @property
    def p(self):
        """Get pressure."""
        return self.__p

    @p.setter
    def p(self, p):
        """Set pressure."""
        self.__p = p

    @property
    def h(self):
        """Get humidity."""
        return self.__h

    @h.setter
    def h(self, h):
        """Set humidity."""
        self.__h = h

    @property
    def mdt(self):
        """Get measured datetime."""
        return self.__mdt
