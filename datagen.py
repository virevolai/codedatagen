import requests
import json
import typer
from dotenv import load_dotenv
import os

app = typer.Typer()

def fetch_json(url, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises exception for HTTP errors
    return response.json()

@app.command()
def get_github_data(repo_owner: str, repo_name: str, branch: str = "master", output_file: str = "github_data.jsonl", max_changes: int = 1_000):
    load_dotenv()
    github_token = os.getenv("GITHUB_TOKEN")  # Get GitHub token from .env file
    if not github_token:
        typer.echo("GitHub token is not set. Please check your .env file.")
        raise typer.Exit()

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    prs = fetch_json(f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls?state=closed&base={branch}", headers)

    with open(output_file, 'a') as f:  # Open file for appending
        for pr in prs:
            if pr['merged_at'] is not None:
                pr_number = pr['number']
                pr_details = fetch_json(f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}", headers)
                if pr_details['additions'] + pr_details['deletions'] < max_changes:
                    commits = fetch_json(f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/commits", headers)
                    comments = fetch_json(f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{pr_number}/comments", headers)
                    
                    for commit in commits:
                        commit_sha = commit['sha']
                        diffs = fetch_json(f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{commit_sha}", headers)
                        
                        document = commit['commit']['message']
                        messages = [
                            {"content": diffs['files'][0]['patch'] if diffs['files'] else "No change", "role": "assistant"},
                            *[
                                {"content": comment['body'], "user": comment['user']['login']} for comment in comments
                            ]
                        ]
                        output = ["merged"]
                        
                        entry = {
                            "document": document,
                            "messages": messages,
                            "output": output
                        }
                        f.write(json.dumps(entry) + '\n')  # Write each entry as a single line JSON string

if __name__ == "__main__":
    app()
