#%%
# IMPORTING libraries
import random
from sklearn.tree import DecisionTreeClassifier
#from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
#%%
# setting random seed
random.seed(0.13975)
#%%
# opening file
filename = ""
file = open("/Users/arunkrishnavajjala/Documents/GMU/CS 484/PROJECT/project/boxScore.csv")
#%%
# creating stat dict
statDict = {"Home": 1.0, "Away": 0.0, "East": 1.0, "West": 0.0, "Win": 1.0, "Loss": 0.0}
#%%
# initializing train info
trainDataSet = []
firstKeys = []
secondKeys = []
regularKeys = []
#%%
## parsing the data into the list
count = 0
for line in file:
    if count >= 1:
        trainData = []
        arr = line.split(",")
        # First Team Data
        trainData.append(statDict[arr[6]])
        trainData.append(statDict[arr[8]])
        
        #keys.append(statDict[arr[9]])
        firstKeys.append(float(arr[12]))
        
        #trainData.append(statDict[arr[9]])
        #trainData.append(float(arr[12])/4.0)
        trainData.append(float(arr[13])/4.0)
        trainData.append(float(arr[14])/4.0)
        trainData.append(float(arr[15])/4.0)
        trainData.append(float(arr[16])/4.0)
        trainData.append(float(arr[17])/4.0)
        trainData.append(float(arr[18])/4.0)
        trainData.append(float(arr[19])/4.0)
        trainData.append(float(arr[21])/4.0)
        trainData.append(float(arr[22])/4.0)
        trainData.append(float(arr[24])/4.0)
        trainData.append(float(arr[25])/4.0)
        trainData.append(float(arr[27])/4.0)
        trainData.append(float(arr[28])/4.0)
        trainData.append(float(arr[30])/4.0)
        trainData.append(float(arr[31])/4.0)
        trainData.append(float(arr[33]))
        # Second Team Data
        trainData.append(statDict[arr[62]])
        trainData.append(statDict[arr[64]])
        #trainData.append(statDict[arr[65]])
        #trainData.append(float(arr[68])/4.0)
        trainData.append(float(arr[69])/4.0)
        trainData.append(float(arr[70])/4.0)
        trainData.append(float(arr[71])/4.0)
        trainData.append(float(arr[72])/4.0)
        trainData.append(float(arr[73])/4.0)
        trainData.append(float(arr[74])/4.0)
        trainData.append(float(arr[75])/4.0)
        trainData.append(float(arr[77])/4.0)
        trainData.append(float(arr[78])/4.0)
        trainData.append(float(arr[80])/4.0)
        trainData.append(float(arr[81])/4.0)
        trainData.append(float(arr[83])/4.0)
        trainData.append(float(arr[84])/4.0)
        trainData.append(float(arr[86])/4.0)
        trainData.append(float(arr[87])/4.0)
        trainData.append(float(arr[89]))
        # Append to big Data Set
        secondKeys.append(float(arr[68]))
        trainDataSet.append(trainData)
    if count == 0:
        count += 1
#%%
        
print("Length of Data Set: " + str(len(trainDataSet)))
print("Length ovals in DataSet: " + str(len(trainDataSet[100])))
#%%

#%%
#clf = DecisionTreeClassifier(random_state=0)
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
from sklearn.neighbors import KNeighborsRegressor
# creating the model
clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
X = trainDataSet
Y = firstKeys
clf = clf.fit(X, Y)

# creating the model
cmf = MLPRegressor(solver='lbfgs', alpha=1e-8, hidden_layer_sizes=(5, 2), random_state=1)
X = trainDataSet
Y = secondKeys
cmf = cmf.fit(X, Y)

# creating the gui
from tkinter import *
 
window = Tk()
 
# creating the inputs
window.title("NBA Prediction")

window.geometry('500x550')

lbl0 = Label(window, text="HOME TEAM", foreground="Green")
lbl0.grid(column=0, row=0)

# getting conference
lbl = Label(window, text="E(1)/W(0)")
lbl.grid(column=0, row=1)
txt = Entry(window,width=10)
txt.grid(column=1, row=1)

# getting assista
lbl1 = Label(window, text="Assists")
lbl1.grid(column=0, row=2)
txt1 = Entry(window,width=10)
txt1.grid(column=1, row=2)

# getting tunrovers
lbl2 = Label(window, text="Turnovers")
lbl2.grid(column=0, row=3)
txt2 = Entry(window,width=10)
txt2.grid(column=1, row=3)

# getting steals
lbl3 = Label(window, text="Steals")
lbl3.grid(column=0, row=4)
txt3 = Entry(window,width=10)
txt3.grid(column=1, row=4)

