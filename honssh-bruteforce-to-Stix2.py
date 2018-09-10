from stix2 import UserAccount,ObservedData,IPv4Address,MemorySink,CustomObservable



def user_account_observable(timestamp,ip,id,passwors,success):
    usr=UserAccount(user_id=id)

    source = IPv4Address(value=ip)
    dict = {"Password":passwors,"src_ip_ref":"0","success":success}
    obs = ObservedData(first_observed=timestamp,
                       last_observed=timestamp,
                       number_observed=1,
                       objects={"0": source,"1":usr },
                       custom_properties=dict
                       )
    wrt.add(obs)

file = open('X:hon_log.txt', 'r')

wrt = MemorySink()

for line in file:
    a = line.split(',')
    b=str(a[0])
    b=b.replace('_','')
    c=b[:4]+'-'+b[4:6]+'-'+b[6:8]+'T'+b[8:10]+':'+b[10:12]+':'+b[12:14]+'.'+b[14:]+'Z'
    user_account_observable(c, a[1], a[2], a[3], a[4])

wrt.save_to_file('X:honssh_to_stix2.json')
