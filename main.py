import time, requests, json

def get_downloads(repo):
    releases = requests.get(
        f"https://api.github.com/repos/{repo}/releases"
    ).json()
    count = 0
    for release in releases:
        for asset in release["assets"]:
            count += asset["download_count"]

    return count

data = json.load(open("data.json"))

data[time.time()] = {
    "poly": get_downloads("PolyMC/PolyMC"),
    "prism": get_downloads("PrismLauncher/PrismLauncher")
}

with open("data.json", "w") as f:
    f.write(json.dumps(data))
