import subprocess

import datetime
from dateutil.parser import parse


class ToggleDurationExtractor:

    def extract(self):
        annotate_output = subprocess.check_output(['git', 'annotate', 'FeatureToggleConfig.java'])

        output = ""
        for line in annotate_output.strip().split('\n'):
            if "@FeatureToggleBind(" in line:
                name = line.split("toggleName")[1].split("\"")[1].split("\"")[0].strip()
                time_delta = datetime.datetime.now() - parse(line.split('\t')[2]).replace(tzinfo=None)
                print name, time_delta.seconds

ToggleDurationExtractor().extract()