import psutil
from rich.console import Console
from rich.table import Table
from time import sleep
import os
import subprocess

console = Console()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def gpu_info():
    gpus_list = []
    try:
        result = subprocess.run(
            ["nvidia-smi", 
             "--query-gpu=name,utilization.gpu,memory.used,memory.total", 
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, check=True
        )
        for line in result.stdout.strip().split("\n"):
            name, util, mem_used, mem_total = line.split(", ")
            barras_gpu = "█" * int(int(util)/5)
            gpus_list.append(f"{name}: {util}% [{barras_gpu}] VRAM: {mem_used}/{mem_total} MB")
    except Exception:
        gpus_list.append("GPU info not available (NVIDIA required)")
    return gpus_list

def mostrar_sysmonitor():
    while True:
        limpar_tela()
        
        console.rule("[bold red]GPU Usage[/bold red]")
        for gpu in gpu_info():
            console.print(gpu)

        # RAM
        ram = psutil.virtual_memory()
        console.rule("[bold green]RAM Usage[/bold green]")
        barras_ram = "█" * int(ram.percent/2)
        console.print(f"Used: {ram.percent}% ({ram.used // (1024**2)}MB / {ram.total // (1024**2)}MB)")
        console.print(barras_ram)

        console.rule("[bold blue]Disk Usage[/bold blue]")
        partitions = psutil.disk_partitions()
        for part in partitions:
            try:
                usage = psutil.disk_usage(part.mountpoint)
                barras_disk = "█" * int(usage.percent/2)
                console.print(f"{part.device} ({part.mountpoint}) - {usage.percent}% used")
                console.print(barras_disk)
            except PermissionError:
                continue

        console.rule("[bold yellow]Top 5 Processes by CPU[/bold yellow]")
        processes = [(p.info['cpu_percent'], p.info['name'], p.info['pid']) 
                     for p in psutil.process_iter(['cpu_percent', 'name', 'pid'])]
        processes.sort(reverse=True)
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("PID", justify="right")
        table.add_column("Name")
        table.add_column("CPU %", justify="right")
        for cpu, name, pid in processes[:5]:
            table.add_row(str(pid), name, f"{cpu}")
        console.print(table)
        
        sleep(1)

if __name__ == "__main__":
    mostrar_sysmonitor()
