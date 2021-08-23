from flask import Flask
from flask import request
from app.errors import InvalidDataInput
from app.mutants import is_mutant
from http import HTTPStatus


def create_app():
    flask_app = Flask(__name__, static_folder=None, static_url_path=None)
    flask_app.url_map.strict_slashes = False

    @flask_app.route("/mutant", methods=["POST"])
    def mutant_check():
        data = request.get_json(force=True, silent=True) or {}

        if not data or "dna" not in data:
            raise InvalidDataInput

        result = is_mutant(data.get("dna"))

        if result:
            return "", HTTPStatus.OK
        else:
            return "", HTTPStatus.FORBIDDEN

    return flask_app
