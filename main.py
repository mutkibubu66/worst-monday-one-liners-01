import os

SUBJECT = "My human's Monday standup "
DURATION = "lasted nine minutes; "
FILLER = "eight were him saying 'so, yeah' "
CONTRAST = "while I had already "
FIX = "shipped the fix."
LINE = SUBJECT + DURATION + FILLER + CONTRAST + FIX

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE, "round-trip mismatch"
print(len(LINE))
