import json
import requests

## Defines all the dictionarys
bookingDict = {}
FIRS = {
    'ESAA': [
        'ES',
        'EUD',
        'SCA'
    ],
    'EDWW':[
        'XX',
        'EUD',
        'SCA'
    ],
    'EKDK': [
        'EK',
        'EUD',
        'SCA'
    ],
    'EFIN':[
        'EF',
        'EUD',
        'SCA'
    ],
    'ENOR':[
        'EN',
        'EUD',
        'SCA'
    ],
    'EVRR':[
        'XX',
        'EUD',
        'SCA'
    ],
    'EETT':[
        'XX',
        'EUD',
        'SCA'
    ],
    'EPWW':[
        'XX',
        'EUD',
        'SCA'
    ],
    'UMKK':[
        'XX',
        'EUD',
        'SCA'
    ]
}

## Loops fro all FIR
for FIR in FIRS:
    print(FIR)

    Temp_bookingDict = {}

    ## ESAA
    apiReq = requests.get('https://atc-bookings.vatsim.net/api/booking', params = {
        "callsign" : FIRS[FIR][0],
        "division" : FIRS[FIR][1],
        "subdivision" :FIRS[FIR][2] })

    apiData = apiReq.json()

    #Reformat to the way we want it
    for booking in apiData:
        try:
            Temp_bookingDict[booking["callsign"]].append({'type': booking['type'], 'Date':booking['start'].split()[-2], 'start':booking['start'].split()[-1], 'end':booking['end'].split()[-1]})
        except:
            Temp_bookingDict[booking["callsign"]] = [{'type': booking['type'], 'Date':booking['start'].split()[-2], 'start':booking['start'].split()[-1], 'end':booking['end'].split()[-1]}]

    bookingDict[FIR] = Temp_bookingDict

fil = open('ATC-Booking.json', 'w')
fil.write(json.dumps(bookingDict, indent=4))