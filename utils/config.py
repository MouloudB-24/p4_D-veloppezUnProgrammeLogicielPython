from pathlib import Path

save_folder = Path(__file__).parent.parent / "data"

# Vérifier si le dossier existe, sinon le créer
if not save_folder.exists():
    save_folder.mkdir(parents=True)
