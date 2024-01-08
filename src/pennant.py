import sys
import inspect

from typing import Callable
from functools import wraps
from contextlib import contextmanager

# This module started from an implenentation of the following blog post:
# https://tkjoetang.medium.com/python-decorator-use-it-as-feature-flag-b28f1c03bcc9

# Code flagging stems from the approach taken by the accepted answers on SO:
# https://stackoverflow.com/questions/13639482/how-to-stop-statements-within-a-python-with-context-from-executing
# https://stackoverflow.com/questions/12594148/skipping-execution-of-with-block
# https://stackoverflow.com/questions/3711184/how-to-use-inspect-to-get-the-callers-info-from-callee-in-python

# This also adopts part of the approach for AnonymousBlocksInPython:
# https://code.google.com/archive/p/ouspg/wikis/AnonymousBlocksInPython.wiki

class FEATURE_FLAG_CODE(object):

  def __init__(self, condition: bool = True):
    """ Constructor """
    self.condition = condition

  def __enter__(self):
    """ If condition falsy, get the calling frame, raise exception """
    if not self.condition:
      sys.settrace(lambda *args, **keys: None)
      frame = inspect.currentframe().f_back
      frame.f_trace = self.__flagged_code_exception
      self.start = frame.f_lasti

  def __flagged_code_exception(self, *args):
    """ Raise the exception with custom type that just passes """
    raise FlaggedCodeException

  def __exit__(self, *args):
    """ Return to the code after the with... block """
    return True

class FlaggedCodeException(Exception):
  """ Do, like...nothing? """
  pass

def FEATURE_FLAG_FUNCTION(status: bool = True) -> Callable:
  """ Creates decorator for wrapping functions to feature flag in/out """
  def feature_flag(function: Callable):
    @wraps(function)
    def wrapper(*args, **kwargs) -> Callable:
      if status:
        function(*args, **kwargs)
    return wrapper
  return feature_flag
