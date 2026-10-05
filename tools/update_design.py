#!/usr/bin/env python3
"""Regenerate GRUB assets using the canonical dotfiles design renderer."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import shutil
import tempfile

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--dotfiles',type=Path,required=True)
options=parser.parse_args()
source=options.dotfiles.resolve()/'support/compat/boot_render.py'
spec=importlib.util.spec_from_file_location('boot_render',source)
renderer=importlib.util.module_from_spec(spec);spec.loader.exec_module(renderer)
resolutions={'1080p':'1920x1080','2k':'2560x1440','4k':'3840x2160','ultrawide':'2560x1080','ultrawide2k':'3440x1440'}
with tempfile.TemporaryDirectory(prefix='anto-grub-design-') as temporary:
    work=Path(temporary)
    for preset,size in resolutions.items():
        wallpaper=ROOT/f'backgrounds/{preset}/background-anto426.jpg'
        renderer.render(str(work),str(wallpaper),size,'#141820','#edf1f8','#b4c8ff')
        shutil.copyfile(work/'grub-theme.txt',ROOT/f'config/theme-anto426-{preset}.txt')
        # Background originals are retained; bake the translucent panel only
        # at installation/runtime, using the same geometry as these templates.
        if preset in ('1080p','2k','4k'):
            destination=ROOT/f'assets/assets-select-anto426/select-{preset}'
            for asset in work.glob('select_*.png'):shutil.copyfile(asset,destination/asset.name)
receipt={'source_repository':'https://github.com/Arch-repo/dotfiles','tokens_sha256':hashlib.sha256((options.dotfiles/'design/tokens.json').read_bytes()).hexdigest(),'renderer_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'regenerate':'python3 tools/update_design.py --dotfiles /path/to/dotfiles'}
(ROOT/'design-source.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('Five layouts and nine-slice selection assets regenerated from dotfiles.')
