#!/usr/bin/ennv python
import toml
import re


def parse_requirement(line):
    match = re.match(r"([a-zA-Z0-9-_]+)([><=]{0,2}[.0-9]+)?", line)
    if match:
        package, version = match.groups()
        if version:
            return package, version
        else:
            return package, "^0.0.0"
    return None, None


def update_dependencies(pyproject_file, requirements_file, dependencies_key):
    # Read pyproject.toml
    with open(pyproject_file, "r") as f:
        pyproject_data = toml.load(f)

    # Read requirements.txt
    with open(requirements_file, "r") as f:
        requirements = [line.strip() for line in f.readlines()]

    # Update dependencies
    for requirement in requirements:
        package, version = parse_requirement(requirement)
        if package and not package.startswith("-"):
            pyproject_data["tool"]["poetry"][dependencies_key][package] = version

    # Write updated pyproject.toml
    with open(pyproject_file, "w") as f:
        toml.dump(pyproject_data, f)


if __name__ == "__main__":
    update_dependencies("pyproject.toml", "requirements.txt", "dependencies")
    update_dependencies("pyproject.toml", "requirements-dev.txt", "dev-dependencies")
