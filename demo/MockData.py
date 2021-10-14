import json
import logging
import signal
from functools import wraps
from random import randint
import time
import yaml

from .ProcessData import ProcessData

logger = logging.getLogger()
logger.setLevel(logging.INFO)

config_yaml_file = open("/Users/suhaskashyap/PycharmProjects/pythonProject/config.yaml")
config = yaml.load(config_yaml_file, Loader=yaml.FullLoader)
config = config["Configrations"]


def timeout(timeout_secs: int):
    """
    wrapper function for running function for particular amount of time

     :param timeout_secs : Time in seconds till that function needs to run
     :return: N/A
     """

    def wrapper(func):
        @wraps(func)
        def time_limited(*args, **kwargs):
            # Register an handler for the timeout
            def handler(signum, frame):
                raise Exception(f"Timeout for function '{func.__name__}'")

            # Register the signal function handler
            signal.signal(signal.SIGALRM, handler)

            # Define a timeout for your function
            signal.alarm(timeout_secs)
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                raise exc
            finally:
                # disable the signal alarm
                signal.alarm(0)
            return result

        return time_limited

    return wrapper


def write_data_to_file(json_data):
    try:
        with open('input.txt', 'a') as f:
            json.dump(json_data, f)
    except:
        logging.error("Error file i/o operation")


# 40-120(considered min, max heart rate range )
# 12 -25( considered min, max resp rate range)
class Simulation():

    @timeout(config["timeTorRunSimulationInSeconds"]+1)
    def simulate_mock_data(self, activity, p_data):
        """
        Function that generates mock data every second with diff heart rate and resp rate and incremental activity
        for every second.

         :param activity: Initial activity start rate
         :param p_data: Object of process data
         :return: N/A
         """
        try:
            while True:
                activity = activity + 1
                json_data = {'user_id': "abc", 'timestamp': time.time(), 'heart_rate': randint(40, 120),
                             'respiration_rate': randint(12, 25),
                             'activity': activity}
                p_data.add_data_to_df(json_data)
                logging.info("writing data for user abc {0}".format(json_data))
                write_data_to_file(json_data)
                time.sleep(1)
        except Exception as e:
            logging.error("problem occurred generating mock data {0}".format(e))
