
import subprocess
import sys

packages = [
    "discord.py",
    "colorama",
    "requests"
]

for package in packages:
    print(f"{package}...")
    result = subprocess.run([
        sys.executable, "-m", "pip", "install", "--upgrade", package
    ])

    if result.returncode != 0:
        print(f"Erreur pendant l'installation de {package}.")

print("\nInstallation terminée.")
input("Appuie sur Entrée pour fermer...")
