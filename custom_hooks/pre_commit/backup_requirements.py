import sys
import shutil
import os


def main():
    # file to backup
    requirements_file = "requirements.txt"
    # backup destination
    backup_file = "requirements.backup.txt"

    # copy the requirements to the backup if they exist
    if os.path.exists(requirements_file):
        shutil.copy(requirements_file, backup_file)
        print(f"requirements backed up")
    else:
        print(f"No requirements found. Skipping backup")

    # return 0 to not block commit
    return 0


if __name__ == "__main__":
    # execute the pre-commit hook without blocking the commit
    sys.exit(main())
