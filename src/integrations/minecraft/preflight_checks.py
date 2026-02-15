import subprocess


def system_has_java():
    try:
        result = subprocess.run(
            ["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return result.returncode == 0
    except FileNotFoundError:
        print("Java executable not found.")
        return False