# getting blocks
lbl4 = Label(window, text="Blocks")
lbl4.grid(column=0, row=5)
txt4 = Entry(window,width=10)
txt4.grid(column=1, row=5)

# getting fouls
lbl5 = Label(window, text="Fouls")
lbl5.grid(column=0, row=6)
txt5 = Entry(window,width=10)
txt5.grid(column=1, row=6)

# getting fga
lbl6 = Label(window, text="FG-A")
lbl6.grid(column=0, row=7)
txt6 = Entry(window,width=10)
txt6.grid(column=1, row=7)

# getting fgm
lbl7 = Label(window, text="FG-M")
lbl7.grid(column=0, row=8)
txt7 = Entry(window,width=10)
txt7.grid(column=1, row=8)

# getting 2pa
lbl8 = Label(window, text="2pt-A")
lbl8.grid(column=0, row=9)
txt8 = Entry(window,width=10)
txt8.grid(column=1, row=9)

# getting 2pm
lbl9 = Label(window, text="2pt-M")
lbl9.grid(column=0, row=10)
txt9 = Entry(window,width=10)
txt9.grid(column=1, row=10)

# getting 3pa
lbl10 = Label(window, text="3pt-A")
lbl10.grid(column=0, row=11)
txt10 = Entry(window,width=10)
txt10.grid(column=1, row=11)

# getting 3pm
lbl11 = Label(window, text="3pt-M")
lbl11.grid(column=0, row=12)
txt11 = Entry(window,width=10)
txt11.grid(column=1, row=12)

# getting fta
lbl14 = Label(window, text="FT-A")
lbl14.grid(column=0, row=13)
txt14 = Entry(window,width=10)
txt14.grid(column=1, row=13)

# getting ftm
lbl15 = Label(window, text="FT-M")
lbl15.grid(column=0, row=14)
txt15 = Entry(window,width=10)
txt15.grid(column=1, row=14)

# getting oreb
lbl16 = Label(window, text="ORB")
lbl16.grid(column=0, row=15)
txt16 = Entry(window,width=10)
txt16.grid(column=1, row=15)

# getting drrreb
lbl17 = Label(window, text="DRB")
lbl17.grid(column=0, row=16)
txt17 = Entry(window,width=10)
txt17.grid(column=1, row=16)

# getting points
lbl18 = Label(window, text="Points")
lbl18.grid(column=0, row=17)
txt18 = Entry(window,width=10)
txt18.grid(column=1, row=17)

home = []
# function to create vector to predict the score
def processhome():
    homeTeam = []
    homeTeam.append(float(txt.get()))
    homeTeam.append(1)
    homeTeam.append(float(txt1.get()))
    homeTeam.append(float(txt2.get()))
    homeTeam.append(float(txt3.get()))
    homeTeam.append(float(txt4.get()))
    homeTeam.append(float(txt5.get()))
    homeTeam.append(float(txt6.get()))
    homeTeam.append(float(txt7.get()))
    homeTeam.append(float(txt8.get()))
    homeTeam.append(float(txt9.get()))
    homeTeam.append(float(txt10.get()))
    homeTeam.append(float(txt11.get()))
    homeTeam.append(float(txt14.get()))
    homeTeam.append(float(txt15.get()))
    homeTeam.append(float(txt16.get()))
    homeTeam.append(float(txt17.get()))
    homeTeam.append(float(txt18.get()))
    homeTeam.append(float(txtd.get()))
    homeTeam.append(0)
    homeTeam.append(float(txt1d.get()))
    homeTeam.append(float(txt2d.get()))
    homeTeam.append(float(txt3d.get()))
    homeTeam.append(float(txt4d.get()))
    homeTeam.append(float(txt5d.get()))
    homeTeam.append(float(txt6d.get()))
    homeTeam.append(float(txt7d.get()))
    homeTeam.append(float(txt8d.get()))
    homeTeam.append(float(txt9d.get()))
    homeTeam.append(float(txt10d.get()))
    homeTeam.append(float(txt11d.get()))
    homeTeam.append(float(txt14d.get()))
    homeTeam.append(float(txt15d.get()))
    homeTeam.append(float(txt16d.get()))
    homeTeam.append(float(txt17d.get()))
    homeTeam.append(float(txt18d.get()))
    print(homeTeam)
    
    # setting the predictions
    predictionsOne = clf.predict([homeTeam])
    predictionsTwo = cmf.predict([homeTeam])
    
    # creates results window
    result = Tk()
    result.title("Result")
    # presents home score
    lbl0d = Label(result, text="Home")
    lbl0d.grid(column=2, row=0)
    lbl0dt = Label(result, text= str(round(predictionsOne[0])))
    lbl0dt.grid(column=2, row=1)
    
    lbl0dh = Label(result, text=" vs. ")
    lbl0dh.grid(column=1, row=1)
    
    # presents away score
    lbl0dg = Label(result, text="Away")
    lbl0dg.grid(column=0, row=0)
    lbl0dg = Label(result, text= str(round(predictionsTwo[0].round())))
    lbl0dg.grid(column=0, row=1)
    
    lbl0dh = Label(result, text="  ")
    lbl0dh.grid(column=1, row=2)
    
    difference = round(predictionsOne[0]) - round(predictionsTwo[0])
    # says who wins by how much
    if(difference > 0):
        lbl0dgf = Label(result, text="Home Team Wins By")
        lbl0dgf.grid(column=1, row=3)
        lbl0dgf = Label(result, text= str(difference))
        lbl0dgf.grid(column=1, row=4)
    else:
        lbl0dgf = Label(result, text="Home Team Loses By")
        lbl0dgf.grid(column=1, row=3)
        lbl0dgf = Label(result, text = str(difference * -1))
        lbl0dgf.grid(column=1, row=4)
    
    
    result.geometry('400x200')
    result.mainloop()
    
    
    print(difference)
    print(str(predictionsOne) + str(predictionsTwo))
    

