import json
import subprocess

import datetime
from dateutil.parser import parse

import git_util


class ToggleDurationExtractor:

    def extract(self):


        git_util.get_file_history("/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios", "./ABN/ABN/Resources/featureToggles/FeatureToggles.json")

        # f = open("/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios/ABN/ABN/Resources/featureToggles/FeatureToggles.json", "r")
        # data = f.read()
        # f.close()
        #
        # toggles = json.loads(data)
        #
        # features = []
        #
        # for toggle in toggles["featuresConfiguration"]:
        #     if toggle["active"]:
        #         features.append(toggle["id"])
        #
        # print features
        # for feature in features:
        #     trace back history until the feature was introduced





        # annotate_output = subprocess.check_output(['git', 'annotate', 'FeatureToggles.json'])
        #
        # for line in annotate_output.strip().split('\n'):
        #     if "@FeatureToggleBind(" in line:
        #         name = line.split("toggleName")[1].split("\"")[1].split("\"")[0].strip()
        #         time_delta = datetime.datetime.now() - parse(line.split('\t')[2]).replace(tzinfo=None)
        #         print name, time_delta.seconds
        #
                # TODO: Upload to rest service

ToggleDurationExtractor().extract()