from flask import Flask, render_template, request
import pg8000

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        level = request.form["level"]

        return render_template("timetable.html", level=level, data=[], message="Loading timetable...")

    return render_template("index.html")


@app.route("/timetable", methods=["GET"])
def timetable():
    level = request.args.get('level')
    if not level:
        return "Level not provided", 400

    try:
        conn = pg8000.connect(
            user="Xalimovt",
            password="Xalimov_pass",
            host="localhost",
            port=5432,
            database="Xalimovt"
        )

        cur = conn.cursor()
        query = "SELECT * FROM Timetable WHERE level = %s;"
        cur.execute(query, (level,))
        rows = cur.fetchall()

        cur.close()
        conn.close()

        if rows:
            return render_template("timetable.html", level=level, data=rows, message="")
        else:
            return render_template("timetable.html", level=level, data=[], message="No data found for this level.")
    except Exception as e:
        return f"An error occurred: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)