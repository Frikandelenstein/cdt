import json
import subprocess

import datetime
from dateutil.parser import parse

import git_util



class ToggleDurationExtractor:

    def extract(self):
        f = open("/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios/ABN/ABN/Resources/featureToggles/FeatureToggles.json", "r")
        data = f.read()
        f.close()

        toggles = json.loads(data)

        features = []

        for toggle in toggles["featuresConfiguration"]:
            if toggle["active"]:
                features.append(toggle["id"])

        revisions = git_util.get_file_revisions("/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios", "./ABN/ABN/Resources/featureToggles/FeatureToggles.json")

        for feature in features:

            earliest_date = datetime.datetime.now()
            for revision in revisions:
                data = git_util.get_file_revision("/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios",
                                           "./ABN/ABN/Resources/featureToggles/FeatureToggles.json", revision.revision)

                try:
                    toggles = json.loads(data)
                    for toggle in toggles["featuresConfiguration"]:
                        if toggle["id"] == feature:
                            if parse(revision.date).replace(tzinfo=None) < earliest_date:
                                earliest_date = parse(revision.date).replace(tzinfo=None)
                                continue


                except:
                    continue
            print earliest_date


ToggleDurationExtractor().extract()