# Anto426 GRUB Theme

Single active GRUB2 theme tuned for the Anto426 Hyprland setup.

`anto426` is the only theme exposed by the installer. It uses the Riva/Anto426 palette, a centered control-style boot menu, color icons, and dedicated layouts for 1080p, 2k, 4k, and ultrawide displays.

## Install

```bash
sudo bash ./install-anto426.sh
```

The wrapper installs the `anto426` variant with color icons on a 1080p layout. You can override the screen preset:

```bash
sudo ANTO426_GRUB_SCREEN=2k bash ./install-anto426.sh
```

Or use a custom resolution:

```bash
sudo ANTO426_GRUB_RESOLUTION=1600x900 bash ./install-anto426.sh
```

To install directly into `/boot/grub/themes` or `/boot/grub2/themes`, set:

```bash
sudo ANTO426_GRUB_BOOT=1 bash ./install-anto426.sh
```

## Advanced Usage

```bash
sudo ./install.sh [OPTIONS...]
```

Options:

```text
  -t, --theme                 theme variant             [anto426]
  -i, --icon                  icon variant              [color]
  -s, --screen                screen display variant(s) [1080p|2k|4k|ultrawide|ultrawide2k]
  -c, --custom-resolution     set custom resolution     (e.g. 1600x900)
  -r, --remove                remove theme
  -b, --boot                  install theme into /boot/grub or /boot/grub2
  -g, --generate              generate theme into a chosen directory
```

Examples:

```bash
sudo ./install.sh -t anto426 -s 2k
sudo ./install.sh -t anto426 -c 3440x1440
sudo ./install.sh -r -t anto426
```

## Integration

`Arch-Hyprland` clones this repository during setup and runs `install-anto426.sh`. The dotfiles wallpaper engine can later update `/usr/share/grub/themes/anto426/background.jpg`, `theme.txt`, and selection pixmaps so the boot menu follows the active wallpaper palette.

## Credits

Original GRUB theme project by [vinceliuice](https://github.com/vinceliuice/grub2-themes). This fork keeps the installer shape but exposes only the Anto426/Riva theme.
