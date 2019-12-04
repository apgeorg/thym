# thym [![PyPI version](https://badge.fury.io/py/thym.svg)](https://badge.fury.io/py/thym)

A simple timer component that allows you to trigger an event at a specified interval.

## Installation
### There are two ways to install thym:

Install thym from PyPI (recommended):
```
sudo pip install thym
```
If you are using a virtualenv, you may want to avoid using sudo:
```
pip install thym
```
### Alternatively: install thym from the GitHub source:
First, clone thym using `git`:
```
git clone https://github.com/apgeorg/thym.git
```
Then, cd to the thym folder and run the install command:
```
cd thym
sudo python setup.py install
```
## Getting started
### Timer
The Timer is able to trigger a callback either periodically or as a one shot by setting the `oneshot` argument correspondingly. 
There is an `elapsed` property that returns the elapsed time since `start()` was called. 
Further, a `remaining` property is also available that returns the remaining time of the specified interval.  
```python
import thym

# Timer callback function
def timer_timeout():
  print("Hello!")

# Create a Timer which runs periodically 
t = thym.Timer(1, timer_timeout, oneshot=False)

# Start running
t.start()
```
The Timer can be stopped anytime by calling `stop()` as shown below. Accordingly, the elapsed time and remaining time are calculated. 
```python
t.stop()
```

## Licence

Thym is licensed under MIT. See [LICENSE](./LICENSE) file for details.

Copyright © 2019 Apostolos Georgiadis.






