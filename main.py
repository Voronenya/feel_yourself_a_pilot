import os
help = {
    'start': 'start the engine',
    'stop': 'stop the engine',
    'departure': 'departure from the airport',
    'arrival': 'arrive to the airport',
    'quit': 'to exit'
}
print('Dear passengers welcome on board.')
command = ''
flight = False
started = False
while True:
    command = input('>').lower()
    if command == 'help':
        for key, value in help.items():
            print(key, '-', value)

#start command
    elif command == 'start':
        if started and flight:
            print("Hey, you are in the air!")
        if started and not flight:
            print("Engine is already started!")
        if not started and flight:
            print('You successfully prevented your aircraft from the crash!')
        if not started and not flight:
            started = True
            print('Please fasten your seat belt. Engine is started...We are ready for departure!')

#departure command
    elif command == 'departure':
        if started and flight:
            print("You already in the air")
        if started and not flight:
            flight = True
            print('You have departed! What is the great view in the sky!')
        if not started and flight:
            print('You are in simulator? or just high?')
        if not started and not flight:
            print('First start your engine')

#arrival command
    elif command == 'arrival':
        if started and flight:
            flight = False
            print('Congratulation! You just landed the aircraft')
        elif started and not flight:
            print("You are on the ground. Sop your engine or go for departure")
        if not started and flight:
            print('Most probably you are falling')
        if not started and not flight:
            print("You ain't even departed, better go check your aircraft")

#stop command
    elif command == 'stop':
        if not started and not flight:
            print("Engine is already stopped!")
        if started and flight:
            started = False
            print("You have made a mistake and your engine is off") #add timer
        elif not started and flight:
            print('WTF??? Are you a bird?')
            while True:
                answer = str(input('Do you want to start from the beginning?\n'))
                if answer in ('yes', 'y', 'n', 'no'):
                    break
                print('invalid input')
            if answer == 'yes' or answer == 'y':
                os.system('python main.py')
                print('Restarting...')
            else:
                print('Goodbye')
                break
        if started and not flight:
            started = False
            print('Engine is stopped')
    elif command == 'quit':
        print('Thank you for joining us on this trip and we are looking forward to seeing you on board again')
        break

#no correct command
    else:
        print("Please repeat your request")
