import os
import subprocess


def main():
    process = subprocess.run(['pip', 'install', 'PySide6'])
    print()
    print('[+] Installation Completed')
    print('[+] You are ready to Roll')
    print('[+] Run main.py')
    print('[+] Closing...')


if __name__ == '__main__':
    main()
