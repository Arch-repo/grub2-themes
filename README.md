<div align="center">

# 🗂️ anto426 grub2-themes

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=28&duration=3000&pause=1000&color=8cb8e4&center=true&vCenter=true&width=435&lines=Custom+GRUB+Theme;Aesthetic+Bootloader;Dynamic+Colors+Support)](https://git.io/typing-svg)

A highly customized and fully responsive **GRUB2 Bootloader** theme tuned for the `anto426` Hyprland ecosystem.

</div>

---

## ✨ Features

The `anto426` theme is the exclusive variant exposed by this installer. It is designed to look extremely premium and integrates seamlessly with the dynamic color theme engine.

- 🎨 **Dynamic Colors**: Sourced automatically from your active desktop wallpaper.
- 📐 **Responsive Layouts**: Pre-configured screen assets and customized layouts for **1080p**, **2k**, **4k**, **ultrawide**, and **ultrawide2k** displays.
- 🧩 **Branding & Assets**: Features custom icons, elegant selection pixmaps, stylized terminal widgets, and the custom branding `info.png` block.

---

## 🚀 Quick Install

To install the theme with the default 1080p layout and color icons:

```bash
sudo bash ./install-anto426.sh
```

---

## ⚙️ Custom Configurations

You can customize the installation using environment variables before running the script:

### 📺 Change Screen Preset
Override the display configuration for high-resolution monitors:
```bash
sudo ANTO426_GRUB_SCREEN=2k bash ./install-anto426.sh
```

### 📏 Use Custom Resolution
If your native display is not listed, specify a custom resolution directly (automatically resizes and formats assets via ImageMagick):
```bash
sudo ANTO426_GRUB_RESOLUTION=1600x900 bash ./install-anto426.sh
```

### 💾 Install to Boot Directory
To install directly into `/boot/grub/themes` or `/boot/grub2/themes` (useful for EFI installations):
```bash
sudo ANTO426_GRUB_BOOT=1 bash ./install-anto426.sh
```

---

## 🛠️ Advanced Usage

For full control, run the core installer script directly:

```bash
sudo ./install.sh [OPTIONS...]
```

| Option | Argument | Description |
|--------|----------|-------------|
| `-t, --theme` | `anto426` | Theme variant (default is `anto426`) |
| `-i, --icon` | `color` | Icon variant (default is `color`) |
| `-s, --screen` | `1080p\|2k\|4k\|ultrawide\|ultrawide2k` | Screen display variant (default is `1080p`) |
| `-c, --custom-resolution` | `WIDTHxHEIGHT` | Custom display resolution (e.g. `1600x900`) |
| `-r, --remove` | `anto426` | Remove installed theme |
| `-b, --boot` | *(None)* | Install theme into `/boot/grub` or `/boot/grub2` |
| `-g, --generate` | `/path/to/dir` | Generate theme into chosen directory |

### Examples
```bash
# Install for 2K screen
sudo ./install.sh -t anto426 -s 2k

# Install with custom resolution
sudo ./install.sh -t anto426 -c 3440x1440

# Remove the theme
sudo ./install.sh -r -t anto426
```

---

## 🤝 Integration

`Arch-Hyprland` clones this repository during system installation and runs `install-anto426.sh`. 

The dotfiles wallpaper engine (`wallpaper_effects.sh`) then takes over to dynamically modify `/usr/share/grub/themes/anto426/background.jpg`, `theme.txt`, and selection pixmaps, making your boot menu follow the active wallpaper palette perfectly!

---

## 🎨 Credits

Original GRUB theme project created by [vinceliuice/grub2-themes](https://github.com/vinceliuice/grub2-themes). This fork keeps the installer framework but specializes exclusively in exposing and adapting the premium `anto426` Riva controls theme.

---

<div align="center">
  <i>Configured by anto426</i>
</div>
