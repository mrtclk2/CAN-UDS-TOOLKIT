# CAN Protocol Notes

Controller Area Network (CAN) is the standard communication bus used in almost every modern vehicle.  
It lets multiple ECUs (Electronic Control Units) talk to each other without needing a central host computer.  


## Key Points
- Multi-master bus (every node can start talking if the bus is free).  
- Message-based, not node-based → messages are identified by their ID, not by sender address.  
- Very reliable: built-in error detection and fault confinement.  
- Speeds: usually 125 kbps to 1 Mbps (Classical CAN), and up to 8 Mbps with CAN FD.  


## Frame Layout (Classical CAN)

| Field          | Bits       | What it does                               |
|----------------|------------|--------------------------------------------|
| Start of Frame | 1          | Marks the start of a new frame             |
| Identifier     | 11 or 29   | Message ID (priority is based on the value)|
| Control        | 6          | Includes Data Length Code (DLC)            |
| Data           | 0–64       | Up to 8 bytes (64 for CAN FD)              |
| CRC            | 15 + 1     | Error checking (Cyclic Redundancy Check)   |
| ACK            | 2          | Acknowledgement slot                       |
| End of Frame   | 7          | Marks the end of the frame                 |


## Common Tools & Software
- **SocketCAN** (Linux kernel CAN stack)  
- **python-can** (handy Python library for logging/scripting)  
- **Vector CANoe / CANalyzer** (industry standard tools)  
- **PEAK PCAN** tools (popular USB adapters + software)  
