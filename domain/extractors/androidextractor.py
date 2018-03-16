from domain.feature import Feature


class AndroidExtractor:

    def extract_toggles(self, data):
        features = []
        for line in data.strip().split('\n'):
            if "@FeatureToggleBind(" in line:
                name = line.split("toggleName")[1].split("\"")[1].split("\"")[0].strip()
                features.append(Feature(name))

        return features
