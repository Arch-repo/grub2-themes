# Anto426 GRUB Theme

GRUB2 theme fork based on [`vinceliuice/grub2-themes`](https://github.com/vinceliuice/grub2-themes), tuned for the Anto426 Hyprland setup.

The default variant is `anto426`: it uses the Anto426 wallpaper set, warm selection assets, and a dedicated GRUB layout. The upstream variants remain available as fallbacks.

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
  -t, --theme                 theme variant(s)          [anto426|tela|vimix|stylish|whitesur]
  -i, --icon                  icon variant(s)           [color|white|whitesur]
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

Original GRUB theme project by [vinceliuice](https://github.com/vinceliuice/grub2-themes). This fork keeps upstream compatibility while adding the Anto426 defaults.
