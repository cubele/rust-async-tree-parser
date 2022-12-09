# Rust Async Tree Parser

An attempt of dumping the async exectuion tree of a Rust program only using debuginfo. The results aren't 100% accurate.

## Usage

install [pyvis](https://pyvis.readthedocs.io/en/latest/install.html) and [ddbug](https://github.com/gimli-rs/ddbug) and start from `draw.ipynb`.

## Method

A pretty stupid one. It simply parses the text output of ddbug and finds the async-related structs, adding the `__awaitee` field as childrens. This could obviously be done by directly parsing the debuginfo, but I'm too lazy to do that.
