import json
import subprocess

import datetime
from dateutil.parser import parse

import git_util

class Feature:

    def __init__(self, featurename):
        self.featurename = featurename
        self.introduction_date = None

class ToggleDurationExtractor:

    def extract(self):
        f = open("/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios/ABN/ABN/Resources/featureToggles/FeatureToggles.json", "r")
        data = f.read()
        f.close()

        toggles = json.loads(data)

        features = []

        for toggle in toggles["featuresConfiguration"]:
            if toggle["active"]:
                features.append(Feature(toggle["id"]))

        revisions = git_util.get_file_revisions("/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios", "./ABN/ABN/Resources/featureToggles/FeatureToggles.json")

        for feature in features:

            feature.introduction_date = datetime.datetime.now()
            for revision in revisions:
                data = git_util.get_file_revision("/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios",
                                           "./ABN/ABN/Resources/featureToggles/FeatureToggles.json", revision.revision)

                try:
                    toggles = json.loads(data)
                except:
                    continue

                for toggle in toggles["featuresConfiguration"]:
                    if toggle["id"] == feature.featurename:
                        if parse(revision.date).replace(tzinfo=None) < feature.introduction_date:
                            feature.introduction_date = parse(revision.date).replace(tzinfo=None)
                            continue

            print feature.featurename, feature.introduction_date


ToggleDurationExtractor().extract()