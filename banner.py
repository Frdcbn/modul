import subprocess
import geocoder
import platform
from rich.columns import Columns
from rich.panel import Panel
from rich import print as cetak
import platform
from rich.console import Console
hijau1 = "\033[1;92m"#Terang
kuning1 = "\033[1;93m"#Terang
putih1 = "\033[1;97m"#Terang
merah1 = "\033[1;91m"#Terang
biru1 = "\033[1;94m"#Terang
def get_system_info():
    system_info = {}
    system_info['OS'] = platform.system()
    system_info['OS Version'] = platform.release()
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()

    return system_info

def get_memory_info():
  memory_info = {}
  system = platform.system()
  try:
    if system == 'Linux' or system == 'Darwin':  # Linux or macOS
        try:
            output = subprocess.check_output(['free', '-h']).decode('utf-8')
            lines = output.splitlines()

            total_memory = lines[1].split()[1]
            used_memory = lines[1].split()[2]
            memory_info['Total Memory'] = total_memory
            memory_info['Used Memory'] = used_memory
        except subprocess.CalledProcessError:
            memory_info['Total Memory'] = 'N/A'
            memory_info['Used Memory'] = 'N/A'
    elif system == 'Windows':  # Windows
        try:
            output = subprocess.check_output(['wmic', 'OS', 'get', 'TotalVisibleMemorySize,FreePhysicalMemory', '/Value']).decode('utf-8')
            lines = output.strip().split('\n')

            total_memory = int(lines[0].split('=')[1]) // 1024  # Convert to GB
            used_memory = (int(lines[1].split('=')[1]) // 1024)  # Convert to GB
            memory_info['Total Memory'] = f"{total_memory} GB"
            memory_info['Used Memory'] = f"{used_memory} GB"
        except subprocess.CalledProcessError:
            memory_info['Total Memory'] = 'N/A'
            memory_info['Used Memory'] = 'N/A'
    else:
        memory_info['Total Memory'] = 'N/A'
        memory_info['Used Memory'] = 'N/A'

    return memory_info
  except Exception as e:
    memory_info['Total Memory'] = 'N/A'
    memory_info['Used Memory'] = 'N/A'
    return memory_info

def get_uptime():
    if platform.system() == 'Linux':
        try:
            output = subprocess.check_output(['uptime', '-p']).decode('utf-8').strip()
            return output
        except subprocess.CalledProcessError:
            return 'N/A'
    else:
        return 'N/A'

def get_location_info():
    g = geocoder.ip('me')
    return g
def banner(name):
    location_info = get_location_info()
    system_info = get_system_info()
    memory_info = get_memory_info()
    uptime = get_uptime()
    banner=("""              [green]╔╦╗╦ ╦╦ ╔╦╗╦╔═╗╦  ╔═╗  ╔═╗╔═╗╦═╗╦╔═╗╔╦╗
              [yellow]║║║║ ║║  ║ ║╠═╝║  ║╣   ╚═╗║  ╠╦╝║╠═╝ ║
              [blue]╩ ╩╚═╝╩═╝╩ ╩╩  ╩═╝╚═╝  ╚═╝╚═╝╩╚═╩╩   ╩
"""
"        [green] [white]: [yellow]MR.BADUT     [green] [white]: [yellow]t.me/MRDEMONSCRIPT     [green] [white]: [yellow]Python")
    info_text = (
        f"[green] IP[white] : [yellow]{location_info.ip}\n"
        f"[green] COUNTRY[white] : [yellow]{location_info.country}\n"
        f"[green] PROVINCE[white] : [yellow]{location_info.state}\n"
        f"[green] CITY[white] : [yellow]{location_info.city}\n"
        f"[green] COORDINATE[white] : [yellow]{location_info.latlng}\n"
    )
    info_text1 = (
        f"[green] DEVICE OS[white] : [yellow]{system_info['OS']} {system_info['OS Version']}\n"
        f"[green] ARCHITECTURE[white] : [yellow]{system_info['Machine']}\n"
        f"[green] VERSION[white] : [yellow]{platform.uname().release}\n"
        f"[green] ACTIVE[white] : [yellow]{uptime}\n"
        f"[green] RAM[white] : [yellow]{memory_info['Used Memory']} / {memory_info['Total Memory']}"
    )

    banner_content = (
        f"{info_text}"
        f"\n{info_text1}"
    )
    # Print the MAIN MENU text in a larger font
    #cetak(Panel(banner, width=90, title=f"[bold green]{name}", padding=(5, 2), style="white on black",))
    
    cetak(Panel(banner, width=80,title=f"[bold green]{name}", padding=(0, 4), style="bold white"))
    cetak(Panel(banner_content, width=80,title=f"[bold green]Your Information", padding=(0, 4), style="bold white"))

#banner("System Information")
