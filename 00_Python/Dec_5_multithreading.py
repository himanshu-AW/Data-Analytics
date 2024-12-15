import threading,time
def paratha_making():
    print("Starting to make paratha...")
    time.sleep(3)
    print("Paratha baked successfully!")

def tea_making():
    print("Starting to make tea...")
    time.sleep(5)
    print("Tea brewed successfully!")

def eat_pani_puri():
    print("Starting to eat pani poori...")
    time.sleep(2)
    print("Pani puri enjoyed!")

begintime=time.time()   
paratha_making1 = threading.Thread(target=paratha_making)
tea_making1 = threading.Thread(target=tea_making)

paratha_making1.start()
tea_making1.start()
paratha_making1.join()
tea_making1.join()
print("The total time taken:",time.time()-begintime)
print("Both task has done.")