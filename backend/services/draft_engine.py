from datetime import date
from pathlib import Path


TEMPLATE_DIR = Path("templates")


class DraftEngine:

    def render(self, template_name: str, data: dict):

        template_path = TEMPLATE_DIR / template_name

        text = template_path.read_text()

        for k, v in data.items():
            text = text.replace("{{" + k + "}}", str(v))

        text = text.replace("{{date}}", str(date.today()))

        return text


engine = DraftEngine()
