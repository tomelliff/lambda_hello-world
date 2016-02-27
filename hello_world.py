from __future__ import print_function

import json

def lambda_handler(event, context):
  print("Received event: {0}".format(json.dumps(event, indent=2)))
  try:
    event_object = event['object']
  except KeyError:
    raise KeyError("Event should contain a key called 'object'")
  if event_object != "world":
    raise ValueError("This is a 'Hello world!' function, not 'Hello {0}!".format(event_object))
  return "Hello {0}!".format(event_object)
