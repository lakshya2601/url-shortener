## for learning purpose

from pathlib import Path

db_path = Path("app.db")

print(db_path)
print(db_path.exists())
print(db_path.resolve())