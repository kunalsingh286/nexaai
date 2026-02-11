import structlog
import logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s"
    )

    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ],
    )

    return structlog.get_logger()
