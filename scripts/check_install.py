#!/usr/bin/env python3
"""
Fabric Installation Helper Script

Cross-platform script to check and install Fabric CLI.
Works with: macOS, Linux, Windows (PowerShell).
Compatible with: opencode, Claude Code, Cursor, and other AI coding assistants.
"""

import subprocess
import sys
import os
import shutil


def run_command(cmd, shell=False):
    try:
        result = subprocess.run(
            cmd if shell else cmd, shell=shell, capture_output=True, text=True
        )
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return False, "", str(e)


def check_go_installed():
    return shutil.which("go") is not None


def check_fabric_installed():
    return shutil.which("fabric") is not None


def get_fabric_version():
    success, stdout, stderr = run_command(["fabric", "--version"])
    if success:
        return stdout
    return None


def install_fabric():
    print("Installing Fabric CLI...")
    print()
    print("Choose installation method:")
    print("1. Go (recommended for most users)")
    print("2. One-liner install script (Unix/Linux/macOS)")
    print("3. PowerShell installer (Windows)")
    print("4. Homebrew (macOS)")
    print("5. Winget (Windows)")
    print("6. Docker")
    print()

    # Try Go installation by default
    if check_go_installed():
        print("Installing via Go (recommended)...")
        success, _, stderr = run_command(
            ["go", "install", "github.com/danielmiessler/fabric/cmd/fabric@latest"]
        )
        if success:
            print("✓ Fabric installed successfully!")
            print()
            print("IMPORTANT: Add Go bin to your PATH if not already present:")
            print("  export PATH=$PATH:$(go env GOPATH)/bin")
            print()
            print("Run 'fabric --setup' to configure Fabric.")
            return True
        else:
            print(f"✗ Go install failed: {stderr}")
            return False
    else:
        print("Go is not installed.")
        print()
        print("To install Fabric without Go, run one of these commands:")
        print()
        print("Unix/Linux/macOS:")
        print(
            "  curl -fsSL https://raw.githubusercontent.com/danielmiessler/fabric/main/scripts/installer/install.sh | bash"
        )
        print()
        print("Windows PowerShell:")
        print(
            "  iwr -useb https://raw.githubusercontent.com/danielmiessler/fabric/main/scripts/installer/install.ps1 | iex"
        )
        print()
        print(
            "For more options: https://github.com/danielmiessler/Fabric?tab=readme-ov-file#installation"
        )
        return False


def main():
    print("=" * 60)
    print("Fabric CLI Installation Checker")
    print("=" * 60)
    print()

    # Check if Go is installed
    if not check_go_installed():
        print("⚠ Go is not installed. Required for Go-based installation.")
        print()

    # Check if Fabric is installed
    if check_fabric_installed():
        version = get_fabric_version()
        print(f"✓ Fabric is installed: {version}")
        print()
        print("Run 'fabric --help' for usage information.")
        print("Run 'fabric --listpatterns' to see available patterns.")
        print("Run 'fabric --listvendors' to see supported AI providers.")
        return 0
    else:
        print("✗ Fabric is NOT installed.")
        print()
        return install_fabric()


if __name__ == "__main__":
    sys.exit(main())
