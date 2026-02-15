from ..preflight_checks import system_has_java
import subprocess

def setup_java():
    if system_has_java():
        print("Java is already installed.")
        return

    print("Java is not installed. Installing OpenJDK 25...")
    
    try:
        subprocess.run(
            ["sudo", "apt", "update"],
            check=True
        )

        subprocess.run(
            ["sudo", "apt", "install", "-y", "openjdk-25-jdk"],
            check=True
        )

        print("Java installation complete!")

        
        result = subprocess.run(["java", "-version"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error installing Java: {e}")
        exit(1)


def setup_linux_environment():
    print("Setting up Linux environment for Minecraft server...")
    setup_java()
    print("Environment setup complete!")