# gets away information
lbl0d = Label(window, text="AWAY TEAM", foreground="Blue")
lbl0d.grid(column=4, row=0)

# gets conference
lbld = Label(window, text="E(1)/W(0)")
lbld.grid(column=4, row=1)
txtd = Entry(window,width=10)
txtd.grid(column=5, row=1)

# gets assists
lbl1d = Label(window, text="Assists")
lbl1d.grid(column=4, row=2)
txt1d = Entry(window,width=10)
txt1d.grid(column=5, row=2)

# gets to
lbl2d = Label(window, text="Turnovers")
lbl2d.grid(column=4, row=3)
txt2d = Entry(window,width=10)
txt2d.grid(column=5, row=3)

# gets stls
lbl3d = Label(window, text="Steals")
lbl3d.grid(column=4, row=4)
txt3d = Entry(window,width=10)
txt3d.grid(column=5, row=4)

# gets blcks
lbl4d = Label(window, text="Blocks")
lbl4d.grid(column=4, row=5)
txt4d = Entry(window,width=10)
txt4d.grid(column=5, row=5)

# gets fouls
lbl5d = Label(window, text="Fouls")
lbl5d.grid(column=4, row=6)
txt5d = Entry(window,width=10)
txt5d.grid(column=5, row=6)

# gets fga
lbl6d = Label(window, text="FG-A")
lbl6d.grid(column=4, row=7)
txt6d = Entry(window,width=10)
txt6d.grid(column=5, row=7)

# gets fgm
lbl7d = Label(window, text="FG-M")
lbl7d.grid(column=4, row=8)
txt7d = Entry(window,width=10)
txt7d.grid(column=5, row=8)

# gets 2pa
lbl8d = Label(window, text="2pt-A")
lbl8d.grid(column=4, row=9)
txt8d = Entry(window,width=10)
txt8d.grid(column=5, row=9)

# gets 2pm
lbl9d = Label(window, text="2pt-M")
lbl9d.grid(column=4, row=10)
txt9d = Entry(window,width=10)
txt9d.grid(column=5, row=10)

# gets 3pa
lbl10d = Label(window, text="3pt-A")
lbl10d.grid(column=4, row=11)
txt10d = Entry(window,width=10)
txt10d.grid(column=5, row=11)

# gets 3pm
lbl11d = Label(window, text="3pt-M")
lbl11d.grid(column=4, row=12)
txt11d = Entry(window,width=10)
txt11d.grid(column=5, row=12)

# gets fta
lbl14d = Label(window, text="FT-A")
lbl14d.grid(column=4, row=13)
txt14d = Entry(window,width=10)
txt14d.grid(column=5, row=13)

# gets fta
lbl15d = Label(window, text="FT-M")
lbl15d.grid(column=4, row=14)
txt15d = Entry(window,width=10)
txt15d.grid(column=5, row=14)

# gets orb
lbl16d = Label(window, text="ORB")
lbl16d.grid(column=4, row=15)
txt16d = Entry(window,width=10)
txt16d.grid(column=5, row=15)

# gets dreb
lbl17d = Label(window, text="DRB")
lbl17d.grid(column=4, row=16)
txt17d = Entry(window,width=10)
txt17d.grid(column=5, row=16)

# gets points
lbl18d = Label(window, text="Points")
lbl18d.grid(column=4, row=17)
txt18d = Entry(window,width=10)
txt18d.grid(column=5, row=17)

# predict button 
btn = Button(window, text="Predict", command = processhome, width=10, height = 2, foreground="red")

print("--------")
print(processhome)

btn.grid(column=3, row=21)

# prints the gui
window.mainloop()
#%%




















