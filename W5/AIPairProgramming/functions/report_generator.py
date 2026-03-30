


def generate_report(data):
    """
    Generate a report based on the provided data.

    Args:
        data (dict): A dictionary containing the data to be included in the report.

    Returns:
        str: A formatted report as a string.
    """

    report = f"# Data Quality Report\n\n"
    report += f"**Generated**: {data.get('generated', 'N/A')}\n"
    report += f"**File**: {data.get('file', 'N/A')}\n"
    report += f"**Total Rows**: {data.get('total_rows', 0)}\n\n"

    report += "## Summary\n\n"
    report += "| Check | Status | Issues Found |\n"
    report += "| ----- | ------ | ------------ |\n"

    for check in data.get('checks', []):
        report += f"| {check['name']} | {check['status']} | {check['issues']} |\n"

    report += "\n## Detailed Results\n\n"

    for check in data.get('checks', []):
        report += f"### {check['name']} - {check['status']}\n"
        report += f"{check.get('details', '...')}\n\n"

    return report