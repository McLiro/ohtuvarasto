# ohtuvarasto

[![GHA workflow badge](https://github.com/McLiro/ohtuvarasto/actions/workflows/main.yml/badge.svg)](https://github.com/McLiro/ohtuvarasto/actions)

[![codecov](https://codecov.io/github/McLiro/ohtuvarasto/graph/badge.svg?token=5X0HXUGDPJ)](https://codecov.io/github/McLiro/ohtuvarasto)

## Web interface

Run the warehouse web interface with:

```sh
PYTHONPATH=src uv run flask --app web run
```

Create storages by entering a unique name and size. Each storage has controls
to add and remove items, and its current balance is displayed on the page.
