from pathlib import Path
log_path = Path("logs/sample_auth.log")

suspicious_words=["failed","unauthorized","warning","error"]

print("Suspicious Log Entries")
print("=============================")

if log_path.exists():
    with open(log_path,"r",encoding="utf-8") as file:
        for line in file:
            line_lower = line.lower()
            
            for word in suspicious_words:
                if word in line_lower:
                    print(line.strip())
                    break
else:
    print("Log file not found:",log_path)