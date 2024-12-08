# Mini-project-of-Behruzbek-Xalimov-br-

# Behruzbek_Xalimov_mini_project
Project to create simple webpage to check timetable use resources from docker



**1. Start PostgreSQL in Docker**

```bash
# Pull the latest PostgreSQL Docker image
docker pull postgres:latest

# Create a Docker container for the PostgreSQL database
docker run --name university-db -e POSTGRES_USER=Xalimovt -e POSTGRES_PASSWORD=Xalimov_pass -d -p 5432:5432 postgres:latest

# Verify the container is running
docker ps

# Access the running PostgreSQL container
docker exec -it university-db psql -U Xalimovt
```

### 2. **Set Up the PostgreSQL Database and Tables**

```sql
CREATE TABLE Timetable (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(255),
    instructor VARCHAR(255),
    day VARCHAR(50),
    time VARCHAR(50),
    room VARCHAR(50),
    level_course VARCHAR(50),
    campus VARCHAR(255)
    level INT;
);


--1 semester
INSERT INTO Timetable (course_name, instructor, day, time, room, level_course, campus, level) VALUES
('Computer Programming I', 'Kakde, Yog', 'Wednesday', '09:30 AM - 12:20 PM', '114', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 1),
('College Algebra', 'Pirnapasov', 'Wednesday', '06:30 PM - 09:20 PM', '413', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 1),
('Global Cornerstone Seminar', 'Nazarov, R', 'Wednesday', '12:30 PM - 03:20 PM', '411', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 1),
('Webster 101', 'Khegay, Ev', 'Monday', '05:30 PM - 07:20 PM', '411', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 1),
('Survey of Economics', 'Muminov, T', 'Friday', '03:30 PM - 06:20 PM', '110', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 1);

--2 Semester
INSERT INTO Timetable (course_name, instructor, day, time, room, level_course, campus, level) VALUES
('Mathematics for Computer', 'Nacional', 'Tuesday', '12:30 PM - 03:20 PM', '413', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 2),
('Network Principles', 'Goje, Niti', 'Wednesday', '03:30 PM - 06:20 PM', '304', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 2),
('Descriptive Statistics', 'Klieb, Lesl', 'Thursday', '12:30 PM - 03:20 PM', 'Online', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 2),
('Introduction to Political Theory', 'Paiva, Ale', 'Thursday', '03:30 PM - 06:20 PM', '405', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 2),
('Public Speaking', 'Khaydarov', 'Tuesday', '03:30 PM - 06:20 PM', '413', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 2),
('Introduction to Business', 'Isroilov', 'Wednesday', '06:30 PM - 09:20 PM', '101', 'Freshman', 'Webster Univ Tashkent, Uzbekistan', 2);


-- Semester 3
INSERT INTO Timetable (course_name, instructor, day, time, room, level_course, campus, level) VALUES
('Computer Programming II', 'Pimazarov', 'Friday', '04:30 PM - 06:50 PM', '115', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 3),
('Computer Languages', 'Bekov, San', 'Wednesday', '04:30 PM - 06:50 PM', '114', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 3),
('Operating Systems', 'Boeva, Sok', 'Monday', '04:30 PM - 06:50 PM', '304', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 3),
('Global Social Problems', 'Mirakilov', 'Monday', '07:00 PM - 09:20 PM', 'Online', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 3),
('Science in the News', 'Attanayake', 'Thursday', '04:30 PM - 06:50 PM', 'Online', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 3),
('Culture and Communication', 'Inprom, Ch', 'Tuesday', '04:30 PM - 06:50 PM', 'Online', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 3);

-- Semester 4
INSERT INTO Timetable (course_name, instructor, day, time, room, level_course, campus, level) VALUES
('Social Engineering and Systems Analysis', 'Now know yet', 'Wednesday', '11:30 AM', 'Room 101', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 4),
('Systems Analysis and Design', 'Now know yet', 'Tuesday', '2:00 PM', 'Room 102', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 4),
('Introduction to WebNet+', 'Now know yet', 'Thursday', '4:30 PM', 'Room 103', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 4),
('Discrete Mathematics', 'Now know yet', 'Friday', '6:00 PM', 'Room 104', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 4),
('Writing in the Workplace', 'Now know yet', 'Monday', '4:20 PM', 'Room 105', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 4),
('Computer Architecture', 'Now know yet', 'Friday', '1:50 PM', 'Room 106', 'Sophomore', 'Webster Univ Tashkent, Uzbekistan', 4);
```

