# natureremo
Using Nature Remo to control home appliances

### What we can do
 - Get Nature Remo info
 - Analyze infrared signal
 - Transmit infrared signal
 - Register infrared signal
 - Remote control Sharp TV

### Get Nature Remo info
 - Get Remo's instance name `dns-sd -B _remo._tcp`
 - Get Remo's ip address `dns-sd -G v4 ${Instance Name}.local`
 
### Analyze infrared signal
 - Set Remo's ip address to `IP_ADDRESS`
 - Set output file name to `FILE_NAME`
 - Run `remo_analysis.py`

### Transmit infrared signal
- Set Remo's ip address to `IP_ADDRESS`
- Set input file name to `FILE_NAME`
- Run `remo_transmission.py`

### Register infrared signal

### Remote control Sharp TV