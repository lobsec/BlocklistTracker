import requests

urls = {
    "ABUSE.CH BOTNET C2 IOC": "https://feodotracker.abuse.ch/downloads/ipblocklist.txt",
    "ABUSE.CH BOTNET C2": "https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt",
    "BLOCKLIST.DE": "https://lists.blocklist.de/lists/all.txt",
    "SGBOX BAD REPUTATION IP": "https://download.sgbox.it/dnld/feeds/sgbox_badreputation_ip.txt",
    "SGBOX BOTNET": "https://download.sgbox.it/dnld/feeds/sgbox_botnet.txt",
    "TOR EXIT POINT": "https://check.torproject.org/torbulkexitlist"
}
ips = []

for site, url in urls.items():
    req = requests.get(url)
    if req.status_code == 200:
        for ip in req.text.split("\n"):
            if not ip.replace("\r", "").startswith("#") and (ip.replace("\r", "") not in ips):
                ips.append(ip.replace("\r", ""))

with open("out.txt", "w") as f_out:
    for ip in ips:
        f_out.write("%s\n" % ip)
