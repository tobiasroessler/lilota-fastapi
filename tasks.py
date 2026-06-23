from lilota.worker import LilotaWorker
import time
from models import ReportInput, ReportOutput


worker = LilotaWorker(
    db_url="sqlite:///tasks.db"
)


@worker.task
def generate_report(data: ReportInput) -> ReportOutput:
    # Simulate a long-running operation
    time.sleep(10)

    # Return the output
    return ReportOutput(
        filename = f"report-{data.customer_id}.pdf"
    )


def main():
    worker.start()


if __name__ == "__main__":
    main()