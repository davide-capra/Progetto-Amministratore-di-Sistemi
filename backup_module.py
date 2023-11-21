import subprocess
import json

def backup_files(directories_to_backup, backup_locations):
    for directory in directories_to_backup:
        for location in backup_locations:
            rsync_command = f"rsync -av --delete --update {directory}/ {location}/{directory.split('/')[-1]}"
            subprocess.run(rsync_command, shell=True)

# Leggi i dati dal file JSON
with open('backup_config.json', 'r') as json_file:
    data = json.load(json_file)

# Ottieni le informazioni necessarie per il backup
directories_to_backup = data["directories_to_backup"]
backup_locations = data["backup_locations"]

# Esegui il backup
backup_files(directories_to_backup, backup_locations)
