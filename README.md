
# GitHub Activity

## Overview

`github-activity` is a simple command-line tool that retrieves and displays activity data for a given GitHub user. The program fetches recent events for a specified user from the GitHub API and provides a summary of various types of activities.

https://roadmap.sh/projects/github-user-activity

## Features

- Fetch and display commit messages from push events.
- Count and display the number of different types of GitHub events:
  - Push events
  - Pull request events
  - Pull request reviews
  - Issues events
  - Other events

## Installation

You can install `github-activity` using pip. Run the following command in your terminal:

```sh
pip install .
```

This will install the package along with its dependencies.

## Usage

Once installed, you can use the command-line tool `github-activity` to fetch and display GitHub user activity. 

### Command-Line Interface

To use the tool, run:

```sh
github-activity <username>
```

Replace `<username>` with the GitHub username you want to get the activity for.

### Example

```sh
github-activity diegarlin
```

This command will fetch and display the activity data for the user `diegarlin`.

## Output

The output will include:

1. **Commit Messages**: A list of commit messages from push events.
2. **Events Count**: A summary of different types of events, including:
   - Push events
   - Pull request events
   - Pull request reviews
   - Issues events
   - Other events

## Error Handling

- If the specified user does not exist, you will receive a message: `This user doesn't exist.`

## Dependencies

The tool requires the `requests` library. It is specified as a dependency in the setup configuration and will be installed automatically.

## License

This project is licensed under the MIT License. See the LICENSE file for details.