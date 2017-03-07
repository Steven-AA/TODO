#!python2
'''using python 2.7'''
#coding:utf-8

import time
import datetime
import msvcrt

DATAPATH = 'data'
BACKUPPATH = 'backup'
ALL_TODO = {}
ALL_DONE = {}

START_MENU = 'a)add todo\ne)edit\nq)quit\n'
MENU2 = 'd)deadlind\n'
EDIT_MENU = 'd)done\n'
def write_data():
    '''write data'''
    all_data = ''
    for todo in ALL_TODO:
        print todo
        todo_ = ALL_TODO[todo]
        data = todo_.show()
        all_data += data +'\n'
    fff = open(DATAPATH, 'w')
    fff.write(all_data)
class Time(object):
    '''time'''
    time = ''
    timestamp = ''
    def __init__(self):
        '''init'''

    def record(self):
        '''recode'''
        self.time, self.timestamp = record()
    def input(self, time_input):
        '''input time'''
        try:
            if not time_input == 'q':
                time_input = time.mktime(time.strptime(time_input, '%Y-%m-%d %H:%M:%S'))
            else:
                return
        except:
            print 'input error'
            time_input = raw_input('Input the deadline(eg.2017-3-3 13:00:00)(q to pass):')
            self.input(time_input)
        self.timestamp = time_input
        self.time = time.mktime(time.localtime(time_input))
        print 'time:', self.time

class Todo(object):
    ''' todo '''
    state = 'todo'
    name = ''
    finishTime = Time()
    cancelTime = Time()
    startTime = Time()
    deadline = Time()
    predictTime = 0
    def __init__(self):
        pass
    def add(self):
        '''add'''
        self.name = raw_input('Input the todo name:')
    def input_deadline(self):
        '''input deadline'''
        time_input = raw_input('Input the deadline(eg.2017-3-3-13:00:00):')
        '''
        if not time_input == 'q':
            self.deadline.input(time_input)
        '''
        self.deadline.input(time_input)

    def start(self):
        '''start'''
        self.state = 'UNDERGO'
        self.startTime.record()
    def cancel(self):
        '''cancel'''
        self.state = 'CANCELED'
        self.cancelTime.record()
    def done(self):
        '''done'''
        self.state = 'DONE'
        self.finishTime.record()
        print self.finishTime.timestamp
    def show(self):
        '''show'''
        data = ''
        data += self.name + ' '
        data += self.state + ' '
        if self.deadline.time:
            data += str(self.deadline.time) + ' '
        else:
            data += '0 '
        if self.startTime.time:
            data += str(self.startTime.time) + ' '
        else:
            data += '0 '
        if self.finishTime.time:
            data += str(self.finishTime.time) + ' '
        else:
            data += '0 '
        if self.cancelTime.time:
            data += str(self.cancelTime.time) + ' '
        else:
            data += '0 '
        return data



def print_time(flag, time_type):
    '''
    print time
    1 TIMESTAMMP
    0 TIME
    '''
    if flag == 1:
        return time_type.timestamp
    else:
        return time_type.time
def get_time():
    '''return time.time(), time.ctime()'''
    return time.time(), time.ctime()

def record():
    '''return time.time(), time.ctime()'''
    return get_time()

def backup():
    '''backu with global variable'''
    print 'backup the data......'
    try:
        open(BACKUPPATH, "w").write(open(DATAPATH, "r").read())
    except:
        print 'no data found'
    return

def load_data():
    '''load data'''
    print 'loading......'
    try:
        file = open(DATAPATH, 'r')
    except:
        print 'failed'
        print 'opening backup'
        try:
            file = open(BACKUPPATH, 'r')
        except:
            print 'no data found'
            return 0
    todos = file.readlines()
    for todo in todos:
        load_todo(todo)
def load_todo(data):
    '''load todo'''
    datas = data.split(' ')
    new_todo = Todo()
    new_todo.name = datas[0]
    new_todo.state = datas[1]
    if new_todo.state == 'DONE':
        ALL_DONE[new_todo.name] = new_todo
    else:
        ALL_TODO[new_todo.name] = new_todo


def add():
    '''add todo'''
    new_todo = Todo()
    new_todo.add()
    choose2 = {}
    print MENU2
    ALL_TODO[new_todo.name] = new_todo

def input_choose1():
    '''
    input choose1
    '''
    choose = ['a', 'e', 'q']
    print START_MENU
    choose1 = msvcrt.getch()
    if not choose1 in choose:
        print 'input error'
        return input_choose1()
    return choose1
def input_choose_edit():
    '''input choose edit'''
    key = 'a'
    choise = []
    choose_edit = {}
    for todo in ALL_TODO:
        choose_edit[key] = todo
        choise.append(key)
        print key + ')', ALL_TODO[todo].show()
        key = chr(ord(key)+1)
    choose = msvcrt.getch()
    if not choose in choise:
        print 'input error'
        return input_choose_edit()
    return choose_edit, choose
def input_choose_action():
    '''input action'''
    print EDIT_MENU
    choise = ['d']
    choose = msvcrt.getch()
    if not choose in choise:
        print 'input error'
        return input_choose_action()
    return choose
def done(todo):
    '''done'''
    todo.done()
def edit():
    '''edit todo'''
    choose_edit, choose = input_choose_edit()
    edit_choise = {'d':done}
    edit_choise.get(input_choose_action())(ALL_TODO[choose_edit[choose]])
    '''todos = choose_edit.items()
    todos.sort()
    for todo in todos:
        print todo'''
    '''for key in choose_edit:
        print key + ')', choose_edit[key]'''
def show_all():
    '''show_all'''
    for todo in ALL_TODO:
        todo = ALL_TODO[todo]
        print '-->' + todo.show()
'''def show(todo):
    ''''''
    data = ''
    data += todo.name + ' '
    data += todo.state + ' '
    if todo.deadline.time:
        data += str(todo.deadline.time) + ' '
    else:
        data += '0 '
    if todo.startTime.time:
        data += str(todo.startTime.time) + ' '
    else:
        data += '0 '
    if todo.finishTime.time:
        data += str(todo.finishTime.time) + ' '
    else:
        data += '0 '
    if todo.cancelTime.time:
        data += str(todo.cancelTime.time) + ' '
    else:
        data += '0 '
    return data'''
def start():
    ''' start'''
    load_data()
    show_all()
    flag = 1
    while flag:
        choose1 = {'a':add, 'e':edit, 'q':end}
        choose = input_choose1()
        choose1.get(choose)()
def end():
    write_data()
    backup()
    quit()

if __name__ == '__main__':
    start()
