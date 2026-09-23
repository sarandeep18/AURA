"""
Description: Exports important AURA processing information
into a log file.

Concepts used:

1. open()
   - Used to create and write to a file.

2. write()
   - Used to add information to the log file.

Real-life Example:
Logs help developers track what happened
during project execution.
"""


def export_logs(dataset):

    try:

        with open(
            "reports/AURA_logs.txt",
            "w"
        ) as log_file:

            log_file.write(
                "AURA Processing Log\n"
            )

            log_file.write(
                "-------------------------\n"
            )

            log_file.write(
                f"Total Rows : {dataset.shape[0]}\n"
            )

            log_file.write(
                f"Total Columns : {dataset.shape[1]}\n"
            )

            log_file.write(
                "Data processing completed successfully.\n"
            )

        print("AURA logs exported successfully.")

        return dataset

    except Exception as log_export_error:

        print("Unable to export AURA logs.")
        print(log_export_error)

        return None