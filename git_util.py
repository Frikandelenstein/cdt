import subprocess

class GitRevision:

    def __init__(self, revision, date):
        self.revision = revision
        self.date = date

def get_file_revisions(git_directory, relative_feature_file):
    # change to git working directory and execute command there
    output = subprocess.check_output(['git', 'log', '-p', relative_feature_file], cwd=git_directory)

    revisions = []

    lines = output.strip().split("\n")

    for idx, line in enumerate(lines):

        if line.strip().startswith("commit"):

            revision = line.strip().split(" ")[1]

            if lines[idx+2].strip().startswith("Date:"):
                date = lines[idx+2].strip().split("Date:")[1].strip()
            elif lines[idx+3].strip().startswith("Date:"):
                date = lines[idx + 3].strip().split("Date:")[1].strip()

            revisions.append(GitRevision(revision, date))

    return revisions

def get_file_revision(git_directory, f, revision):
    output = subprocess.check_output(['git', 'show', revision + ":" + f], cwd=git_directory)
    return output




