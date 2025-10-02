# UDS Protocol Notes

Unified Diagnostic Services (UDS, ISO 14229) is the diagnostic protocol widely used in automotive systems.  
It usually runs on top of CAN, but it can also work over FlexRay, DoIP and other transports.  


## Commonly Used UDS Services

| Service ID | Name                        | Purpose / Usage                               |
|------------|-----------------------------|-----------------------------------------------|
| 0x10       | Diagnostic Session Control  | Change ECU session (default, programming, etc.)|
| 0x11       | ECU Reset                   | Trigger a reset on the ECU                    |
| 0x22       | Read Data By Identifier     | Read a specific parameter (DID) from the ECU  |
| 0x23       | Read Memory By Address      | Access memory at a given address              |
| 0x27       | Security Access             | Unlock protected features (seed/key exchange) |
| 0x28       | Communication Control       | Enable or disable certain comm channels       |
| 0x2E       | Write Data By Identifier    | Write a parameter (DID) into the ECU          |
| 0x31       | Routine Control             | Run or stop a predefined routine              |
| 0x34       | Request Download            | Start a software download (flashing)          |
| 0x36       | Transfer Data               | Transfer blocks of data during download       |
| 0x37       | Request Transfer Exit       | End the download process                      |


## Notes
- When UDS runs over CAN, it uses **ISO-TP (ISO 15765-2)** for transport.  
- Every service has a positive response, but also a set of negative response codes (NRCs) if something goes wrong.  
- Security Access (0x27) is one of the most important services for both OEMs and security researchers, since it controls who can access critical functions.  

*These notes will be extended with practical examples, logs, and some code snippets as the project grows.*
