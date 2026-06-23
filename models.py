from dataclasses import dataclass

@dataclass
class ReportInput:
  customer_id: int

@dataclass
class ReportOutput:
  filename: str