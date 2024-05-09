# GitHub Data Extraction Tool

This tool is designed to extract data from GitHub repositories, focusing on merged pull requests (PRs). It collects data about PR commits, their diffs, and associated comments, and saves this information in a JSON Lines format for efficient data handling.

## Prerequisites

Before you start using this tool, you need to have the following installed:
- Python 3.6 or higher
- `requests` library
- `typer` library
- `python-dotenv` library

You also need a GitHub personal access token with appropriate permissions to access the repository data. This token should have the `repo` scope to access private repositories or `public_repo` for public repositories.

## Installation

1. Clone this repository:
   `bash
   git clone https://github.com/virevol/yourrepository.git
   `
2. Navigate to the project directory:
   `bash
   cd yourrepository
   `
3. Install the required Python packages:
   `bash
   make dev
   `

## Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your GitHub personal access token to the `.env` file:
   `
   GITHUB_TOKEN=your_personal_access_token_here
   `

## Usage

Run the script from the command line using Typer. You can specify the repository owner, repository name, and optionally the branch (defaults to `master`).

`bash
python script_name.py --repo-owner <owner> --repo-name <repository> --branch <branch> --output-file <output_file>
`

### Parameters:
- `--repo-owner`: Owner of the GitHub repository (username or organization name).
- `--repo-name`: Name of the repository.
- `--branch`: Branch to analyze (default is `master`).
- `--output-file`: Output file name (default is `github_data.jsonl`).

### Example

`bash
python script_name.py --repo-owner example_user --repo-name example_repo --branch master --output-file data.jsonl
`

## Output

The script writes the data to a specified JSON Lines file. Each line in the file is a valid JSON object that represents a PR with its commits, diffs, and comments, along with the status of the PR (merged).

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
