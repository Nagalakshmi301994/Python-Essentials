#!/usr/bin/env python
# coding: utf-8

# # List and its default functions

# In[1]:


list1 = ['physics', 'chemistry', 1997, 2000];


# In[2]:


list2 = [1, 2, 3, 4, 5 ];


# In[3]:


list3 = ["a", "b", "c", "d"]


# In[9]:


print(list1[0])


# In[11]:


print(list2[2])


# In[13]:


print(list1)


# In[14]:


del list1[2];


# In[15]:


print(list1)


# In[16]:


['Hi!'] * 4


# In[17]:


len([1, 2, 3])


# In[18]:


[1, 2, 3] + [4, 5, 6]


# In[19]:


3 in [1, 2, 3]


# In[21]:


L = ['spam', 'Spam', 'SPAM!']


# In[22]:


L[2]


# In[23]:


L[-2]


# In[24]:


L[1:]


# In[35]:


list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']


# In[37]:


print("First list length : ", len(list1))


# In[39]:


print("Second list length : ", len(list2))


# In[51]:


list1, list2 = ['xyz', 'zara', 'abc'], [456, 123]


# In[48]:


max(list1)


# In[52]:


max(list2)


# In[53]:


min(list1)


# In[54]:


min(list2)


# In[55]:


aTuple = (123, 'xyz', 'zara', 'abc');


# In[56]:


aList = list(aTuple)


# In[57]:


aList


# In[58]:


aList = [123, 'xyz', 'zara', 'abc'];


# In[59]:


aList.append( 2009 );


# In[60]:


aList


# In[61]:


aList = [123, 'xyz', 'zara', 'abc', 123];


# In[62]:


aList.count(123)


# In[63]:


aList.count('zara')


# In[1]:


aList = [123, 'xyz', 'zara', 'abc', 123];


# In[2]:


bList = [2009, 'manni'];


# In[3]:


aList.extend(bList)


# In[4]:


aList


# In[5]:


aList = [123, 'xyz', 'zara', 'abc'];


# In[6]:


aList.index( 'xyz' ) 


# In[7]:


aList.index( 'zara' ) 


# In[8]:


aList = [123, 'xyz', 'zara', 'abc']


# In[9]:


aList.insert( 3, 2009)


# In[10]:


aList


# In[11]:


aList = [123, 'xyz', 'zara', 'abc'];


# In[12]:


aList.pop()


# In[13]:


aList.pop(2)


# In[14]:


aList = [123, 'xyz', 'zara', 'abc', 'xyz'];


# In[15]:


aList.remove('xyz');


# In[16]:


aList


# In[17]:


aList.remove('abc');


# In[18]:


aList


# In[19]:


aList = [123, 'xyz', 'zara', 'abc', 'xyz'];


# In[20]:


aList.reverse();


# In[21]:


aList


# In[25]:


aList = ['xyz', 'zara', 'abc', 'xyz'];


# In[23]:


aList


# In[26]:


aList.sort();


# In[27]:


aList


# # Dictionary and its default functions

# In[29]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}


# In[30]:


dict['Name']


# In[31]:


dict['Age']


# In[32]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}


# In[36]:


dict['Age'] = 8; 


# In[37]:


dict['School'] = "DPS School";


# In[38]:


dict['Age']


# In[39]:


dict['School']


# In[40]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}


# In[41]:


del dict['Name'];


# In[42]:


dict.clear();


# In[43]:


del dict ; 


# In[47]:


dict


# In[48]:


dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}


# In[49]:


dict['Name']


# In[52]:


dict1 = {'Name': 'Zara', 'Age': 7};


# In[54]:


len (dict)


# In[55]:


str (dict1)


# In[58]:


dict = {'Name': 'Zara', 'Age': 7};


# In[59]:


type (dict)


# In[60]:


dict = {'Name': 'Zara', 'Age': 7};


# In[61]:


len(dict)


# In[62]:


dict.clear()


# In[63]:


len(dict)


# In[64]:


dict1 = {'Name': 'Zara', 'Age': 7};


# In[66]:


dict2 = dict1.copy()


# In[67]:


str(dict2)


# In[68]:


seq = ('name', 'age', 'sex')


