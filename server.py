from flask import Flask, request
import random
import time

app = Flask(__name__)



@app.route('/', methods=['GET'])
def m():
    return ("Welcome!")

@app.route('/respond', methods=['POST'])
def respond():
    start = time.time()
    starting_fuel_level = random.randint(1,7) # starting random fuel level
    reply = ''
    communication = request.get_json()['string'] # 001 010 000 010 001 010 011 011 100
    commands = communication.split()
    i = 0
    f=0
    nf = 0
    while i < len(commands):
        if commands[i] == '001':
            reply += ack()
        elif commands[i] == '010':
            if (has_fuel_issue):
                f+=1
                reply += flt(gen_fault_code(commands[i+1])) # include randomness
            else:
                nf += 1
                reply += oky()
            i += 1
        elif commands[i] == '011':
            reply += lvl(gen_level_report(starting_fuel_level)) # randomness of reports needed
        elif commands[i] == '100':
            reply += end()
        i += 1

    return {'response' : reply[:-1], 'f': f, 'nf':nf}

def ack():
    return ('001 ')

def flt(fault_code):
    fault_code = fault_code[:3] + ' ' + fault_code[3:]
    return (f'010 {fault_code} ')

def oky():
    return ('011 ')

def end():
    return ('100 ')

def lvl(report):
    return (f'101 {report} ')


# generating random behavior

def has_fuel_issue(component_number):
    random.seed(component_number + str(int(time.time()/10))) # simulated randomness, associated with time. 10 seconds between changes
    return random.choice([0, 1])

def gen_fault_code(component_number):
    random.seed(component_number + str(int(time.time()/3))) # simulated randomness, different issue as time passes. 3 seconds between new issues
    return (str(format(random.randint(1,63), '06b'))) # random from 000 001 to 111 111

def gen_level_report(s):
    return (str(format(s - random.choice([0, 1]), '03b')) + ' ' + str(format(random.choice([0, 7]), '03b')))


if __name__ == '__main__':
    app.run(debug=True, port=3030)