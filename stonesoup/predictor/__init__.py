# -*- coding: utf-8 -*-
from .base import Predictor

__all__ = ['Predictor']
__all__.extend(subclass_.__name__ for subclass_ in Predictor.subclasses)