# In[69]:


dict = dict.fromkeys(seq)


# In[70]:


str(dict)


# In[71]:


dict = dict.fromkeys(seq, 10)


# In[72]:


str(dict)


# In[74]:


dict = {'Name': 'Zabra', 'Age': 7}


# In[75]:


dict.get('Age')


# In[76]:


dict.get('Education', "Never")


# In[83]:


dict = {'Name': 'Zara', 'Age': 7}


# In[86]:


dict.items()


# In[87]:


dict = {'Name': 'Zara', 'Age': 7}


# In[88]:


dict.keys()


# In[89]:


dict = {'Name': 'Zara', 'Age': 7}


# In[90]:


dict.setdefault('Age', None)


# In[92]:


dict.setdefault('Sex', None)


# In[93]:


dict = {'Name': 'Zara', 'Age': 7}


# In[94]:


dict2 = {'Sex': 'female' }


# In[95]:


dict.update(dict2)


# In[96]:


dict


# In[97]:


dict = {'Name': 'Zara', 'Age': 7}


# In[98]:


dict.values()


# # sets and its default functions

# In[100]:


my_set = {1, 2, 3}


# In[101]:


print(my_set)


# In[102]:


my_set = {1.0, "Hello", (1, 2, 3)}


# In[103]:


print(my_set)


# In[104]:


my_set = set([1, 2, 3, 2])


# In[105]:


print(my_set)


# In[107]:


my_set = {1, 2, 3, 4, 3, 2}


# In[108]:


print(my_set)


# In[109]:


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])


# In[110]:


Months={"Jan","Feb","Mar"}


# In[111]:


Dates={21,22,17}


# In[112]:


print(Days)


# In[113]:


print(Months)


# In[114]:


print(Dates)


# In[115]:


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])


# In[118]:


print(Days)


# In[119]:


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])


# In[120]:


Days.add("Sun")


# In[121]:


print(Days)


# In[122]:


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])


# In[123]:


Days.discard("Sun")


# In[124]:


print(Days)


# In[125]:


DaysA = set(["Mon","Tue","Wed"])


# In[128]:


DaysB = set(["Wed","Thu","Fri","Sat","Sun"])


# In[130]:


AllDays = DaysA|DaysB


# In[131]:


print(AllDays)


# In[132]:


DaysA = set(["Mon","Tue","Wed"])


# In[133]:


DaysB = set(["Wed","Thu","Fri","Sat","Sun"])


# In[134]:


AllDays = DaysA & DaysB


# In[136]:


print(AllDays)


# In[137]:


DaysA = set(["Mon","Tue","Wed"])


# In[138]:


DaysB = set(["Wed","Thu","Fri","Sat","Sun"])


# In[139]:


AllDays = DaysA - DaysB


# In[140]:


print(AllDays)


# In[141]:


DaysA = set(["Mon","Tue","Wed"])


# In[142]:


DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])


# In[143]:


SubsetRes = DaysA <= DaysB


# In[144]:


SupersetRes = DaysB >= DaysA


# In[145]:


print(SubsetRes)


# In[146]:


print(SupersetRes)


# In[147]:


my_set = {1, 3, 4, 5, 6}


# In[148]:


my_set.discard(4)


# In[149]:


print(my_set)


# # Tuple and explore default methods

# In[150]:


tup1 = ('physics', 'chemistry', 1997, 2000);


# In[151]:


tup2 = (1, 2, 3, 4, 5 );


# In[152]:


tup3 = "a", "b", "c", "d";


# In[153]:


tup1 = ();


# In[154]:


tup1 = (50,);


# In[157]:


print(tup1[0]);


# In[158]:


print(tup2[1:5]);


# In[159]:


tup1 = (12, 34.56);


# In[160]:


tup2 = ('abc', 'xyz');


# In[162]:


tup3 = tup1 + tup2;


# In[164]:


print(tup3);


# In[165]:


tup = ('physics', 'chemistry', 1997, 2000);


# In[167]:


print(tup);


# In[168]:


del tup;


# In[174]:


tup = ('physics', 'chemistry', 1997, 2000);


# In[176]:


len((1, 2, 3))


# In[177]:


