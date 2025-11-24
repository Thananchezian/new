#!/usr/bin/env python3
"""
Educational calculator app showing:
- How SQL Injection WOULD happen
- How XSS WOULD happen
But implemented safely.

This file is SAFE to run and cannot be exploited.
"""

from flask import Flask, request, escape
import sqlite3
import html

app = Flask(__name__)


# --------------------------
# Database setup (safe)
# --------------------------
def init_db():
    conn = sqlite3.connect("calc.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            score INTEGER
        )
    """)
    cur.execute("INSERT INTO users(name, score) VALUES(?, ?)", ("alice", 42))
    conn.commit()
    conn.close()


# --------------------------
# SAFE Query Function
# --------------------------
def safe_lookup_user(username):
    """
    Demonstrates the correct, safe way to avoid SQL injection.
    """

    # ❌ What NOT to do (vulnerable pattern shown as a comment):
    #
    # vulnerable_query = (
    #     "SELECT score FROM users WHERE name = '" + username + "'"
    # )
    #
    # This would allow SQL injection:
    #   alice' OR '1'='1
    #
    # ------------------------------------------------------------

    # ✔ SAFE version: parameterized SQL
    conn = sqlite3.connect("calc.db")
    cur = conn.cursor()
    cur.execute("SELECT score FROM users WHERE name=?", (username,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None


# --------------------------
# Calculator Route
# --------------------------
@app.route("/calc")
def calc():
    expression = request.args.get("expr", "")
    username = request.args.get("user", "")

    # ❌ What NOT to do (vulnerable XSS example shown as comment):
    #
    # return f"<p>Result is: {expression}</p>"
    #
    # If expression = <script>alert(1)</script>
    # → browser executes JavaScript
    #
    # ------------------------------------------------------------

    # ✔ SAFE version: escape user-provided input
    safe_expr = html.escape(expression)

    # Calculator logic (eval avoided for safety)
    try:
        # Simple restricted safe evaluator
        allowed_chars = "0123456789+-*/(). "
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Invalid characters in expression")

        result = eval(expression, {"__builtins__": {}})
    except Exception:
        result = "Error"

    score = safe_lookup_user(username)

    # Output is fully escaped to prevent XSS
    return f"""
    <h2>Safe Calculator Demo</h2>
    <p><b>You entered:</b> {safe_expr}</p>
    <p><b>Result:</b> {escape(str(result))}</p>
    <p><b>User score:</b> {escape(str(score))}</p>
    <hr>
    <p>This page demonstrates where SQL injection and XSS *would* occur,</p>
    <p>but the code has been written using safe patterns.</p>
    """


# --------------------------
# Main
# --------------------------
if __name__ == "__main__":
    init_db()
    print("Running safe educational calculator demo...")
    app.run(debug=True)
