

shutter-encoder-flatpak
=======================

This repo allows you to package Shutter Encoder as a Flatpak for use
on Linux Flatpak based systems, especially e.g. Fedora Silverblue where
there aren't easier installation options.

Usage
-----

1. `git clone` this repo
2. Build your package, and export to a distributable single file installer:
```
flatpak-builder --force-clean --repo=.repo .build-dir org.paulpacifico.ShutterEncoder.yaml
flatpak build-bundle .repo shutter-encoder.flatpak org.paulpacifico.ShutterEncoder
flatpak install shutter-encoder.flatpak
```

3. Enjoy.
