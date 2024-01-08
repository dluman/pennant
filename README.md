# pennant

[![PyPI version](https://img.shields.io/pypi/v/pennant)](https://pypi.org/project/pennant/)

A feature flagging library that uses decorators and context management to "feature flag" certain
functions or blocks of code. I _feel_ like it's better than a bunch of conditionals, but I'm often
wrong.

## Installation

Find this tool on `PyPI`: `pip install pennant`

## Usage

Contrary to how some folks might do it, this library takes and "opt-out" approach where setting the flag to
`False` prevents the given function or code block from running. As long as the argument provided to the
decorator or content manager evaluates to `False`, anything's game.

Check this out:

```python
import pennant

@pennant.FEATURE_FLAG_FUNCTION(False)
def print_me(test: str = "Hello!") -> str:
  print(test)
  return "!"

def main():
  print("This should run none of the following.")
  print_me(test = "Yes!")
  with pennant.FEATURE_FLAG_CODE(False):
    numbers = [1,2]
    print(numbers)

if __name__ == "__main__":
  main()
```
