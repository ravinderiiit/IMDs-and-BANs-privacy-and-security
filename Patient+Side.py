
# coding: utf-8

# In[71]:

from Crypto.Cipher import AES
import random
import string


# In[72]:

def read_data():
    data = ''
    for i in range(32):
        data += random.choice(string.digits)
    return data


# In[101]:

def decode_data(pid, data):
    p = data[:3]
    encrypt_data = data[4:]
    if (p == pid):
        decoded_data = aes.decrypt(encrypt_data)
        return decoded_data
    else:
        return 'Error'


# In[113]:

pid = 'P04'
key = 'BAOMNloGR3Az9Bju'


# In[114]:

aes = AES.new(key)


# # PART 2 #

# In[115]:

data = read_data()


# In[116]:

encrypted_data = aes.encrypt(data)


# In[117]:

data_to_send = pid + ' ' + encrypted_data


# In[118]:

print data


# In[133]:

data_to_send


# # PART 5 #

# In[146]:

data_received = 'P04 \xb1\xbd\x8e\x9bM\x1a4~V\xa5\xc7\x92\x93\x1f5B'


# In[147]:

data = decode_data(pid, data_received)


# In[148]:

data


# In[ ]:



