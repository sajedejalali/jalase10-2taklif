class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
    
    def show():
        print(h, ":", m, ":", s)

    def t_to_s(self):
        h_s = int(self.h) * 3600
        m_s = int(self.m) * 60
        result = h_s + m_s + int(self.s)
        print(result)
    
    #def s_to_t(self):
        #result = Time(None, None, None)
        #result.h = s_h
        #result.m = s_m
        #result.s = s_s
        #return result

while True:
    print("1- time to s")
    print("2- s to time")
    print("0- exit")
    op = input("enter your choice : ")
    if op == "1":
        time_h = input("enter time h: ")
        time_m = input("enter time m: ")
        time_s = input("enter time s: ")
        time1 = Time(time_h, time_m, time_s)
        time1.t_to_s()

    if op == "2":
        op_s = int(input("enter s: "))
        s_h = 0
        s_m = 0
        s_s = 0
        while True:
            if op_s >= 60 :
                op_s -= 60
                s_m += 1
                if op_s < 60:
                    s_s = op_s
                    break
            if s_m >= 60:
                s_m -= 60
                s_h += 1
        #time = (s_h, ":", s_m, ":", s_s)
        print(s_h, ":", s_m, ":", s_s)
        
    if op == "0" : 
        break


