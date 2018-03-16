import subprocess


def get_file_revisions(git_directory, relative_feature_file):
    # change to git working directory and execute command there
    output = subprocess.check_output(['git', 'log', '-p', relative_feature_file], cwd=git_directory)

    revisions = []

    for line in output.split("\n"):

        if line.strip().startswith("commit"):
            revision = line.strip().split(" ")[1]
            revisions.append(revision)

    return revisions




