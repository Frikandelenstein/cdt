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

class AndroidExtractor:

    def extract_toggles(self, data):
        features = []
        for line in data.strip().split('\n'):
            if "@FeatureToggleBind(" in line:
                name = line.split("toggleName")[1].split("\"")[1].split("\"")[0].strip()
                features.append(Feature(name))

        return features

class ToggleDurationExtractor:

    def extract(self, platform, toggle_file, git_directory, relative_toggle_file, extractor):

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

                for toggle in toggles:
                    if toggle.featurename == feature.featurename:
                        if parse(revision.date).replace(tzinfo=None) < feature.introduction_date:
                            feature.introduction_date = parse(revision.date).replace(tzinfo=None)


            print platform, feature.featurename, feature.introduction_date
            # break

        # Post results to REST service
        for feature in features:
            upload.post_entry(platform, feature.featurename, feature.introduction_date)
            # break

# Android
ToggleDurationExtractor().extract(
    "android",
    "/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-android/ABN/src/main/java/com/abnamro/nl/mobile/payments/core/toggle/feature/FeatureToggleConfig.java",
    "/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-android",
    "./ABN/src/main/java/com/abnamro/nl/mobile/payments/core/toggle/feature/FeatureToggleConfig.java",
    AndroidExtractor())

# iOS
ToggleDurationExtractor().extract(
    "ios",
    "/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios/ABN/ABN/Resources/featureToggles/FeatureToggles.json",
    "/Users/roderik.lagerweij/Documents/workspace/mobiel-bankieren-ios",
    "./ABN/ABN/Resources/featureToggles/FeatureToggles.json",
    IOSExtractor())