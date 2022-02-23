files = ['impegniICal.ics','impegniICal_sfp.ics']

output = open('impegniICal_reordered.ics','w')
corsi = ['THEORETICAL',
        'INFORMATICA PER LA SCUOLA PRIMARIA',
        'MACHINE LEARNING',
        'VIRTUAL REALITY',
        'INTELLIGENT SYSTEMS']

header  = 'BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:00000\n'
output.write(header)


for input in files:
    input_file = open(input,'r')
    Lines = input_file.readlines()

    tmp = ''
    for line in Lines:
        if 'BEGIN:VEVENT' in line :
            if '' != tmp:
                for corso in corsi:
                    if corso in tmp:
                        output.write(tmp)
                tmp = ''
        
        tmp+= line
    input_file.close()
trailer = 'END:VCALENDAR'
output.write(trailer)
output.close()