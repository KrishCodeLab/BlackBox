from database import init_db, save_investigation, get_investigations

init_db()

# Save a test investigation
save_investigation(
    "test_user",
    "10:00 ERROR Database connection failed",
    {"total": 1, "errors": 1},
    "The database connection failed."
)

print("Test investigation saved!")

# Retrieve the saved investigation
records = get_investigations("test_user")

print("Retrieved records:", len(records))
print(records[0] if records else "No records found")