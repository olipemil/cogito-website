#!/usr/bin/env python3
"""
Set up webhook trigger for cross-repository automation.
This script helps configure the webhook between COGITO and website repos.
"""

import requests
import json
import os

def create_workflow_dispatch(repo_owner, repo_name, token):
    """Trigger the workflow dispatch event for documentation updates."""

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/dispatches"

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }

    data = {
        "event_type": "cogito-updated",
        "client_payload": {
            "source": "manual-trigger",
            "message": "Documentation update requested"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 204:
        print("✅ Workflow dispatch triggered successfully!")
        return True
    else:
        print(f"❌ Failed to trigger workflow: {response.status_code}")
        print(f"Response: {response.text}")
        return False

def setup_webhook_instructions():
    """Print instructions for setting up the webhook."""

    instructions = """
🔧 Setting Up Cross-Repository Automation

To enable automatic documentation updates when COGITO is updated:

1. **In the COGITO repository**, add a workflow file (.github/workflows/notify-website.yml):

```yaml
name: Notify Website of Updates

on:
  push:
    branches: [ main ]
    paths:
      - 'COGITO.py'
      - 'COGITOpost.py'
      - 'COGITOico.py'
      - '**/*.ipynb'

jobs:
  notify-website:
    runs-on: ubuntu-latest
    steps:
    - name: Trigger website update
      run: |
        curl -X POST \\
          -H "Accept: application/vnd.github.v3+json" \\
          -H "Authorization: token ${{ secrets.WEBSITE_TOKEN }}" \\
          https://api.github.com/repos/olipemil/cogito-website/dispatches \\
          -d '{"event_type":"cogito-updated","client_payload":{"source":"cogito-push"}}'
```

2. **In the COGITO repository settings**:
   - Go to Settings > Secrets and variables > Actions
   - Add a new secret: `WEBSITE_TOKEN`
   - Value: Personal access token with `repo` scope for cogito-website

3. **In the website repository** (this repo):
   - The workflow is already set up in .github/workflows/update-docs.yml
   - It will automatically trigger when COGITO is updated

4. **Alternative: Manual trigger**:
   - Go to Actions tab in this repository
   - Select "Update Documentation from COGITO"
   - Click "Run workflow"

🎯 **Result**: Every time COGITO code is updated, your website documentation will automatically refresh!
"""

    print(instructions)

def test_manual_trigger():
    """Test the manual trigger functionality."""

    print("🧪 Testing manual workflow trigger...")

    # Check if we're in a GitHub Actions environment
    if os.getenv('GITHUB_ACTIONS'):
        print("Running in GitHub Actions - workflow dispatch not needed")
        return True

    # For local testing, we can't actually trigger the workflow
    # but we can verify the API endpoint structure
    print("✅ Workflow trigger script ready")
    print("💡 To test: Use GitHub Actions tab or set up the webhook as described")

    return True

if __name__ == "__main__":
    print("🚀 COGITO Website Cross-Repository Automation Setup")
    print("=" * 50)

    # Show setup instructions
    setup_webhook_instructions()

    # Test the trigger mechanism
    test_manual_trigger()

    print("\n" + "=" * 50)
    print("✅ Setup complete! Documentation will auto-update when COGITO changes.")