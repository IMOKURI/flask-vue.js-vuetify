from flask import Flask, render_template

APP = Flask(
    __name__,
    static_folder="../frontend/dist/static",
    template_folder="../frontend/dist",
)


@APP.route("/", defaults={"path": ""})
@APP.route("/<path:path>")
def index(path):
    return render_template("index.html")


if __name__ == "__main__":
    APP.run(host="0.0.0.0")
