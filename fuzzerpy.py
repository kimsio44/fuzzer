import os
import subprocess
import sys
import urllib.request
import zipfile
import shutil
import ctypes

# Vérifie si admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.user32.MessageBoxW(0, "Lance ce programme en administrateur !", "Erreur", 0x10)
    sys.exit()

# Vérifie si Python est installé
def is_python_installed():
    try:
        output = subprocess.check_output(["python", "--version"])
        return True
    except:
        return False

# Télécharge Python si besoin
def install_python():
    print("Téléchargement de Python...")
    url = "https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe"
    python_installer = "python_installer.exe"
    urllib.request.urlretrieve(url, python_installer)
    subprocess.run([python_installer, "/quiet", "InstallAllUsers=1", "PrependPath=1"])
    os.remove(python_installer)

# Installe les requirements
def install_requirements():
    try:
        import pip
    except ImportError:
        print("pip manquant, tentative de réparation...")
        urllib.request.urlretrieve("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
        subprocess.run(["python", "get-pip.py"])
        os.remove("get-pip.py")

    requirements = [
        "requests",
        "matplotlib",
        "pillow",
        "tk",
        "minecraft==1.16.5",  # ou autre version selon ton script
    ]
    for package in requirements:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package])

# Télécharge et exécute le vrai fuzzer
def download_and_run_script():
    script_url = "https://example.com/fuzzer.py"  # 🔁 Remplace par ton URL GitHub brut ou raw
    local_script = "fuzzer_main.py"
    urllib.request.urlretrieve(script_url, local_script)
    subprocess.Popen([sys.executable, local_script], creationflags=subprocess.CREATE_NO_WINDOW)

# ------------------ MAIN ---------------------
if not is_python_installed():
    install_python()

install_requirements()
download_and_run_script()
