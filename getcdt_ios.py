import json
import subprocess

import datetime
from dateutil.parser import parse

import git_util
import upload


class Feature:

    def __init__(self, featurename):
        self.featurename = featurename
        self.introduction_date = None


class IOSExtractor:

    def extract_toggles(self, data):
        toggles = json.loads(data)

        features = []

        for toggle in toggles["featuresConfiguration"]:
            if toggle["active"]:
                features.append(Feature(toggle["id"]))
        return features


class ToggleDurationExtractor:

    def extract(self, toggle_file, git_directory, relative_toggle_file, extractor):

        f = open(toggle_file, "r")
        data = f.read()
        f.close()

        features = extractor.extract_toggles(data)

        revisions = git_util.get_file_revisions(git_directory, relative_toggle_file)

        for feature in features:

            feature.introduction_date = datetime.datetime.now()
            for revision in revisions:
                data = git_util.get_file_revision(git_directory,
                                           relative_toggle_file, revision.revision)

                try:
                    toggles = extractor.extract_toggles(data)
                except:
                    continue

                for toggle in features:
                    if toggle.featurename == feature.featurename:
                        if parse(revision.date).replace(tzinfo=None) < feature.introduction_date:
                            feature.introduction_date = parse(revision.date).replace(tzinfo=None)
                            continue

            print feature.featurename, feature.introduction_date
            break

        # Post results to REST service
        for feature in features:
            upload.post_entry(feature.featurename, feature.introduction_date)
            break


ToggleDurationExtractor().extract(
    "/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios/ABN/ABN/Resources/featureToggles/FeatureToggles.json",
    "/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios",
    "./ABN/ABN/Resources/featureToggles/FeatureToggles.json",
    IOSExtractor())