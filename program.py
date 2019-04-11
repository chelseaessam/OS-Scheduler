import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import  QMainWindow,QApplication, QComboBox, QDialog,QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,QVBoxLayout,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import pyqtSlot
import matplotlib.pyplot as plt
import numpy as np
import linked_list
import index
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Program")
        #self.setWindowIcon(QtGui.QIcon("download.jpg"))
        self.setGeometry(50,50,500,300)
        self.home()
        self.show()
       
    def home(self):
       
        
        self.label2=QLabel(self)
        self.label2.setText("Type of Scheduler")
        self.label2.move(10,50)

        #self.textbox2=QLineEdit(self)
        #self.textbox2.move(100,50)
        self.comboBox=QComboBox(self)
        self.comboBox.addItem("FCFS")
        self.comboBox.addItem("SJF")
        self.comboBox.addItem("SJF Preemptive")
        self.comboBox.addItem("Priority")
        self.comboBox.addItem("Priority Preemptive")
        self.comboBox.addItem("RR")
        self.comboBox.move(100,50)
       
        self.button=QPushButton("Go",self)
        self.button.move(0,200)
        self.button.clicked.connect(self.runcode)
        
    def runcode(self):
      schedular_type=str(self.comboBox.currentText())
      if(schedular_type=="FCFS"):
       self.close()
       self.fcfs=Window2(self)
      elif(schedular_type=="RR"):
       self.close()
       self.rr=Window3(self)
      elif(schedular_type=="SJF"):
       self.close()
       self.sjf=Window4(self)
      elif(schedular_type=="Priority"):
       self.close()
       self.pr=Window5(self)
      elif(schedular_type=="SJF Preemptive"):
       self.close()
       self.sjfp=Window6(self)
      elif(schedular_type=="Priority Preemptive"):
       self.close()
       self.pp=Window7(self)


