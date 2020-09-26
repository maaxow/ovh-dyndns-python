# Informations

This script auto update your public IP to your ovh dns A domain.

# Pre requists

configure your ovh.conf with API keys

# RUN
```
python3 update-ovh-dns.py <domain>
```

# CRON
You can add this script in crontab like this :
```
crontab -e
*/30 * * * * python3 /home/ovh-dyndns-python/update-ovh-dns.py <domain>
```
