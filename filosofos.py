import random
import threading as hilos
import time as t

philosof = 5
total_time = 3

class Philosopher(hilos.Thread):

    count=0
    state = []
    forks = []
    traffic = hilos.Lock()

    #Main method | Start
    def __init__(self):
        super().__init__()      
        self.id=Philosopher.count 
        Philosopher.count+=1 
        Philosopher.state.append('PENSANDO') 
        Philosopher.forks.append(hilos.Semaphore(0)) 
        print("FILOSOFO #{0} - PENSANDO".format(self.id))

    def __del__(self):
        print("FILOSOFO #{0} - SE PARA DE LA MESA".format(self.id))  

    def think(self):
        t.sleep(random.randint(0,5)) #Random

    def right(self,i):
        return (i-1)%philosof 

    def left(self,i):
        return(i+1)%philosof 

    def validate(self,i):
        if Philosopher.state[i] == 'HAMBRIENTO' and Philosopher.state[self.left(i)] != 'COMIENDO' and Philosopher.state[self.right(i)] != 'COMIENDO':
            Philosopher.state[i]='COMIENDO'
            Philosopher.forks[i].release() 

    def take(self):
        Philosopher.traffic.acquire() 
        Philosopher.state[self.id] = 'HAMBRIENTO'
        self.validate(self.id) 
        Philosopher.traffic.release() 
        Philosopher.forks[self.id].acquire() 

    def drop(self):
        Philosopher.traffic.acquire() 
        Philosopher.state[self.id] = 'PENSANDO'
        self.validate(self.left(self.id))
        self.validate(self.right(self.id))
        Philosopher.traffic.release() 

    def eat(self):
        print("FILOSOFO #{} COMIENDO".format(self.id))
        t.sleep(2) 
        print("FILOSOFO #{} TERMINO DE COMER".format(self.id))

    #Call all methods
    def run(self):
        for i in range(total_time):
            self.think()
            self.take() 
            self.eat() 
            self.drop() 

def main():
    lista=[]
    for i in range(philosof):
        lista.append(Philosopher()) 

    for f in lista:
        f.start() 

    for f in lista:
        f.join() #Block Thread

#start app
main()