class Window3(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Round Robin")
        #self.setWindowIcon(QtGui.QIcon("download.jpg"))
        self.setGeometry(50,50,500,300)
        self.home()
        self.show()
       
    def home(self):
        
        self.label1=QLabel(self)
        self.label1.setText("No of Processes")
        self.label1.move(10,0) #col ,row

        self.label3=QLabel(self)
        self.label3.setText("Processess Names")
        self.label3.move(10,50)

        self.label4=QLabel(self)
        self.label4.setText("Burst Time")
        self.label4.move(10,100)

        self.label6=QLabel(self)
        self.label6.setText("Arrival Time")
        self.label6.move(10,150)

        self.label5=QLabel(self)
        self.label5.setText("Quantum")
        self.label5.move(10,200)

        
        self.textbox=QLineEdit(self)
        self.textbox.move(100,0)

        self.names=QLineEdit(self)
        self.names.move(100,50)
        self.names.resize(1700,30)

        self.burst=QLineEdit(self)
        self.burst.move(100,100)
        self.burst.resize(1700,30)

        self.quantum=QLineEdit(self)
        self.quantum.move(100 ,200)
        
        
        #self.textEdit=QTextEdit(self)
        #self.textEdit.move(20,250)
       
        
        self.arrival_time=QLineEdit(self)
        self.arrival_time.move(100,150)
        self.arrival_time.resize(1400,30)
        
        
        self.button=QPushButton("Go",self)
        self.button.move(0,250)
        self.button.clicked.connect(self.runcode)

        self.back=QPushButton("Back",self)
        self.back.move(100,250)
        self.back.clicked.connect(self.main)
    def main(self):
        self.close()
        self.main=MainWindow(self)
            
    def runcode(self):
      
      
      no_of_process=self.textbox.text()
      process_names=self.names.text()
      burst_time=self.burst.text()
      arrival_time=self.arrival_time.text()
      quantum=self.quantum.text()
      
      names_list=process_names.split()
      burst_list=burst_time.split()
      arrival_list=arrival_time.split()
      
  

      #integer conversion
      
      burst_list=[float(i) for i in burst_list]
      arrival_list=[float(i) for i in arrival_list]
      no_of_process=int(no_of_process)
      quantum=int(quantum)
      ls=linked_list.LinkedList()
      i=0
      while i<no_of_process:
              ls.append(names_list[i],burst_list[i],arrival_list[i])
              i=i+1
      ls.bubble_sort_time()
         
      time=ls.getHead().getarrivaltime()
      j=0
      start=[]
      end=[]
      name=[]
      dep=[]
      while j<no_of_process:
              dep.append(0)
              j=j+1
      temp=linked_list.LinkedList()
      i=0
      while ((ls.size())!=0 or (temp.size())!=0):
              head=ls.getHead()
              while head is not None:
                  if(head.getarrivaltime()<=time or head.getarrivaltime()<=time+quantum ):
                     temp.append(head.getname(),head.getbursttime(),head.getarrivaltime())
                     #temp.swap_head_and_tail()
                     ls.remove(head.getname())
                  head=head.getNext()
                  
              if(temp.size()!=0):
                  
                  start.append(time)
                  head2=temp.getHead()
                  remaining=head2.getbursttime()
                  if(remaining>quantum or remaining==quantum):
                      time=time+quantum
                      head2.setbursttime(remaining-quantum)
                      
                  else:
                      time=time+remaining
                      head2.setbursttime(0)
                      
                    
                  end.append(time)
                  name.append(head2.getname())
                  if(head2.getbursttime()==0):
                      myname=head2.getname()
                      dep[index.index(names_list,myname)]=time
                      
                      temp.remove(head2.getname())
                      
                  else:
                     temp.swap_head_and_tail()
                      
              else:
                  time=time+1
              i=i+1
             
      k=0
      waiting=0
      while(k<no_of_process):
              waiting=waiting+dep[k]-arrival_list[k]-burst_list[k]
              k=k+1
      average_waiting=waiting/no_of_process
      
      x=name
      begin = np.array(start)
      end =   np.array(end)
      plt.barh(range(len(begin)),  end-begin, left=begin)
      plt.yticks(range(len(begin)),x)
      #plt.text(0.6,1.5,('average waiting is ',average_waiting))
      #plt.annotate(("average waiting is",average_waiting),xy=(0.5,1.49))
      plt.title(('average waiting is ',average_waiting))
      plt.show() 
        
          
        
          
          
          


       
       
class Window2(QMainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("FCFS")
        #self.setWindowIcon(QtGui.QIcon("download.jpg"))
        self.setGeometry(50,50,500,300)
        #self.average_waiting=average_waiting
        self.home()
        self.show()
       
    def home(self):
        self.label1=QLabel(self)
        self.label1.setText("No of Processes")
        self.label1.move(10,0) #col ,row
        
        self.textbox=QLineEdit(self)
        self.textbox.move(100,0)
     
        
        self.label3=QLabel(self)
        self.label3.setText("Processess Names")
        self.label3.move(10,50)

        self.label4=QLabel(self)
        self.label4.setText("Burst Time")
        self.label4.move(10,100)

        self.label5=QLabel(self)
        self.label5.setText("Arrival Time")
        self.label5.move(10,150)

        self.names=QLineEdit(self)
        self.names.move(100,50)
        self.names.resize(1400,30)

        self.burst=QLineEdit(self)
        self.burst.move(100,100)
        self.burst.resize(1400,30)

        self.arrival=QLineEdit(self)
        self.arrival.move(100 ,150)
        self.arrival.resize(1400,30)
        #self.textEdit=QTextEdit(self)
        #self.textEdit.move(20,250)
##        self.label6=QLabel(self)
##        self.label6.setText("Waiting Time=",self.average_waiting)
##        self.label6.move(0,250)
##        
        
        self.button=QPushButton("Go",self)
        self.button.move(0,200)
        self.button.clicked.connect(self.fcfs)
        self.back=QPushButton("Back",self)
        self.back.move(100,200)
        self.back.clicked.connect(self.main)
    def main(self):
        self.close()
        self.main=MainWindow(self)
        
    def fcfs(self):
      
      no_of_process=self.textbox.text()
      process_names=self.names.text()
      burst_time=self.burst.text()
      arrival_time=self.arrival.text()
      
      names_list=process_names.split()
      burst_list=burst_time.split()
      arrival_list=arrival_time.split()
     

      #integer conversion
      
      burst_list=[float(i) for i in burst_list]
      arrival_list=[float(i) for i in arrival_list]
      no_of_process=int(no_of_process)
      
 
      
     
      
      ls=linked_list.LinkedList()
      i=0

      while i<no_of_process:
              ls.append(names_list[i],burst_list[i],arrival_list[i])
              i=i+1
      
      ls.bubble_sort_time()
      print("sorted")
      time=ls.getHead().getarrivaltime()
      j=0
      start=[]
      end=[]
      name=[]
      while j<(ls.size()):
        while(time<arrival_list[j]):
            time=time+1
                
        start.append(time)
        time=time+burst_list[j]
        end.append(time)
        name.append(names_list[j])
        j=j+1
      waiting_time=0
      k=0
      #average_waiting=0
      while k<(ls.size()):
             waiting_time=waiting_time+end[k]-arrival_list[k]-burst_list[k]
             average_waiting=waiting_time/ls.size()
             k=k+1
      #print("avd",average_waiting)   
      x=name
      begin = np.array(start)
      end =   np.array(end)
      plt.barh(range(len(begin)),  end-begin, left=begin)
      plt.yticks(range(len(begin)),x)
      plt.title(('average waiting is ',average_waiting))
      #plt.annotate(("average waiting is",average_waiting),xy=(0.5,1.49))
      plt.show()
################################SJF###############################################################################

class Window4(QMainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("SJF")
        #self.setWindowIcon(QtGui.QIcon("download.jpg"))
        self.setGeometry(50,50,500,300)
        self.home()
        self.show()
       
    def home(self):
        
        self.label1=QLabel(self)
        self.label1.setText("No of Processes")
        self.label1.move(10,0) #col ,row
        
        self.textbox=QLineEdit(self)
        self.textbox.move(100,0)
     
        self.label3=QLabel(self)
        self.label3.setText("Processess Names")
        self.label3.move(10,50)

        self.label4=QLabel(self)
        self.label4.setText("Burst Time")
        self.label4.move(10,100)

        self.label5=QLabel(self)
        self.label5.setText("Arrival Time")
        self.label5.move(10,150)

        self.names=QLineEdit(self)
        self.names.move(100,50)
        self.names.resize(1400,30)

        self.burst=QLineEdit(self)
        self.burst.move(100,100)
        self.burst.resize(1400,30)

        self.arrival=QLineEdit(self)
        self.arrival.move(100 ,150)
        self.arrival.resize(1400,30)
        #self.textEdit=QTextEdit(self)
        #self.textEdit.move(20,250)
        
        
        
        self.button=QPushButton("Go",self)
        self.button.move(0,200)
        self.button.clicked.connect(self.runcode)
        self.back=QPushButton("Back",self)
        self.back.move(100,200)
        self.back.clicked.connect(self.main)
    def main(self):
        self.close()
        self.main=MainWindow(self)
        
    def runcode(self):
      
      
      no_of_process=self.textbox.text()
      process_names=self.names.text()
      burst_time=self.burst.text()
      arrival_time=self.arrival.text()
     
      names_list=process_names.split()
      burst_list=burst_time.split()
      arrival_list=arrival_time.split()
  

      #integer conversion
      burst_list=[float(i) for i in burst_list]
      arrival_list=[float(i) for i in arrival_list]
      no_of_process=int(no_of_process)
      
      ls=linked_list.LinkedList()
      
      i=0
      while i<no_of_process:
              ls.append(names_list[i],burst_list[i],arrival_list[i])
              i=i+1         
      ls.bubble_sort_time()
      time=ls.getHead().getarrivaltime()
      j=0
      start=[]
      end=[]
      name=[]
      dep=[]
      while j<no_of_process:
          dep.append(0)
          j=j+1
      #start.append(time)
      #time=time+burst_list[0]
      #end.append(time)
      #name.append(names_list[0])
      #dep[0]=time
      #ls.remove(ls.getHead().getname())
      temp=linked_list.LinkedList()
      while ls.size()!=0:
          head=ls.getHead()
          #if(temp.size()==0):
          while head is not None:
               if(head.getarrivaltime()<=time):
                   temp.append(head.getname(),head.getbursttime(),head.getarrivaltime())
               
               head=head.getNext()
          temp.bubble_sort()
          if(temp.size()!=0):
              
              start.append(time)
              time=time+temp.getHead().getbursttime()
              end.append(time)
              name.append(temp.getHead().getname())
              dep[index.index(names_list,temp.getHead().getname())]=time
              ls.remove(temp.getHead().getname())
              temp.remove(temp.getHead().getname())
          else:
              time=time+1
      k=0
      waiting=0
      while k<no_of_process:
          waiting=waiting+dep[k]-arrival_list[k]-burst_list[k]
          k=k+1
      average_waiting=waiting/no_of_process    
      x=name
      begin = np.array(start)
      end =   np.array(end)
      plt.barh(range(len(begin)),  end-begin, left=begin)
      plt.yticks(range(len(begin)),x)
      #plt.text(0.6,1.5,('average waiting is ',average_waiting))
      #plt.annotate(("average waiting is",average_waiting),xy=(0.5,1.49))
      plt.title(('average waiting is ',average_waiting))

      plt.show()

#####################priority#########################################################


class Window5(QMainWindow):
   
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Priority")
        #self.setWindowIcon(QtGui.QIcon("download.jpg"))
        self.setGeometry(50,50,500,300)
        self.home()
        self.show()
       
    def home(self):
        
        self.label1=QLabel(self)
        self.label1.setText("No of Processes")
        self.label1.move(10,0) #col ,row
        
        self.textbox=QLineEdit(self)
        self.textbox.move(100,0)
     
        self.label3=QLabel(self)
        self.label3.setText("Processess Names")
        self.label3.move(10,50)

        self.label4=QLabel(self)
        self.label4.setText("Burst Time")
        self.label4.move(10,100)

        self.label5=QLabel(self)
        self.label5.setText("Arrival Time")
        self.label5.move(10,150)

        self.names=QLineEdit(self)
        self.names.move(100,50)
        self.names.resize(1400,30)

        self.burst=QLineEdit(self)
        self.burst.move(100,100)
        self.burst.resize(1400,30)

        self.arrival=QLineEdit(self)
        self.arrival.move(100 ,150)
        self.arrival.resize(1400,30)
        #self.textEdit=QTextEdit(self)
        #self.textEdit.move(20,250)
        self.label6=QLabel(self)
        self.label6.setText("Priority no")
        self.label6.move(10,200)

        self.priority=QLineEdit(self)
        self.priority.move(100,200)
        self.priority.resize(1400,30)
        
        
        self.button=QPushButton("Go",self)
        self.button.move(0,250)
        self.button.clicked.connect(self.runcode)
        self.back=QPushButton("Back",self)
        self.back.move(100,250)
        self.back.clicked.connect(self.main)
    def main(self):
        self.close()
        self.main=MainWindow(self)
    def runcode(self):
      
      
      no_of_process=self.textbox.text()
      process_names=self.names.text()
      burst_time=self.burst.text()
      arrival_time=self.arrival.text()
      priority=self.priority.text()
     
      
      names_list=process_names.split()
      burst_list=burst_time.split()
      arrival_list=arrival_time.split()
      priority_list=priority.split()
  

      #integer conversion
     
      burst_list=[float(i) for i in burst_list]
      arrival_list=[float(i) for i in arrival_list]
      no_of_process=int(no_of_process)
      priority_list=[int(i) for i in priority_list]
      
      ls=linked_list.LinkedList()
      
      i=0
      while i<no_of_process:
              ls.append3(names_list[i],burst_list[i],arrival_list[i],priority_list[i])
              i=i+1
      ls.bubble_sort_time2()       
      time=ls.getHead().getarrivaltime()
      j=0
      start=[]
      end=[]
      name=[]
      dep=[]
      while j<no_of_process:
          dep.append(0)
          j=j+1
     
      temp=linked_list.LinkedList()
      while ls.size()!=0:
          
          head=ls.getHead()
          #if(temp.size()==0):
          #print("time",time)
          while head is not None:
               
               if(head.getarrivaltime()<=time):
                   temp.append3(head.getname(),head.getbursttime(),head.getarrivaltime(),head.getpriority())
                   
               
               head=head.getNext()
          temp.bubble_sort_p()
          #print("D")
          temp.printList2()
          if(temp.size()!=0):
              
              start.append(time)
              time=time+temp.getHead().getbursttime()
              end.append(time)
              name.append(temp.getHead().getname())
              dep[index.index(names_list,temp.getHead().getname())]=time
              ls.remove(temp.getHead().getname())
              temp.remove(temp.getHead().getname())
          else:
              time=time+1
      k=0
      waiting=0
      while k<no_of_process:
          waiting=waiting+dep[k]-arrival_list[k]-burst_list[k]
          k=k+1
      average_waiting=waiting/no_of_process    
      x=name
      begin = np.array(start)
      end =   np.array(end)
      plt.barh(range(len(begin)),  end-begin, left=begin)
      plt.yticks(range(len(begin)),x)
      #plt.text(0.6,1.5,('average waiting is ',average_waiting))
      #plt.annotate(("average waiting is",average_waiting),xy=(0.5,1.49))
      plt.title(('average waiting is ',average_waiting))

      plt.show()
##################SJFP##########################################################################################
class Window6(QMainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("SJFP")
        #self.setWindowIcon(QtGui.QIcon("download.jpg"))
        self.setGeometry(50,50,500,300)
        self.home()
        self.show()
       
    def home(self):
        
        self.label1=QLabel(self)
        self.label1.setText("No of Processes")
        self.label1.move(10,0) #col ,row
        
        self.textbox=QLineEdit(self)
        self.textbox.move(100,0)
     
        self.label3=QLabel(self)
        self.label3.setText("Processess Names")
        self.label3.move(10,50)

        self.label4=QLabel(self)
        self.label4.setText("Burst Time")
        self.label4.move(10,100)

        self.label5=QLabel(self)
        self.label5.setText("Arrival Time")
        self.label5.move(10,150)

        self.names=QLineEdit(self)
        self.names.move(100,50)
        self.names.resize(1400,30)

        self.burst=QLineEdit(self)
        self.burst.move(100,100)
        self.burst.resize(1400,30)

        self.arrival=QLineEdit(self)
        self.arrival.move(100 ,150)
        self.arrival.resize(1400,30)
        #self.textEdit=QTextEdit(self)
        #self.textEdit.move(20,250)
        
        
        
        self.button=QPushButton("Go",self)
        self.button.move(0,200)
        self.button.clicked.connect(self.runcode)
        self.back=QPushButton("Back",self)
        self.back.move(100,200)
        self.back.clicked.connect(self.main)
    def main(self):
        self.close()
        self.main=MainWindow(self)
        
    def runcode(self):
      
      
      no_of_process=self.textbox.text()
      process_names=self.names.text()
      burst_time=self.burst.text()
      arrival_time=self.arrival.text()
     
      names_list=process_names.split()
      burst_list=burst_time.split()
      arrival_list=arrival_time.split()
  

      #integer conversion
      burst_list=[float(i) for i in burst_list]
      arrival_list=[float(i) for i in arrival_list]
      no_of_process=int(no_of_process)
      
      ls=linked_list.LinkedList()
      
      i=0
      while i<no_of_process:
              ls.append(names_list[i],burst_list[i],arrival_list[i])
              i=i+1         
      ls.bubble_sort_time()
      time=ls.getHead().getarrivaltime()
      j=0
      start=[]
      end=[]
      name=[]
      dep=[]
      while j<no_of_process:
          dep.append(0)
          j=j+1
      
      temp=linked_list.LinkedList()
      name_in_progress=None
      i=0
      i2=0
      while (ls.size()!=0 or temp.size()!=0):
          
          head=ls.getHead()
          while head is not None :
               if(head.getarrivaltime()<=time):
                   temp.append(head.getname(),head.getbursttime(),head.getarrivaltime())
                   
                   ls.remove(head.getname())
               head=head.getNext()
               
          temp.bubble_sort()
          
          if(temp.size()!=0):
              if(ls.size()!=0):# premetive
                  
                  if(i==0):#first iteration ever
                      start.append(time)
                      name.append(temp.getHead().getname())
                      time=time+1
                      name_in_progress=temp.getHead().getname()
                      temp.getHead().setbursttime(temp.getHead().getbursttime()-1)
                   
                      if(temp.getHead().getbursttime()==0):
                          end.append(time)
                          #
                          #name.append(temp.getHead().getname())
                          dep[index.index(names_list,temp.getHead().getname())]=time
                          temp.remove(temp.getHead().getname())
                         
                  else:#if process should be interrupted
                      
                      if(temp.getHead().getname()!=name_in_progress):
                          node_in_progress=temp.search(name_in_progress)
                          if(node_in_progress!=0):

                           end.append(time)
                           #name.append(name_in_progress)
                          start.append(time)
                          name.append(temp.getHead().getname())
                          time=time+1
                          name_in_progress=temp.getHead().getname()
                          temp.getHead().setbursttime(temp.getHead().getbursttime()-1)
                         
                          if(temp.getHead().getbursttime()==0):
                              end.append(time)
                              dep[index.index(names_list,temp.getHead().getname())]=time
                              temp.remove(temp.getHead().getname())
                             
                      else:#process still have the processor
                          time=time+1
                          temp.getHead().setbursttime(temp.getHead().getbursttime()-1)
                          
                          if(temp.getHead().getbursttime()==0):
                              end.append(time)
                              #name.append(name_in_progress)
                              dep[index.index(names_list,temp.getHead().getname())]=time
                              temp.remove(temp.getHead().getname())
                            
                              
              else:#treated as non prememtive
                

                  if(temp.getHead().getname()==name_in_progress):# if last process was not shorter than remaining time of current process
                      time=time+temp.getHead().getbursttime()
                      #name.append(name_in_progress)
                      end.append(time)
                      dep[index.index(names_list,temp.getHead().getname())]=time
                      temp.remove(temp.getHead().getname())
                      
                  else:#either process is done or has bigger remaining time
                     
                      node_in_progress=temp.search(name_in_progress)
                      if(node_in_progress!=0):#found but has larger remaining time
                       end.append(time)
                       #name.append(name_in_progress)
                      
                      start.append(time)
                      name.append(temp.getHead().getname())
                      name_in_progress=temp.getHead().getname()
                      time=time+temp.getHead().getbursttime()
                      end.append(time)
                      #name.append(temp.getHead().getname())
                      dep[index.index(names_list,temp.getHead().getname())]=time
                      temp.remove(temp.getHead().getname())
                      
                  i2=i2+1
                  
                  
          else:
              time=time+1
          i=i+1
          
    
      k=0
      waiting=0
      while k<no_of_process:
          waiting=waiting+dep[k]-arrival_list[k]-burst_list[k]
          k=k+1
     
      
      average_waiting=waiting/no_of_process    
      x=name
      begin = np.array(start)
      end =   np.array(end)
      plt.barh(range(len(begin)),  end-begin, left=begin)
      plt.yticks(range(len(begin)),x)
      #plt.text(0.6,1.5,('average waiting is ',average_waiting))
      #plt.annotate(("average waiting is",average_waiting),xy=(0.5,1.49))
      plt.title(('average waiting is ',average_waiting))
 
      plt.show()


####################PP#################################################################################
class Window7(QMainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("SJFP")
        #self.setWindowIcon(QtGui.QIcon("download.jpg"))
        self.setGeometry(50,50,500,300)
        self.home()
        self.show()
       
    def home(self):
        
        self.label1=QLabel(self)
        self.label1.setText("No of Processes")
        self.label1.move(10,0) #col ,row
        
        self.textbox=QLineEdit(self)
        self.textbox.move(100,0)
     
        self.label3=QLabel(self)
        self.label3.setText("Processess Names")
        self.label3.move(10,50)

        self.label4=QLabel(self)
        self.label4.setText("Burst Time")
        self.label4.move(10,100)

        self.label5=QLabel(self)
        self.label5.setText("Arrival Time")
        self.label5.move(10,150)

        self.names=QLineEdit(self)
        self.names.move(100,50)
        self.names.resize(1400,30)

        self.burst=QLineEdit(self)
        self.burst.move(100,100)
        self.burst.resize(1400,30)

        self.arrival=QLineEdit(self)
        self.arrival.move(100 ,150)
        self.arrival.resize(1400,30)
        #self.textEdit=QTextEdit(self)
        #self.textEdit.move(20,250)
        self.label6=QLabel(self)
        self.label6.setText("Priority")
        self.label6.move(10,200)

        self.priority=QLineEdit(self)
        self.priority.move(100,200)
        self.priority.resize(1400,30)
        
        
        
        self.button=QPushButton("Go",self)
        self.button.move(0,250)
        self.button.clicked.connect(self.runcode)
        self.back=QPushButton("Back",self)
        self.back.move(100,250)
        self.back.clicked.connect(self.main)
    def main(self):
        self.close()
        self.main=MainWindow(self)
        
    def runcode(self):
      
      
      no_of_process=self.textbox.text()
      process_names=self.names.text()
      burst_time=self.burst.text()
      arrival_time=self.arrival.text()
      priority=self.priority.text()
     
      names_list=process_names.split()
      burst_list=burst_time.split()
      arrival_list=arrival_time.split()
      priority_list=priority.split()
  

      #integer conversion
      burst_list=[float(i) for i in burst_list]
      arrival_list=[float(i) for i in arrival_list]
      priority_list=[int (i) for i in priority_list]
      no_of_process=int(no_of_process)
      
      ls=linked_list.LinkedList()
      
      i=0
      while i<no_of_process:
              ls.append3(names_list[i],burst_list[i],arrival_list[i],priority_list[i])
              i=i+1         
      ls.bubble_sort_time2()
      time=ls.getHead().getarrivaltime()
      j=0
      start=[]
      end=[]
      name=[]
      dep=[]
      while j<no_of_process:
          dep.append(0)
          j=j+1
      
      temp=linked_list.LinkedList()
      name_in_progress=None
      i=0
      i2=0
      while (ls.size()!=0 or temp.size()!=0):
          
          head=ls.getHead()
          while head is not None :
               if(head.getarrivaltime()<=time):
                   temp.append3(head.getname(),head.getbursttime(),head.getarrivaltime(),head.getpriority())
                   
                   ls.remove(head.getname())
               head=head.getNext()
               
          temp.bubble_sort_p()
          
          if(temp.size()!=0):
              if(ls.size()!=0):# premetive
                  
                  if(i==0):#first iteration ever
                      start.append(time)
                      name.append(temp.getHead().getname())
                      time=time+1
                      name_in_progress=temp.getHead().getname()
                      temp.getHead().setbursttime(temp.getHead().getbursttime()-1)
                   
                      if(temp.getHead().getbursttime()==0):
                          end.append(time)
                          #
                          #name.append(temp.getHead().getname())
                          dep[index.index(names_list,temp.getHead().getname())]=time
                          temp.remove(temp.getHead().getname())
                         
                  else:#if process should be interrupted
                      
                      if(temp.getHead().getname()!=name_in_progress):
                          node_in_progress=temp.search(name_in_progress)
                          if(node_in_progress!=0):

                           end.append(time)
                           #name.append(name_in_progress)
                          start.append(time)
                          name.append(temp.getHead().getname())
                          time=time+1
                          name_in_progress=temp.getHead().getname()
                          temp.getHead().setbursttime(temp.getHead().getbursttime()-1)
                         
                          if(temp.getHead().getbursttime()==0):
                              end.append(time)
                              dep[index.index(names_list,temp.getHead().getname())]=time
                              temp.remove(temp.getHead().getname())
                             
                      else:#process still have the processor
                          time=time+1
                          temp.getHead().setbursttime(temp.getHead().getbursttime()-1)
                          
                          if(temp.getHead().getbursttime()==0):
                              end.append(time)
                              #name.append(name_in_progress)
                              dep[index.index(names_list,temp.getHead().getname())]=time
                              temp.remove(temp.getHead().getname())
                            
                              
              else:#treated as non prememtive
                

                  if(temp.getHead().getname()==name_in_progress):# if last process was not shorter than remaining time of current process
                      time=time+temp.getHead().getbursttime()
                      #name.append(name_in_progress)
                      end.append(time)
                      dep[index.index(names_list,temp.getHead().getname())]=time
                      temp.remove(temp.getHead().getname())
                      
                  else:#either process is done or has bigger remaining time
                     
                      node_in_progress=temp.search(name_in_progress)
                      if(node_in_progress!=0):#found but has larger remaining time
                       end.append(time)
                       #name.append(name_in_progress)
                      
                      start.append(time)
                      name.append(temp.getHead().getname())
                      name_in_progress=temp.getHead().getname()
                      time=time+temp.getHead().getbursttime()
                      end.append(time)
                      #name.append(temp.getHead().getname())
                      dep[index.index(names_list,temp.getHead().getname())]=time
                      temp.remove(temp.getHead().getname())
                      
                  i2=i2+1
                  
                  
          else:
              time=time+1
          i=i+1
          
    
      k=0
      waiting=0
      while k<no_of_process:
          waiting=waiting+dep[k]-arrival_list[k]-burst_list[k]
          k=k+1
     
      
      average_waiting=waiting/no_of_process    
      x=name
      begin = np.array(start)
      end =   np.array(end)
      plt.barh(range(len(begin)),  end-begin, left=begin)
      plt.yticks(range(len(begin)),x)
      #plt.text(0.6,1.5,('average waiting is ',average_waiting))
      #plt.annotate(("average waiting is",average_waiting),xy=(0.5,1.49))
      plt.title(('average waiting is ',average_waiting))

      plt.show()



      
    
      
      
      
     
        

      
    
      
      
      
     
        
        



















       
        
        
    
def main():
    import sys
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   
    main()
