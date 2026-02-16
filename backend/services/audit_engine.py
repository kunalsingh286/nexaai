from datetime import datetime
import json
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


class AuditLogger:

    def log(self, user_id, action, data):

        record = {
            "time": str(datetime.utcnow()),
            "user_id": user_id,
            "action": action,
            "data": data
        }

        file = LOG_DIR / "audit.log"

        with open(file, "a") as f:
            f.write(json.dumps(record) + "\n")


logger = AuditLogger()
