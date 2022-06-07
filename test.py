

g_msg = ["Hello", "GOOD DAY","this is working", "ghfh"]
g_msg_ip = ["192.168.1.312","192.168.1.145","192.168.1.143","192.168.1.12"]
g_recived_msg = [[],[],[],[]]
connected_devices = ["192.168.1.312"]




def remove_seen_msg():
    global g_msg
    global g_msg_ip
    global g_recived_msg
    i=0

    msg_ip_delete = []
    msg_delete = []


    ##deletes g_recived_msg and get locations to be deleted
    for x in g_recived_msg[:]:
        if len(x) == len(connected_devices):
            g_recived_msg.remove(x)
            msg_delete.append(g_msg[i])
            msg_ip_delete.append(g_msg_ip[i])
        i += 1
    ##deletes msg_ip_delete
    for x in msg_ip_delete[:]:
        g_msg_ip.remove(x)

    ##deletes msg_delete
    for x in msg_delete[:]:
        g_msg.remove(x)



def send_all(ip):
    i =0
    l_msg = g_msg[:]
    msg_delete = []

    ##finds messages for deletion
    for x in g_msg_ip[:]:
        ##mesages that user has sent them selfs they also get mark as seen
        if x == ip:
            msg_delete.append(l_msg[i])
            g_recived_msg[g_msg_ip.index(x)].append(ip)
        ##the messages the user has already seen
        elif ip in g_recived_msg[i]:
            msg_delete.append(l_msg[i])
        ##deletes 
        else:
            g_recived_msg[i].append(ip)

        i += 1
    ##deletes the messages
    for x in msg_delete:
        l_msg.remove(x)
    print(l_msg)

send_all("192.168.1.145")
remove_seen_msg()



