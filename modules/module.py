import requests
import json
import threading
import queue
import time
from lib.outputlib import *
# The base class of Module().
# All modules shall be inherited from this class.


class Module:
    # Init method. All variables and arguments goes here.
    def __init__(self, module_controller):
        self.module_controller = module_controller
        # Here, to be precise.
        self.args = {
            # Better not to touch these written parts.
            # There could be some serious issues if you modify these.
            # Unless you know what you are doing.
            'url': '',
            'max_threads': 10,
            'max_recursive_search': 3,
            'http_request_timeout': 1,
            'socks_request_timeout': 1,
            'http_proxy': ''
        }
        # The information category of modules.
        # If you don't use Chinese, leave it blank. We'll add that part for you.
        self.info = {
            # the displayed name of the module.
            'name': {
                'cn': '',
                'en': '',
            },
            # YOU.
            'author': '',
            # version for update checks.
            'version': '',
            # Module description. Add some fun part if you want.
            'description': {
                'cn': '',
                'en': '',
            },
            # Arguments. replace that 'args' part with your own argument name.
            # 'args': {
            #     'name': {
            #         'cn': '',
            #         'en': '',
            #     },
            # }
        }
        self.queue = queue.Queue()
        self.thread_pool = []
        self.thread_update_time = False
        self.watchdog_check_duration = 1
        self.is_complete = False
        self.results = []
        pass

    # output to controller
    def output(self):
        pass

    # Common duplication removal method.
    def remove_duplicate(self):
        pass

    # Prints the info.
    def info(self):
        pass

    # Set the internal arg to value. Unset and del works the same but without that very value argument.
    def set(self, arg, value=None):
        if arg in self.args.keys():
            return value
        else:
            return False

    # Check if the args and values are all valid.
    def arm(self):
        pass

    # The Start function for module.
    def fire(self):
        pass

    # The finalization process, if required.
    def end(self):
        pass

    # Function for multi-threading.
    def multi_thread(self, func, param=queue.Queue()):
        watch_dog = threading.Thread(target=self.watchdog)
        watch_dog.setDaemon(True)
        watch_dog.start()
        while param.qsize():
            if len(self.thread_pool) < self.args['max_threads']:
                thread = threading.Thread(target=func, args=param.get())
                thread.start()
                self.thread_pool.append(thread)
                time.sleep(self.thread_update_time)
        else:
            for item in self.thread_pool:
                item.join()
        return True

    # Watchdog, in case of fuck-ups.
    def watchdog(self):
        while 1:
            for item in self.thread_pool:
                if not item.is_alive():
                    self.thread_pool.remove(item)
                time.sleep(self.watchdog_check_duration)