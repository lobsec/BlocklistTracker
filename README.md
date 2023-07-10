# Blocklist feed

## Abstract 
The purpose of this tracker is to collect the list of IP addresses considered malicious from public feeds (without duplicated).
In this moment the feeds are:
* [ABUSE.CH BOTNET C2 IOC](https://feodotracker.abuse.ch/downloads/ipblocklist.txt)
* [ABUSE.CH BOTNET C2](https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt)
* [BLOCKLIST.DE](https://lists.blocklist.de/lists/all.txt)
* [SGBOX BAD REPUTATION IP](https://download.sgbox.it/dnld/feeds/sgbox_badreputation_ip.txt)
* [SGBOX BOTNET](https://download.sgbox.it/dnld/feeds/sgbox_botnet.txt)
* [TOR EXIT POINT](https://check.torproject.org/torbulkexitlist)
* [CENSYS IPC2s-30days](https://github.com/drb-ra/C2IntelFeeds/blob/master/feeds/IPC2s-30day.csv)
* [CENSYS IPC2s](https://github.com/drb-ra/C2IntelFeeds/blob/master/feeds/IPC2s.csv)

## Files
* ```generate.py``` generates a text file (```out.txt```) containing all the ip addresses separated by newlines.