
import datetime, Bible_verses

today = datetime.date(2025, 4, 20).weekday()


if today == 6:
  print(f"Special Verse: {Bible_verses.special_verse}")
else:
  print(f"Verse of the Day: {Bible_verses.random_verse}")