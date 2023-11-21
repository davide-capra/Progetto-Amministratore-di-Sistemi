import json

# Dati da scrivere nel file JSON
data = {
    "directories_to_backup": [
        "/percorso/directory1",
        "/percorso/directory2"
    ],
    "backup_on_pc": True,
    "backup_on_usb": True,
    "backup_location_pc": "/percorso/backup/pc",
    "backup_location_usb": "/percorso/backup/usb"
}

# Scrivi i dati nel file JSON
with open('backup_config.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)