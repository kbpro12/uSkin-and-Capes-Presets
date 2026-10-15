# uSkin and Capes - Community Presets

Everything in `presets/` is downloaded automatically by every player of the uSkin and Capes mod
(Presets screen -> Refresh Presets).

## Add your preset
1. Fork this repo.
2. Put your skin in `presets/skins/yourname.png` (64x64 or 64x32) and/or your cape in `presets/capes/yourname.png`
   (64x32; animated = vertical sheet, 64 wide, 32 tall per frame).
3. Add an entry to `presets/index.json` (copy an existing one). `id` = lowercase letters, digits, `_` `-` only.
4. Run `python tools/update_hashes.py`.
5. Open a Pull Request.

To update a preset later: change the files and raise `version` by 1.
