# nlogging

## Description

`nlogging` is a Python library for a Simple logging Liblary.

## Installaction

```bash
pip install nlogging
```

## Usage

```python
from nlogging import nLogging
from nlogging import DEBUG, INFO, WARNING, ERROR, CRITICAL, NOOUT


def subfunc1():
	logging.output(DEBUG, 'message for debugging.')
	logging.output(CRITICAL, 'message for critical!')

def subfunc2():
	logging.output(DEBUG, 'message for debugging.')
	logging.output(CRITICAL, 'message for critical!')



logging = nLogging('YourLoggerName', './sample.log')

logging.set_out_level(stream_lv=DEBUG, file_lv=DEBUG)
logging.output(DEBUG, 'message for debugging.')
logging.output(CRITICAL, 'message for critical!')


logging.set_out_level(stream_lv=INFO, file_lv=INFO)
subfunc1()

logging.set_out_level(stream_lv=NOOUT, file_lv=WARNING)
subfunc2()
```

result(stream)
```
2024/03/17 18:18:29.602 DEBUG    exsample.py(19) [<module>] message for debugging.
2024/03/17 18:18:29.602 CRITICAL exsample.py(20) [<module>] message for critical!
2024/03/17 18:18:29.602 CRITICAL exsample.py(7) [subfunc1] message for critical!
```
result(file)
```text
2024/03/17 18:18:29.602 DEBUG    exsample.py(19) [<module>] message for debugging.
2024/03/17 18:18:29.602 CRITICAL exsample.py(20) [<module>] message for critical!
2024/03/17 18:18:29.602 CRITICAL exsample.py(7) [subfunc1] message for critical!
2024/03/17 18:18:29.602 CRITICAL exsample.py(11) [subfunc2] message for critical!
```
