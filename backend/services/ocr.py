from paddleocr import PaddleOCR


ocr_engine = PaddleOCR(use_angle_cls=True, lang="en")


def run_ocr(image_path: str) -> str:
    result = ocr_engine.ocr(image_path)

    text_lines = []

    for page in result:
        for line in page:
            text_lines.append(line[1][0])

    return "\n".join(text_lines)
