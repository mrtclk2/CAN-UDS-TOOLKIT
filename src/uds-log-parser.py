services = {
    0x10: "Diagnostic Session Control",
    0x11: "ECU Reset",
    0x22: "Read Data By Identifier",
    0x27: "Security Access",
    0x2E: "Write Data By Identifier",
    0x31: "Routine Control",
    0x34: "Request Download",
    0x36: "Transfer Data",
    0x37: "Request Transfer Exit"
}

with open("examples/can_log_sample.asc", "r") as f:
    for line in f:
        if line.startswith("#") or line.strip() == "" or "date " in line:
            continue
        
        parts = line.split()
        if len(parts) < 7:
            continue

        timestamp = parts[0]
        can_id = parts[2]
        direction = parts[3]
        data = parts[6:]
        
        try:
            sid = int(data[1], 16)
        except:
            sid = None

        if sid in services:
            print(f"[{timestamp}] {direction} {can_id} SID=0x{sid:02X} ({services[sid]}) Data={data}")
        else:
            print(f"[{timestamp}] {direction} {can_id} SID=? Data={data}")
