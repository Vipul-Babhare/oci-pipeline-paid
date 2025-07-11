import os
import datetime
import subprocess

# Step 1: Create a text file with timestamp
timestamp = datetime.datetime.utcnow().isoformat()
with open("output.txt", "w") as f:
    f.write(f"✅ This file was auto-generated on the VM at {timestamp} UTC\n")

# Step 2: Setup Git
repo_url = os.environ["REPO_URL"]
gh_pat = os.environ["GH_PAT"]
full_url = repo_url.replace("https://", f"https://{gh_pat}@")

subprocess.run("git config --global user.name 'oci-vm'", shell=True)
subprocess.run("git config --global user.email 'oci@vm.com'", shell=True)

# Step 3: Clone, commit, and push
subprocess.run(f"git clone {full_url}", shell=True)
repo_name = repo_url.split("/")[-1].replace(".git", "")
os.chdir(repo_name)
subprocess.run("mv ../output.txt .", shell=True)
subprocess.run("git add output.txt", shell=True)
subprocess.run("git commit -m '✅ Auto output from OCI VM'", shell=True)
subprocess.run("git push", shell=True)
