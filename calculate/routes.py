from flask import render_template, request, url_for
from . import calculate_bp


# ---------------- HOME ----------------
@calculate_bp.route("/")
def home():
    return render_template('home.html')


# ---------------- PRIME NUMBER ----------------
@calculate_bp.route("/prime", methods=['GET','POST'])
def prime():
    if request.method == "GET":
        return render_template("body.html")

    num_str = request.form.get("Enter your number", "").strip()

    if not num_str.isdigit():
        return render_template("body.html", value=f"Invalid input '{num_str}'. Please enter a valid number (e.g., 123)")

    number = int(num_str)
    primes = []

    for i in range(2, number):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)

    return render_template("body.html",value=f"Prime numbers of '{number}' = {primes}")


# ---------------- FACTORIAL ----------------
@calculate_bp.route("/factorial", methods=['GET','POST'])
def form():
    if request.method == "GET":
        return render_template("form.html")

    num_str = request.form.get("Enter your number", "").strip()

    if not num_str.isdigit():
        return render_template("form.html",score=f"Invalid input '{num_str}'. Please enter a valid number (e.g., 123)")

    n = int(num_str)
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return render_template("form.html", score=f"Factorial of '{n}' = {fact}")


# ---------------- FIBONACCI ----------------
@calculate_bp.route("/fibonacci", methods=['GET','POST'])
def form2():
    if request.method == "GET":
        return render_template("form2.html")

    num_str = request.form.get("Enter your number", "").strip()

    if not num_str.isdigit():
        return render_template("form2.html",
                               fibonacci=f"Invalid input '{num_str}'. Please enter a valid number (e.g., 123)")

    count = int(num_str)
    result = []
    a, b = 0, 1

    for _ in range(count):
        result.append(a)
        a, b = b, a + b

    return render_template("form2.html",
                           fibonacci=f"Fibonacci sequence of '{count}' = {result}")


# ---------------- LONGEST WORD ----------------
@calculate_bp.route("/longest", methods=['GET','POST'])
def form3():
    if request.method == "GET":
        return render_template("form3.html")

    text = request.form.get("Enter your number", "")
    words = text.split()

    if not words:
        return render_template("form3.html", num="Please enter a sentence (eg. Hello word)")

    longest = max(words, key=len)

    return render_template("form3.html",
                           num=f"Longest word of '{text}' = '{longest}'")


# ---------------- REVERSE NUMBER/TEXT ----------------
@calculate_bp.route("/reverse", methods=['GET','POST'])
def reverse():
    if request.method == "GET":
        return render_template("profile.html")

    value = request.form.get("Enter your value")

    if value.isdigit():
        n = int(value)
        rev = int(str(n)[::-1])
        answer = f"Reversed number of '{value}' = {rev}"
    else:
        answer = f"Reversed text of '{value}' = {value[::-1]}"

    return render_template("profile.html", rever=answer)


# ---------------- EVEN OR ODD ----------------
@calculate_bp.route("/evenorodd", methods=['GET','POST'])
def form4():
    if request.method == "GET":
        return render_template("form4.html")

    num_str = request.form.get("Enter your number", "").strip()

    if not num_str.isdigit():
        return render_template("form4.html",put=f"Invalid input '{num_str}'. Please enter a valid number (e.g., 123)")

    n = int(num_str)
    msg = "Even" if n % 2 == 0 else "Odd"

    return render_template("form4.html",put=f"Number '{n}' is {msg}")


# ---------------- BMI ----------------
@calculate_bp.route("/BMI", methods=['GET','POST'])
def form5():
    if request.method == "GET":
        return render_template("form5.html")

    # Get form values
    weight_str = request.form.get("weight", "").strip()
    height_str = request.form.get("hight", "").strip()

    # Validate: Check empty fields
    if weight_str == "" or height_str == "":
        return render_template(
            "form5.html",
            data="Error: Weight and height cannot be empty. Please enter valid numbers."
        )

    # Validate: Check if numeric
    if not weight_str.replace('.', '', 1).isdigit() or not height_str.replace('.', '', 1).isdigit():
        return render_template(
            "form5.html",
            data=f"Error: Invalid input (Weight: '{weight_str}', Height: '{height_str}'). Please enter numeric values."
        )

    # Convert to numbers
    weight = float(weight_str)
    height_ft = float(height_str)

    # Convert feet → meters
    height_m = height_ft / 3.28

    # BMI calculation
    bmi = weight / (height_m ** 2)

    # Success message
    return render_template(
        "form5.html",
        data=f"You entered weight '{weight}' kg and height '{height_ft}' ft. Your BMI = {bmi:.1f}"
    )


# ---------------- ARMSTRONG ----------------
@calculate_bp.route("/armstrong", methods=['GET','POST'])
def armstrong():
    if request.method == "GET":
        return render_template("index.html")

    num_str = request.form.get("Enter your number", "").strip()

    if not num_str.isdigit():
        return render_template("index.html", dt=f"Invalid input '{num_str}'. Please enter a valid number (e.g., 123)")

    n = int(num_str)
    s = sum(int(d) ** 3 for d in num_str)

    if n == s:
        msg = "Armstrong number"
    else:
        msg = "Not an Armstrong number"

    return render_template("index.html", dt=f"You entered '{num_str}' = '{msg}'")


# ---------------- PELINDROME ----------------
@calculate_bp.route("/pelindrome", methods=['GET','POST'])
def pelindrome():
    if request.method == "GET":
        return render_template("form6.html")

    text = request.form.get("Enter your number", "").lower()

    if text == text[::-1]:
        msg = f"is a palindrome"
    else:
        msg = f"is NOT a palindrome"

    return render_template("form6.html", pen=f"You entered '{text}' = '{msg}'")