(1, 2, 3) + (4, 5, 6)


# In[178]:


3 in (1, 2, 3)


# In[182]:


('Hi!',) * 4


# In[183]:


L = ('spam', 'Spam', 'SPAM!')


# In[184]:


L[2]


# In[185]:


L[-2]


# In[186]:


L[1:]


# In[188]:


print('abc', -4.24e93, 18+6.6j, 'xyz');


# In[189]:


x, y = 1, 2;


# In[190]:


print(x,y)


# In[195]:


tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')


# In[196]:


len(tuple1)


# In[197]:


len(tuple2)


# In[201]:


tuple1, tuple2 = ('xyz', 'zara', 'abc'), (456, 700, 200)


# In[202]:


max(tuple1)


# In[203]:


max(tuple2)


# In[204]:


min(tuple1)


# In[205]:


min(tuple2)


# In[206]:


aList = [123, 'xyz', 'zara', 'abc']


# In[207]:


aTuple = tuple(aList)


# In[208]:


print(aTuple)


# # Strings and explore default methods

# In[209]:


var1 = 'Hello World!'


# In[210]:


var2 = "Python Programming"


# In[211]:


print(var1[0])


# In[212]:


print(var2[1:5])


# In[213]:


var1 = 'Hello World!'


# In[214]:


print(var1[:6] + 'Python')


# In[215]:


print("My name is %s and weight is %d kg!" % ('Zara', 21))


# In[216]:


para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""


# In[218]:


print(para_str)


# In[219]:


print('C:\\nowhere')


# In[222]:


print(r'C:\\nowhere')


# In[223]:


print(u'Hello, world!')


# In[224]:


str = "this is string example....wow!!!";


# In[225]:


print("str.capitalize() : ", str.capitalize())


# In[226]:


str = "this is string example....wow!!!"


# In[227]:


print("str.center(40, 'a') : ", str.center(40, 'a'))


# In[228]:


str = "this is string example....wow!!!";


# In[229]:


sub = "i";


# In[230]:


