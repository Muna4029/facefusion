#!/usr/bin/env python3

import os
import sys

os.environ['OMP_NUM_THREADS'] = '1'

from facefusion import core

def _remove_existing_output_arg(argv):
    # Look for -o or --output and remove the file if it already exists to
    # prevent ffmpeg from prompting for overwrite (interactive) which can
    # cause non-zero exit in CI environments.
    for i, a in enumerate(argv):
        if a in ('-o', '--output') and i + 1 < len(argv):
            out = argv[i + 1]
            try:
                if os.path.exists(out):
                    os.remove(out)
            except Exception:
                # If removal fails for any reason, ignore and let CLI handle it
                pass
            break

if __name__ == '__main__':
    _remove_existing_output_arg(sys.argv)
    core.cli()
