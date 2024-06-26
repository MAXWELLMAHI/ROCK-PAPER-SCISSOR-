from tkinter import*
from PIL import Image,ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

#pictures
rock_img = ImageTk.PhotoImage(Image.open("user_rock.jpg"))
paper_img = ImageTk.PhotoImage(Image.open("user_paper.jpg"))
scissor_img = ImageTk.PhotoImage(Image.open("user_scissor.jpg"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor.png"))

#insert picture
user_label = Label(root,image=scissor_img,bg="#9b59b6")
comp_label = Label(root,image=scissor_img_comp,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indicators
user_indicator = Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg =Label(root, font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)



#update message

def updateMessage(x):
    msg['text'] = x
    
#update userscore

def updateUserscore():
    score = (playerScore["text"])
    score =+1
    playerScore["text"] = str(score)
#updatecomputer score

def updateCompScore():
    score = (computerScore["text"])
    score =+1
    computerScore["text"] = str(score)
    
#check winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("Its a Tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
        else:
          updateMessage("You Win!!!!")
          updateUserscore
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose!!")
            updateCompScore()
        else:
            updateMessage("You WIN!!")
            updateUserscore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You WIN")
            updateUserscore()
            
    else:
        pass
    
#update choice

choices = ["rock","paper","scissor"]
def updatechoice(x):
 
#for computer
  compChoice = choices[randint(0,2)]
  if compChoice == "rock":
      comp_label.configure(image=rock_img_comp)
  elif compChoice == "paper":
      comp_label.configure(image=paper_img_comp)
  else :
     comp_label.configure(image=scissor_img_comp)
 
 
    
#for user   
  if x=="rock":
        user_label.configure(image=rock_img)
  elif x=="paper":
        user_label.configure(image=paper_img)
  else:
        user_label.configure(image=scissor_img)
        
  checkWin(x,compChoice)


#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command = lambda:updatechoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command = lambda:updatechoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command = lambda:updatechoice("scissor")).grid(row=2,column=3)

root.mainloop()