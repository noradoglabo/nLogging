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
