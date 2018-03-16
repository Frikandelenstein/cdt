import json
import subprocess

import datetime


def post_entry(featurename, start_date):
    time_delta = datetime.datetime.now() - start_date

    dict = json.dumps({"feature": {"name": featurename, "duration": int(time_delta.total_seconds())}})
    print dict
    # subprocess.check_output(['curl', "-d", dict, "-H", "Accept: application/json", "-H", "Content-Type: application/json", '-X', 'POST', "http://frikandelenstein.herokuapp.com/features"])