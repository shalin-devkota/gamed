import os
import subprocess
import urllib.request
import tempfile
from ..preflight_checks import system_has_java


def setup_java():
    if system_has_java():
        print("Java is already installed.")
        return
    print("Java is not installed. Downloading and installing Java...")
    java_url = "https://download.oracle.com/java/25/latest/jdk-25_windows-x64_bin.msi"

    # Temporary download path
    temp_dir = tempfile.gettempdir()
    java_installer_path = os.path.join(temp_dir, "OpenJDK17.msi")

    print(f"Downloading Java from {java_url}...")
    urllib.request.urlretrieve(java_url, java_installer_path)
    print(f"Downloaded to {java_installer_path}")

    # Install Java silently
    print("Installing Java...")
    subprocess.run(
        ["msiexec", "/i", java_installer_path, "/qn", "/norestart"],
        check=True,
    )

    print("Java installation complete!")

    result = subprocess.run(["java", "-version"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)


def setup_windows_envrionment():
    print("Setting up Windows environment for Minecraft server...")
    setup_java()
