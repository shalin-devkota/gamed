import os
import subprocess
import urllib.request
import tempfile


def setup_windows_envrionment():
    print("Setting up windows environment for Minecraft server...")
    java_url = "https://github.com/adoptium/temurin17-binaries/releases/latest/download/OpenJDK17U-jdk_x64_windows_hotspot.msi"

    # Temporary download path
    temp_dir = tempfile.gettempdir()
    java_installer_path = os.path.join(temp_dir, "OpenJDK17.msi")

    print(f"Downloading Java from {java_url}...")
    urllib.request.urlretrieve(java_url, java_installer_path)
    print(f"Downloaded to {java_installer_path}")

    # Install Java silently
    print("Installing Java...")
    subprocess.run(
        ["msiexec", "/i", java_installer_path, "/qn", "/norestart"], check=True
    )

    print("Java installation complete!")

    # Optional: verify Java
    result = subprocess.run(["java", "-version"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
