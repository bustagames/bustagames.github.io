# Welcome to Busta Games

Busta Games Home Page

# Setup

This site is built with Jekyll and is pinned to the GitHub Pages dependency set.

Use Ruby `3.3.4` locally. The repository includes `.ruby-version` so version managers such as `rbenv`, `asdf`, or `mise` can pick it up automatically.

On macOS, avoid the system Ruby. Install a user-managed Ruby and Bundler, then install gems from the lockfile:

```sh
bundle install
```

# Commands

## Serve locally
```sh
bundle exec jekyll serve
```

## Update Ruby dependencies
```sh
bundle update
```

## Just Build, not serve
```sh
bundle exec jekyll build
```

## Serve with drafts
Enable draft posts in order to preview them
```sh
bundle exec jekyll serve --drafts
```

## Python image conversion helper

If you want to convert images to `.webp`, use the Python helper:

```sh
python image-converter.py path/to/image.png
```

## Check Gem versions
https://pages.github.com/versions/
