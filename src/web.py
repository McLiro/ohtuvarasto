import math

from flask import (
    Blueprint,
    Flask,
    abort,
    current_app,
    redirect,
    render_template,
    request,
    url_for,
)

from varasto import Varasto

warehouse = Blueprint("warehouse", __name__)


def _render_storages(error=None, status=200):
    return (
        render_template(
            "index.html",
            storages=current_app.extensions["storages"],
            error=error,
        ),
        status,
    )


def _parse_amount(value, minimum):
    try:
        amount = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(amount) or amount < minimum:
        return None
    return amount


@warehouse.get("/")
def index():
    return _render_storages()


@warehouse.post("/storages")
def create_storage():
    name = request.form.get("name", "").strip()
    size = _parse_amount(request.form.get("size", ""), 0)
    storages = current_app.extensions["storages"]
    if not name or size is None or size == 0 or name in storages:
        return _render_storages("Enter a unique name and a positive size.", 400)

    storages[name] = Varasto(size)
    return redirect(url_for("warehouse.index"))


def _change_balance(name, amount, add):
    storage = current_app.extensions["storages"].get(name)
    if storage is None:
        abort(404)
    amount = _parse_amount(amount, 0)
    if amount is None:
        return _render_storages("Enter a non-negative amount.", 400)

    if add:
        storage.lisaa_varastoon(amount)
    else:
        storage.ota_varastosta(amount)
    return redirect(url_for("warehouse.index"))


@warehouse.post("/storages/<path:name>/add")
def add_item(name):
    return _change_balance(name, request.form.get("amount"), add=True)


@warehouse.post("/storages/<path:name>/remove")
def remove_item(name):
    return _change_balance(name, request.form.get("amount"), add=False)


def create_app():
    application = Flask(__name__)
    application.extensions["storages"] = {}
    application.register_blueprint(warehouse)
    return application


app = create_app()
