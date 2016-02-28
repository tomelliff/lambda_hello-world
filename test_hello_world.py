from nose.tools import assert_equals, assert_raises

from hello_world import lambda_handler

import json
import logging

logging.getLogger().setLevel(logging.DEBUG)

def test_hello_world():

  event = { 'object': 'world' }

  logging.debug(event)

  assert_equals(lambda_handler(event, None), "Hello world!")

def test_hello_world_casing():

  event = { 'object': 'World' }

  logging.debug(event)

  assert_equals(lambda_handler(event, None), "Hello World!")

def test_hello_tom():

  event = { 'object': 'Tom' }

  logging.debug(event)

  assert_raises(ValueError, lambda_handler, event, None)

def test_hello_key_error():

  event = { 'error': 'world' }

  logging.debug(event)

  assert_raises(KeyError, lambda_handler, event, None)