print("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))


# In[231]:


sub = "wow";


# In[233]:


print("str.count(sub) : ", str.count(sub))


# In[246]:


str = "this is string example....wow!!!";


# In[247]:


suffix = "wow!!!";


# In[248]:


str.endswith(suffix)


# In[249]:


str.endswith(suffix,20)


# In[250]:


suffix = "is";


# In[251]:


str.endswith(suffix, 2, 4)


# In[252]:


str.endswith(suffix, 2, 6)


# In[253]:


str = "this is\tstring example....wow!!!";


# In[254]:


str


# In[255]:


str.expandtabs()


# In[256]:


str.expandtabs(16)


# In[257]:


str1 = "this is string example....wow!!!";


# In[258]:


str2 = "exam";


# In[259]:


str1.find(str2)


# In[260]:


str1.find(str2, 10)


# In[261]:


str1.find(str2, 40)


# In[262]:


str1.index(str2)


# In[263]:


str1.index(str2, 10)


# In[264]:


str = "this2009";


# In[265]:


str.isalnum()


# In[266]:


str = "this is string example....wow!!!";


# In[267]:


str.isalnum()


# In[268]:


str = "this";


# In[269]:


str.isalpha()


# In[270]:


str = "this is string example....wow!!!";


# In[272]:


str.isalpha()


# In[273]:


str = "123456";


# In[274]:


str.isdigit()


# In[275]:


str = "this is string example....wow!!!";


# In[276]:


str.isdigit()


# In[277]:


str.islower()


# In[278]:


str = "THIS is string example....wow!!!"; 


# In[279]:


str.islower()


# In[280]:


str = u"this2009";  


# In[281]:


str = u"23443434";


# In[282]:


str.isnumeric()


# In[283]:


str = u"this2009";  


# In[284]:


str.isnumeric()


# In[285]:


str = "       "; 


# In[286]:


str.isspace()


# In[287]:


str = "This is string example....wow!!!";


# In[288]:


str.isspace()


# In[289]:


str = "This Is String Example...Wow!!!";


# In[290]:


str.istitle()


# In[291]:


str = "This is string example....wow!!!";


# In[292]:


str.istitle()


# In[293]:


str = "THIS IS STRING EXAMPLE....WOW!!!"; 


# In[294]:


str.isupper()


# In[295]:


str = "THIS is string example....wow!!!";


# In[296]:


str.isupper()


# In[297]:


s = "-";


# In[298]:


seq = ("a", "b", "c");


# In[299]:


s.join( seq )


# In[300]:


str = "this is string example....wow!!!";


# In[301]:


len(str)


# In[302]:


str.ljust(50, '0')


# In[303]:


str = "THIS IS STRING EXAMPLE....WOW!!!";


# In[304]:


str.lower()


# In[305]:


str = "     this is string example....wow!!!     ";


# In[306]:


str.lstrip()


# In[307]:


str = "88888888this is string example....wow!!!8888888";


# In[308]:


str.lstrip()


# In[309]:


str.lstrip('8')


# In[317]:


str = "this is really a string example....wow!!!";


# In[318]:


max(str)


# In[320]:


str = "this is a string example....wow!!!";


# In[321]:


max(str)


# In[322]:


min(str)


# In[323]:


min(str)


# In[324]:


str = "this-is-a-string-example....wow!!!";


# In[325]:


min(str)


# In[326]:


str = "this is string example....wow!!! this is really string"


# In[327]:


str.replace("is", "was")


# In[328]:


str.replace("is", "was", 3)


# In[329]:


str1 = "this is really a string example....wow!!!";


# In[330]:


str2 = "is";


# In[331]:


str1.rfind(str2)


# In[332]:


str1.rfind(str2, 0, 10)


# In[333]:


str1.rfind(str2, 10, 0)


# In[334]:


str1.find(str2)


# In[335]:


str1.find(str2, 0, 10)


# In[336]:


str1.find(str2, 10, 0)


# In[337]:


str1 = "this is string example....wow!!!";


# In[338]:


str2 = "is";


# In[339]:


str1.rindex(str2)


# In[340]:


str1.index(str2)


# In[341]:


str = "this is string example....wow!!!";


# In[342]:


str.rjust(50, '0')


# In[343]:


str = "     this is string example....wow!!!     ";


# In[344]:


str.rstrip()


# In[345]:


str = "88888888this is string example....wow!!!8888888";


# In[346]:


str.rstrip('8')


# In[347]:


str = "Line1-abcdef \nLine2-abc \nLine4-abcd";


# In[348]:


str.split( )


# In[349]:


str.split(' ', 1 )


# In[350]:


str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";


# In[351]:


str.splitlines( )


# In[352]:


str.splitlines( 0 )


# In[353]:


str.splitlines( 3 )


# In[354]:


str.splitlines( 4 )


# In[355]:


str.splitlines( 5 )


# In[357]:


str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";


# In[359]:


str.splitlines(True)


# In[360]:


str.splitlines( 0 )


# In[361]:


str.splitlines( 3 )


# In[362]:


str.splitlines( 4 )


# In[366]:


str.splitlines( 5 )


# In[367]:


str = "this is string example....wow!!!";


# In[368]:


str.startswith( 'this' )


# In[369]:


str.startswith( 'is', 2, 4 )


# In[370]:


str.startswith( 'this', 2, 4 )


# In[371]:


str = "0000000this is string example....wow!!!0000000";


# In[373]:


str.strip( '0' )


# In[374]:


str = "this is string example....wow!!!";


# In[375]:


str.swapcase()


# In[376]:


str = "THIS IS STRING EXAMPLE....WOW!!!";


# In[377]:


str.swapcase()


# In[379]:


str = "this is string exampl....wow!!!";


# In[380]:


str.title()


# In[381]:


str = "this is string example....wow!!!";


# In[382]:


str.upper()


# In[383]:


str = "this is string example....wow!!!";


# In[384]:


str.zfill(40)


# In[385]:


str.zfill(50)


# In[386]:


str = u"this2009";  


# In[387]:


str.isdecimal();


# In[388]:


str = u"23443434";


# In[390]:


str.isdecimal();


# In[391]:


print(str)


# In[392]:


str = u"this2009";  


# In[393]:


str.isdecimal();


# In[394]:


print(str)


# In[ ]:




