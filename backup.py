import json

def get_user_input():
    directories_to_backup = []

    print("Inserisci le directory da backup (inserisci 'fine' per terminare l'inserimento):")
    while True:
        directory = input("Directory: ")
        if directory.lower() == 'fine':
            break
        directories_to_backup.append(directory)

    backup_locations = []
    print("Inserisci le posizioni di backup (inserisci 'fine' per terminare l'inserimento):")
    while True:
        backup_location = input("Posizione di backup: ")
        if backup_location.lower() == 'fine':
            break
        backup_locations.append(backup_location)

    return directories_to_backup, backup_locations

def save_to_json(directories_to_backup, backup_locations):
    config_data = {
        "directories_to_backup": directories_to_backup,
        "backup_locations": backup_locations
    }

    with open('backup_config.json', 'w') as json_file:
        json.dump(config_data, json_file, indent=4)

# Ottieni le directory da backup e le posizioni dall'utente
directories_to_backup, backup_locations = get_user_input()

# Salva le informazioni nel file JSON
save_to_json(directories_to_backup, backup_locations)
