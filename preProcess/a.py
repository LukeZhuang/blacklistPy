import random as rand;
f1=open("dfp_in_shenlan_bla_ext.csv");
f2=open("dfp_not_in_shenlan_bla_ext.csv");
fo_1=open('datax.csv','w');
fo_2=open('datay.csv','w');
ones=[];
for line in f1:
	cols=line.split(',');
	ones.append((cols[0],cols[1],cols[2],'1'));
zeros=[];
for line in f2:
	cols=line.split(',');
	zeros.append((cols[0],cols[1],cols[2],'0'));
rand.shuffle(zeros);
zeros_new=[];
for x in range(1500):
	zeros_new.append(zeros[x]);
for tup in ones:
	print >> fo_1 , '%s,%s,%s' %(tup[0],tup[1],tup[2]);
	print >> fo_2 , tup[3];
for tup in zeros_new:
	print >> fo_1 , '%s,%s,%s' %(tup[0],tup[1],tup[2]);
	print >> fo_2 , tup[3];