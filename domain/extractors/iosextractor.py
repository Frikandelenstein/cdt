import json

from domain.feature import Feature


class IOSExtractor:

    def extract_toggles(self, data):
        toggles = json.loads(data)

        features = []

        for toggle in toggles["featuresConfiguration"]:
            if toggle["active"]:
                features.append(Feature(toggle["id"]))
        return features
