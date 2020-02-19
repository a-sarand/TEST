import time

with open("log.txt","w") as f:
    t= time.asctime(time.localtime(time.time()))
    f.write("start up my program"+"\t"+ t+ "\n")

    time.sleep(4)

    t= time.asctime(time.localtime(time.time()))
    f.write("end of my program"+"\t"+ t)