### 3. **Install Python and Flask Dependencies**

```bash
# Create and activate a virtual environment
python -m venv venv
On Windows use venv\Scripts\activate

# Install Flask and pg8000 for database connection
pip install flask pg8000
```

### 4. **Create Flask Application**

```python
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
```

### 5. **HTML Templates for Flask**

#### **`index.html` (Form for Level Input)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>University Timetable</title>
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #1f1c2c, #928dab);
            color: #e0e0e0;
        }

        header {
            background: linear-gradient(90deg, #0056b3, #003f80);
            padding: 1.5rem;
            text-align: center;
            border-bottom: 4px solid #e0e0e0;
        }

        header h1 {
            font-size: 2rem;
            margin: 0;
        }

        main {
            max-width: 900px;
            margin: 3rem auto;
            padding: 2rem;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
            text-align: center;
        }

        h1 {
            margin-bottom: 1.5rem;
            font-size: 2rem;
            color: #ffffff;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1.5rem;
        }

        label {
            font-size: 1.2rem;
            color: #e0e0e0;
        }

        select {
            padding: 0.8rem;
            font-size: 1rem;
            border: 1px solid #ddd;
            border-radius: 10px;
            background: #1f1c2c;
            color: #ffffff;
            width: 60%;
        }

        button {
            background: linear-gradient(90deg, #0056b3, #003f80);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.8rem 2rem;
            font-size: 1.1rem;
            cursor: pointer;
            transition: transform 0.2s, background 0.3s ease;
        }

        button:hover {
            background: linear-gradient(90deg, #003f80, #0056b3);
            transform: scale(1.1);
        }

        .extra-buttons {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 2rem;
        }

        .extra-buttons button {
            font-size: 0.9rem;
            padding: 0.7rem 1.5rem;
            background: #444;
            color: #fff;
        }

        .extra-buttons button:hover {
            background: #555;
        }

        footer {
            margin-top: 3rem;
            text-align: center;
            font-size: 0.9rem;
            color: #aaa;
        }

        footer a {
            color: #00b0ff;
            text-decoration: none;
        }

        footer a:hover {
            text-decoration: underline;
        }

        footer .contact-info {
            margin-top: 1rem;
        }

        footer .contact-info p {
            margin: 0.5rem 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Mini project of Behruzbek Xalimov<br/>Webster University in Tashkent Timetable Portal</h1>
    </header>

    <main>
        <h1>Hello Behruzbek Xalimov!<br/>Select Your Course Level</h1>

        <form action="/timetable" method="GET">
            <label for="level">Choose your Semester:</label>
            <select name="level" id="level" required>
                <option value="" disabled selected>Select Semester</option>
                <option value="1">Semester 1</option>
                <option value="2">Semester 2</option>
                <option value="3">Semester 3</option>
                <option value="4">Semester 4</option>
            </select>
            <button type="submit">View Timetable</button>
        </form>

        <div class="extra-buttons">
            <button onclick="alert('Coming Soon: Add Course Materials!')">Add Course Materials</button>
            <button onclick="alert('Coming Soon: Download Timetable!')">Download Timetable</button>
        </div>
    </main>

    <footer>
        <p>&copy; 2024 University Timetable | <a href="https://example.com">Contact Us</a></p>
        <div class="contact-info">
            <p>Email: <a href="mailto:halimovbehruz142@gmail.com">halimovbehruz142@gmail.com</a> /
            <a href="mailto:behruzbekxalimov@webster.edu">behruzbekxalimov@webster.edu</a></p>
            <p>Phone: +998907673377 / +375259299000</p>
        </div>
    </footer>
</body>
</html>

```

#### **`timetable.html` (Displaying Timetable)**

```html

<!--<!DOCTYPE html>-->
<!--<html lang="en">-->
<!--<head>-->
<!--    <meta charset="UTF-8">-->
<!--    <meta name="viewport" content="width=device-width, initial-scale=1.0">-->
<!--    <title>Timetable for Level {{ level }}</title>-->
<!--    <style>-->
<!--        body {-->
<!--            font-family: Arial, sans-serif;-->
<!--            margin: 0;-->
<!--            padding: 0;-->
<!--            background: #f4f4f4;-->
<!--        }-->

<!--        header {-->
<!--            background: #0056b3;-->
<!--            color: white;-->
<!--            padding: 1rem;-->
<!--            text-align: center;-->
<!--        }-->

<!--        main {-->
<!--            max-width: 1000px;-->
<!--            margin: 2rem auto;-->
<!--            padding: 1.5rem;-->
<!--            background: white;-->
<!--            border-radius: 10px;-->
<!--            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);-->
<!--        }-->

<!--        h1 {-->
<!--            text-align: center;-->
<!--            margin-bottom: 1.5rem;-->
<!--            color: #333;-->
<!--        }-->

<!--        table {-->
<!--            width: 100%;-->
<!--            border-collapse: collapse;-->
<!--            margin-bottom: 1rem;-->
<!--        }-->

<!--        table, th, td {-->
<!--            border: 1px solid #ddd;-->
<!--        }-->

<!--        th, td {-->
<!--            text-align: center;-->
<!--            padding: 0.8rem;-->
<!--        }-->

<!--        th {-->
<!--            background: #0056b3;-->
<!--            color: white;-->
<!--        }-->

<!--        tr:nth-child(even) {-->
<!--            background: #f9f9f9;-->
<!--        }-->

<!--        p {-->
<!--            text-align: center;-->
<!--            color: #555;-->
<!--        }-->

<!--        a {-->
<!--            display: inline-block;-->
<!--            margin: 1rem auto;-->
<!--            text-align: center;-->
<!--            text-decoration: none;-->
<!--            color: white;-->
<!--            background: #0056b3;-->
<!--            padding: 0.7rem 1.5rem;-->
<!--            border-radius: 5px;-->
<!--            font-size: 1rem;-->
<!--            transition: background 0.3s ease;-->
<!--        }-->

<!--        a:hover {-->
<!--            background: #003f80;-->
<!--        }-->

<!--        footer {-->
<!--            margin-top: 2rem;-->
<!--            text-align: center;-->
<!--            font-size: 0.9rem;-->
<!--            color: #777;-->
<!--        }-->
<!--    </style>-->
<!--</head>-->
<!--<body>-->
<!--    <header>-->
<!--        <h1>University Timetable</h1>-->
<!--    </header>-->

<!--    <main>-->
<!--        <h1>Timetable for Level {{ level }}</h1>-->

<!--        {% if data %}-->
<!--            <table>-->
<!--                <thead>-->
<!--                    <tr>-->
<!--                        <th>Course Name</th>-->
<!--                        <th>Instructor</th>-->
<!--                        <th>Day</th>-->
<!--                        <th>Time</th>-->
<!--                        <th>Room</th>-->
<!--                        <th>Level Course</th>-->
<!--                        <th>Campus</th>-->
<!--                        <th>Level</th>-->
<!--                    </tr>-->
<!--                </thead>-->
<!--                <tbody>-->
<!--                    {% for row in data %}-->
<!--                        <tr>-->
<!--                            <td>{{ row[1] }}</td> &lt;!&ndash; course_name &ndash;&gt;-->
<!--                            <td>{{ row[2] }}</td> &lt;!&ndash; instructor &ndash;&gt;-->
<!--                            <td>{{ row[3] }}</td> &lt;!&ndash; day &ndash;&gt;-->
<!--                            <td>{{ row[4] }}</td> &lt;!&ndash; time &ndash;&gt;-->
<!--                            <td>{{ row[5] }}</td> &lt;!&ndash; room &ndash;&gt;-->
<!--                            <td>{{ row[6] }}</td> &lt;!&ndash; level_course &ndash;&gt;-->
<!--                            <td>{{ row[7] }}</td> &lt;!&ndash; campus &ndash;&gt;-->
<!--                            <td>{{ row[8] }}</td> &lt;!&ndash; level &ndash;&gt;-->
<!--                        </tr>-->
<!--                    {% endfor %}-->
<!--                </tbody>-->
<!--            </table>-->
<!--        {% else %}-->
<!--            <p>{{ message }}</p>-->
<!--        {% endif %}-->

<!--        <a href="/">Go Back</a>-->
<!--    </main>-->

<!--    <footer>-->
<!--        <p>&copy; 2024 University Timetable | <a href="https://example.com">Contact Us</a></p>-->
<!--    </footer>-->
<!--</body>-->
<!--</html>-->



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Timetable for Level {{ level }}</title>
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #1f1c2c, #928dab);
            color: #e0e0e0;
        }

        header {
            background: linear-gradient(90deg, #0056b3, #003f80);
            color: white;
            padding: 1.5rem;
            text-align: center;
        }

        header h1 {
            font-size: 2rem;
        }

        main {
            max-width: 1000px;
            margin: 2rem auto;
            padding: 2rem;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
        }

        h1 {
            text-align: center;
            margin-bottom: 2rem;
            font-size: 2rem;
            color: #ffffff;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1rem;
            background: #ffffff;
            color: #333;
            border-radius: 10px;
            overflow: hidden;
        }

        table, th, td {
            border: 1px solid #ddd;
        }

        th, td {
            text-align: center;
            padding: 0.8rem;
        }

        th {
            background: linear-gradient(90deg, #0056b3, #003f80);
            color: white;
        }

        tr:nth-child(even) {
            background: #f9f9f9;
        }

        p {
            text-align: center;
            color: #f0f0f0;
        }

        a {
            display: block;
            text-align: center;
            text-decoration: none;
            color: white;
            background: #0056b3;
            padding: 0.7rem 1.5rem;
            border-radius: 10px;
            font-size: 1rem;
            width: fit-content;
            margin: 1rem auto;
            transition: background 0.3s ease, transform 0.3s ease;
        }

        a:hover {
            background: #003f80;
            transform: scale(1.05);
        }

        footer {
            margin-top: 2rem;
            text-align: center;
            font-size: 0.9rem;
            color: #aaa;
        }

        footer a {
            color: #00b0ff;
            text-decoration: none;
        }

        footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <h1>Mini project of Behruzbek Xalimov<br/>University Timetable Portal</h1>
    </header>

    <main>
        <h1>Timetable for Semester {{ level }}<br/>For Behruzbek Xalimov</h1>

        {% if data %}
            <table>
                <thead>
                    <tr>
                        <th>Course Name</th>
                        <th>Instructor</th>
                        <th>Day</th>
                        <th>Time</th>
                        <th>Room</th>
                        <th>Level Course</th>
                        <th>Campus</th>
                        <th>Level</th>
                    </tr>
                </thead>
                <tbody>
                    {% for row in data %}
                        <tr>
                            <td>{{ row[1] }}</td> <!-- course_name -->
                            <td>{{ row[2] }}</td> <!-- instructor -->
                            <td>{{ row[3] }}</td> <!-- day -->
                            <td>{{ row[4] }}</td> <!-- time -->
                            <td>{{ row[5] }}</td> <!-- room -->
                            <td>{{ row[6] }}</td> <!-- level_course -->
                            <td>{{ row[7] }}</td> <!-- campus -->
                            <td>{{ row[8] }}</td> <!-- level -->
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% else %}
            <p>{{ message }}</p>
        {% endif %}

        <a href="/">Go Back</a>
    </main>

    <footer>
        <p>&copy; 2024 University Timetable | <a href="mailto:halimovbehruz142@gmail.com">Contact Us</a></p>
        <p>Email: <a href="mailto:halimovbehruz142@gmail.com">halimovbehruz142@gmail.com</a> / <a href="mailto:behruzbekxalimov@webster.edu">behruzbekxalimov@webster.edu</a></p>
        <p>Phone: +998907673377 / +375259299000</p>
    </footer>
</body>
</html>

```

### 6. **Running the Flask Application**

```bash
# Make sure you're in the directory with your Flask app
# Run the Flask app
python app.py
```

### 7. **Accessing the Application**

- Navigate to `http://127.0.0.1:5000/` in your web browser to see the application in action.

### 8. **Stop the Docker Container**

```bash
# Stop the PostgreSQL Docker container after you're done
docker stop university-db
```

---

These are the commands and steps you would use to deploy and run this project. You can adapt or extend the project as needed based on additional requirements.


![image](https://github.com/user-attachments/assets/d724cec7-d29b-4086-9ea4-eaaa93f25bf5)
![image](https://github.com/user-attachments/assets/eeb2cd81-cde5-40d5-987d-1d06b64db475)
![image](https://github.com/user-attachments/assets/79cedb97-293c-43be-a0e6-e7a4e470d316)
![image](https://github.com/user-attachments/assets/bce7731d-aeb7-44a8-90d4-b138adfcd912)
![image](https://github.com/user-attachments/assets/77d5faa6-6701-460f-9771-3c11a1abb8d2)
