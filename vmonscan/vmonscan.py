"""module to do scanning, calling external program clamwin"""
import os
import sys
import subprocess

CLAM_SCAN_BIN = 'clamscan.exe'
CLAM_SCAN_PATH = os.path.join(os.path.dirname(__file__), 'bin',
                    CLAM_SCAN_BIN)

FRESH_CLAM_BIN = 'freshclam.exe'
FRESH_CLAM_PATH = os.path.join(os.path.dirname(__file__), 'bin',
                    FRESH_CLAM_BIN)


def execute_cmd(cmd, cwd=None):
    try:
        proc = subprocess.Popen(cmd.split(),
                stdout=subprocess.PIPE,
                cwd=cwd)
        while True:
            out = proc.stdout.readline()
            if out == '' and proc.poll() != None:
                break
            if out != '':
                yield out
                sys.stdout.flush()
    except OSError as e:
        print e
        yield ''


def scan_memory():
    for line in execute_cmd('%s --memory -d db' % CLAM_SCAN_PATH):
        print line


def update_virus_db():
    for line in execute_cmd('%s --datadir=db' % FRESH_CLAM_PATH):
        print line

if __name__ == '__main__':
    scan_memory()
