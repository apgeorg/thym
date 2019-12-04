# thyme [![PyPI version](https://badge.fury.io/py/thyme.svg)](https://badge.fury.io/py/thyme)
TODO

## Installation
### There are two ways to install thyme:

Install thyme from PyPI (recommended):
```
sudo pip install thyme
```
If you are using a virtualenv, you may want to avoid using sudo:
```
pip install thyme
```
### Alternatively: install thyme from the GitHub source:
First, clone thyme using `git`:
```
git clone https://github.com/apgeorg/thyme.git
```
Then, cd to the thyme folder and run the install command:
```
cd thyme
sudo python setup.py install
```
## Getting started
### Timer
```python
import thyme

# Timer callback function
def timer_timeout():
  print("Hello!")

# Create a Timer which runs periodically 
t = thyme.Timer(1, timer_timeout, oneshot=False)

# Start running
t.start()
```

You can now stop the timer:

```python
t.stop()
```






