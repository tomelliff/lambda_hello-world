from __future__ import print_function

import json

def lambda_handler(event, context):
  print("Received event: {0}".format(json.dumps(event, indent=2)))
