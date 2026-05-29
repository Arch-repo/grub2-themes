<p align="center">
  <img 
    src="https://wsrv.nl/?url=avatars.githubusercontent.com/u/87477585?v=5&w=300&h=300&mask=circle&fit=cover" 
    width="150"
  />
</p>

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=24&duration=3000&pause=1000&color=8cb8e4&center=true&vCenter=true&width=500&height=80&lines=Custom+GRUB+Theme;Aesthetic+Bootloader;Dynamic+Color+Boot" alt="Typing SVG" /></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/divider.gif" width="440" height="40" />
</p>

# <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/icon.gif" width="60px" /> Features;

```sh
root@anto426: ~/grub2-themes (main⚡)$ cat specs.txt

A highly customized and responsive bootloader screen specializing in the premium 'anto426' layout.

- 🎨 Dynamic Colors: Rewritten on desktop wallpaper change to synchronize boot colors with home aesthetics.
- 📐 Screen Presets: High quality visual layouts for 1080p, 2K, 4K, Ultrawide, and Ultrawide2K displays.
- 🧩 Elegant Icons: Premium custom vector icon sets, elegant selectors, and clean branding boxes.
```

<p align="center">
  <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/divider.gif" width="440" height="40" />
</p>

# <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/icon2.gif" width="70px" /> Quick Install;

```sh
root@anto426: ~/grub2-themes (main⚡)$ sudo ./install-anto426.sh

Deploy the theme with default 1080p layout and full color icons instantly:
```

```bash
sudo bash ./install-anto426.sh
```

---

### ⚙️ Environmental Customization

You can control assets compilation and installation paths via variables:

- **High DPI Screen Preset**:
  ```bash
  sudo ANTO426_GRUB_SCREEN=2k bash ./install-anto426.sh
  ```
- **Custom Display Resolutions**:
  ```bash
  sudo ANTO426_GRUB_RESOLUTION=1600x900 bash ./install-anto426.sh
  ```
- **Direct `/boot` Folder Installation**:
  ```bash
  sudo ANTO426_GRUB_BOOT=1 bash ./install-anto426.sh
  ```

<p align="center">
  <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/divider.gif" width="440" height="40" />
</p>

# <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/icon3.gif" width="70px" /> Advanced Options;

```sh
root@anto426: ~/grub2-themes (main⚡)$ ./install.sh --help
```

| Command Options | Values | Rationale |
|---|---|---|
| `-t, --theme` | `anto426` | Select custom profile theme style (locked default). |
| `-i, --icon` | `color` | Icon style asset packages. |
| `-s, --screen` | `1080p\|2k\|4k\|ultrawide\|ultrawide2k` | Screen display preset target. |
| `-c, --custom-resolution` | `WIDTHxHEIGHT` | Forces ImageMagick assets resizing to resolution. |
| `-r, --remove` | `anto426` | Removes boot theme modifications and restores backups. |
| `-b, --boot` | *(None)* | Installs directly into EFI system directory `/boot/grub`. |

<p align="center">
  <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/divider.gif" width="440" height="40" />
</p>

# <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/icon4.gif" width="70px" /> Integration & Credits;

```sh
root@anto426: ~/grub2-themes (main⚡)$ neofetch --view origin

- Upstream Project: vinceliuice/grub2-themes installer logic base.
- Dynamic color integration is handled by the dotfiles colors engine during wallpaper edits:
  - Generates '/usr/share/grub/themes/anto426/background.jpg'
  - Alters 'theme.txt' fonts, color selectors, and layouts to match.
```

<p align="center">
  <img src="https://raw.githubusercontent.com/Anto426/Anto426/main/asset/divider.gif" width="440" height="40" />
</p>

<div align="center">
  <i>Configured by anto426</i>
</div>
