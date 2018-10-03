
# coding: utf-8

# In[19]:

from Crypto.Cipher import AES
import random
import string


# In[151]:

def create_key():
    key = ''
    for i in range(16):
        key += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    return key


# In[33]:

def check_key(key):
    f = open('keys.txt', 'r')
    for line in f:
        owner_name, owner_key = line.split()
        if (owner_key == key):
            f.close()
            return 'taken'
    f.close()
    return 'available'


# In[79]:

def check_availablity(pid):
    f = open('keys.txt', 'r')
    for line in f:
        owner_name, owner_key = line.split()
        if (owner_name == pid):
            f.close()
            return 'taken'
    f.close()
    return 'available'


# In[176]:

def get_key(pid):
    if (check_availablity(pid) == 'taken'):
        f = open('keys.txt', 'r')
        for line in f:
            owner_name, owner_key = line.split()
            if (owner_name == pid):
                f.close()
                return owner_key
        f.close
    else:        
        return None


# In[177]:

def register(pid):
    if (check_availablity(pid) == 'taken'):
        print 'Error: Patient ID taken'
    else:
        new_key = create_key()
        while (check_key(new_key) == 'taken' ):
            new_key = create_key()
            
        f = open('keys.txt', 'a')
        f.write(pid+' '+new_key+'\n')
        f.close()
        print 'Successfully Registered -', pid, ':', new_key


# In[222]:

def decode_data(data):
    pid = data[:3]
    encrypt_data = data[4:]
    key = get_key(pid)
    if (key is None):
        print 'Error: Patient ID Not Available'
        return None
    else:
        aes = AES.new(key)
        data = aes.decrypt(encrypt_data)
        return pid, key, data


# In[179]:

def clean():
    f = open('keys.txt', 'w')
    f.write('')
    f.close()


# In[238]:

def encode_data(pid, key, data):
    l = len(data)%16
    if (l > 0):
        data += ' '*(16-l)
    aes = AES.new(key)
    encrypted_data = aes.encrypt(data)
    return pid+' '+encrypted_data


# # PART 1 #

# In[241]:

clean()
register('P04')
register('P02')
register('P03')


# # PART 3 #

# In[279]:

data_received = 'P04 \xf1\xbb\xcb\x16\xa69\t,\xf3\xdf\x18\x94\x8b]\xa8{E\x87"\x8at\xb0\x07\x12\x07\xba>\xbax\x88S%'


# In[280]:

pid, key, data = decode_data(data_received)


# In[281]:

data


# # PART 4 #

# In[283]:

remark = "EAt medicine"


# In[284]:

data_to_send = encode_data(pid, key, remark)


# In[285]:

data_to_send


# In[ ]:



