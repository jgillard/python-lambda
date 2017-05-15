# -*- coding: utf-8 -*-
import json
import logging
import os
import time
from imp import load_source

import yaml

from .helpers import read, custom_copytree


log = logging.getLogger(__name__)


def invoke(src, alt_event=None, verbose=False):
    """Simulates a call to your function.

    :param str src:
        The path to your Lambda ready project (folder must contain a valid
        config.yaml and handler module (e.g.: service.py).
    :param str alt_event:
        An optional argument to override which event file to use.
    :param bool verbose:
        Whether to print out verbose details.
    """
    # Load and parse the config file.
    path_to_config_file = os.path.join(src, 'config.yaml')
    cfg = read(path_to_config_file, loader=yaml.load)

    # Load and parse event file.
    if alt_event:
        path_to_event_file = os.path.join(src, alt_event)
    else:
        path_to_event_file = os.path.join(src, 'event.json')
    event = read(path_to_event_file, loader=json.loads)

    handler = cfg.get('handler')
    # Inspect the handler string (<module>.<function name>) and translate it
    # into a function we can execute.
    fn = get_callable_handler_function(src, handler)

    # TODO: look into mocking the ``context`` variable, currently being passed
    # as None.

    start = time.time()
    results = fn(event, None)
    end = time.time()

    print("{0}".format(results))
    if verbose:
        print("\nexecution time: {:.8f}s\nfunction execution "
              "timeout: {:2}s".format(end - start, cfg.get('timeout', 15)))


def init(src, minimal=False):
    """Copies template files to a given directory.

    :param str src:
        The path to output the template lambda project files.
    :param bool minimal:
        Minimal possible template files (excludes event.json).
    """

    destination = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "project_templates")
    custom_copytree(destination, src, minimal)


def get_callable_handler_function(src, handler):
    """Tranlate a string of the form "module.function" into a callable
    function.

    :param str src:
      The path to your Lambda project containing a valid handler file.
    :param str handler:
      A dot delimited string representing the `<module>.<function name>`.
    """

    # "cd" into `src` directory.
    os.chdir(src)

    module_name, function_name = handler.split('.')
    filename = get_handler_filename(handler)

    path_to_module_file = os.path.join(src, filename)
    module = load_source(module_name, path_to_module_file)
    return getattr(module, function_name)


def get_handler_filename(handler):
    """Shortcut to get the filename from the handler string.

    :param str handler:
      A dot delimited string representing the `<module>.<function name>`.
    """
    module_name, _ = handler.split('.')
    return '{0}.py'.format(module_name)
