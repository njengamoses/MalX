from rich import print
from rich.console import Console

from core.scanner import scan_file
from core.utils import save_report

console = Console()

print("[bold cyan]MalX Malware Detection System[/bold cyan]")

while True:

    print("\n[bold yellow]--- MENU ---[/bold yellow]")
    print("1. Scan file")
    print("2. Exit")

    choice = input("\nSelect option: ")

    if choice == "1":

        filepath = input("\nEnter file path: ")

        result = scan_file(filepath)

        print("\n[bold green]--- SCAN RESULTS ---[/bold green]\n")

        if "error" in result:
            print(f"[red]Error:[/red] {result['error']}")

        else:
            print(f"[blue]File:[/blue] {result['file']}")
            print(f"[blue]Risk:[/blue] {result['risk']}")
            print(f"[blue]Score:[/blue] {result['score']}")

            if result["findings"]:
                print("\n[bold red]Findings:[/bold red]")

                for finding in result["findings"]:
                    print(f"- {finding}")

            else:
                print("[green]No suspicious patterns detected.[/green]")

            report = (
                f"File: {result['file']} | "
                f"Risk: {result['risk']} | "
                f"Score: {result['score']} | "
                f"Findings: {', '.join(result['findings'])}"
            )

            save_report("reports/report.txt", report)

    elif choice == "2":
        print("[cyan]Exiting MalX...[/cyan]")
        break

    else:
        print("[red]Invalid option.[/red]")
