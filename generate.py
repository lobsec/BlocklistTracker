import requests

urls = {
    "ABUSE.CH BOTNET C2 IOC": [0, "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"],
    "ABUSE.CH BOTNET C2": [0, "https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt"],
    "BLOCKLIST.DE": [0, "https://lists.blocklist.de/lists/all.txt"],
    "SGBOX BAD REPUTATION IP": [0, "https://download.sgbox.it/dnld/feeds/sgbox_badreputation_ip.txt"],
    "SGBOX BOTNET":  [0, "https://download.sgbox.it/dnld/feeds/sgbox_botnet.txt"],
    "TOR EXIT POINT": [0, "https://check.torproject.org/torbulkexitlist"],
    "IPC2s-30day": [1, "https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/IPC2s-30day.csv"],
    "IPC2s": [1, "https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/IPC2s.csv"]

}

ips = []

for site, url in urls.items():
    req = requests.get(url[1])
    if req.status_code == 200:
        for ip in req.text.split("\n"):
            if not ip.replace("\r", "").startswith("#") and (ip.replace("\r", "") not in ips):
                if url[0] == 0:
                    ips.append(ip.replace("\r", ""))
                else:
                    ips.append(ip.replace("\r", "").split(",")[0])

with open("out.txt", "w") as f_out:
    for ip in ips:
        f_out.write("%s\n" % ip)
