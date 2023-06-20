import subprocess
import geocoder
import platform

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
    print(putih1 + f' {name} '.center(56, "•"))
    print(f"""
{biru1}╔╦╗╦ ╦╦ ╔╦╗╦╔═╗╦  ╔═╗  ╔═╗╔═╗╦═╗╦╔═╗╔╦╗
{hijau1}║║║║ ║║  ║ ║╠═╝║  ║╣   ╚═╗║  ╠╦╝║╠═╝ ║ 
{merah1}╩ ╩╚═╝╩═╝╩ ╩╩  ╩═╝╚═╝  ╚═╝╚═╝╩╚═╩╩   ╩ 
{merah1} {putih1}: {hijau1}MR.BADUT     {merah1} {putih1}: {hijau1}t.me/MRDEMONSCRIPT     {merah1} {putih1}: {hijau1}Python""")
    print(putih1 + " Your information ".center(56, "•"))
    location_info = get_location_info()
    system_info = get_system_info()
    memory_info = get_memory_info()
    uptime = get_uptime()
    print(merah1 + ""+hijau1+" IP " + putih1 + ":" + kuning1, location_info.ip)
    print(merah1 + ""+hijau1+" COUNTRY " + putih1 + ":" + kuning1, location_info.country)
    print(merah1 + ""+hijau1+" PROVINCE " + putih1 + ":" + kuning1, location_info.state)
    print(merah1 + ""+hijau1+" CITY " + putih1 + ":" + kuning1, location_info.city)
    print(merah1 + ""+hijau1+" COORDINATE " + putih1 + ":" + kuning1, location_info.latlng)
    print(merah1 + ""+hijau1+" DEVICE OS " + putih1 + ":" + kuning1, system_info['OS'], system_info['OS Version'])
    print(merah1 + ""+hijau1+" ARCHITECTURE " + putih1 + ":" + kuning1, system_info['Machine'])
    print(merah1 + ""+hijau1+" VERSION " + putih1 + ":" + kuning1, platform.uname().release)
    print(merah1 + ""+hijau1+" ACTIVE " + putih1 + ":" + kuning1, uptime)
    print(merah1 + ""+hijau1+" RAM " + putih1 + ":" + kuning1, memory_info['Used Memory'], "/", memory_info['Total Memory'])
    print(putih1 + "".center(56, "•"))

#banner("System Information")
