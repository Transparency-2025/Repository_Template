import os
import json
import requests
from datetime import datetime

# --- CONFIGURATION ---
GITHUB_ORG = "Transparency-2025"
REPOS = [
    "PROJECT_SILENT_SPACE",
    "The-Freedom-Card-Program",
    "PROJECT_TRANSPARENCY_2025",
    "Ireland-Embassies-and-Consulates",
    "Research-Infrared-Light-Infrared-Therapy",
    "PUBLIC-RECORD",
]
SCORE_FILE_PATH = "DATA/SCORE.json"

# --- GITHUB API HELPER ---
def get_score_data(repo_name):
    """Fetches the content of DATA/SCORE.json from a remote repository."""
    # Using the GitHub Content API to fetch the file content
    url = f"https://api.github.com/repos/{GITHUB_ORG}/{repo_name}/contents/{SCORE_FILE_PATH}"
    headers = {
        "Authorization": f"token {os.environ.get('GH_TOKEN')}",
        "Accept": "application/vnd.github.v3.raw" # Get raw file content
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes
        
        # The content is raw JSON due to the header 'application/vnd.github.v3.raw'
        score_data = json.loads(response.text)
        
        # Also fetch the last commit date for the repo
        repo_info_url = f"https://api.github.com/repos/{GITHUB_ORG}/{repo_name}"
        repo_info = requests.get(repo_info_url, headers={"Authorization": f"token {os.environ.get('GH_TOKEN')}"}).json()
        
        last_updated = datetime.strptime(repo_info.get("pushed_at"), '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
        
        return {
            "name": repo_name,
            "description": repo_info.get("description", "No description available."),
            "score_grade": score_data.get("score_grade", "N/A"),
            "score_value": score_data.get("score_value", "N/A"),
            "last_updated": last_updated
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Warning: Could not fetch score for {repo_name}. Using N/A. Error: {e}")
        return {
            "name": repo_name,
            "description": "Error fetching data.",
            "score_grade": "N/A",
            "score_value": "N/A",
            "last_updated": "Unknown"
        }

# --- TABLE GENERATION ---
def generate_table(data_list):
    """Creates the Markdown table string from the fetched data."""
    table_lines = [
        "| Project Name | Focus / Description | Assessment Score | Last Updated |",
        "| :--- | :--- | :--- | :--- |"
    ]
    
    for item in data_list:
        # Use description from the GitHub API, or fall back to score_data if needed
        description = item['description'] if item['description'] else f"Score: {item['score_grade']}"
        
        row = (
            f"| **[{item['name']}](https://github.com/{GITHUB_ORG}/{item['name']})** "
            f"| {description} "
            f"| **{item['score_value']}** ({item['score_grade']}) "
            f"| {item['last_updated']} |"
        )
        table_lines.append(row)
        
    return "\n".join(table_lines)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("Starting dynamic README generation...")
    
    # 1. Fetch data for all repositories
    all_repo_data = [get_score_data(repo) for repo in REPOS]
    
    # 2. Generate the dynamic table
    dynamic_table = generate_table(all_repo_data)
    
    # 3. Read the static README template
    with open("README_TEMPLATE.md", "r") as f:
        template = f.read()
        
    # 4. Insert the dynamic table into the template (using a placeholder)
    new_readme_content = template.replace(
        "", 
        dynamic_table
    )
    
    # 5. Commit the new content to README.md
    with open("README.md", "w") as f:
        f.write(new_readme_content)
        
    print("README.md successfully updated with dynamic scores.")
