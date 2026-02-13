# Ghostty Terminal Config

Chezmoi-managed Ghostty configuration for Claude Code workflows.

## Setup

```bash
# Install chezmoi if not present
sh -c "$(curl -fsLS get.chezmoi.io)"

# Add the template
chezmoi add --template ~/.config/ghostty/config

# Or copy directly
cp docs/config/ghostty/config.tmpl ~/.config/ghostty/config
```

## Chezmoi Variables

Set in `~/.config/chezmoi/chezmoi.toml`:

```toml
[data]
font_size = 14
theme = "catppuccin-mocha"
```

## Keybinding Reference

| Keybinding | Action |
|------------|--------|
| `Ctrl+Shift+H` | Go to left split |
| `Ctrl+Shift+L` | Go to right split |
| `Ctrl+Shift+J` | Go to bottom split |
| `Ctrl+Shift+K` | Go to top split |
| `Ctrl+Shift+N` | New split (right) |
| `Ctrl+Shift+Enter` | New split (down) |
| `Ctrl+Shift+W` | Close split |

## Recommended Layout

```
┌────────────────────────────┬──────────────────┐
│                            │                  │
│   Claude Code (60%)        │  Editor (40%)    │
│                            │                  │
│                            │                  │
├────────────────────────────┴──────────────────┤
│           Terminal (30% height)                │
└───────────────────────────────────────────────┘
```

1. Open Ghostty
2. `Ctrl+Shift+N` — split right for editor
3. `Ctrl+Shift+Enter` — split down for terminal
4. Run `claude` in the main (left) pane

## WSL2 Notes

- Ghostty runs natively on Windows, connects to WSL2 via shell integration
- Set `shell-integration = zsh` (or `bash` if using bash in WSL)
- Ghostty cannot render HTML natively — use Kitty graphics protocol for images
- For rich interactive views, open `ARCHITECTURE.html` in browser
