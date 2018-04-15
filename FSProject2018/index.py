import os
import pandas
import sys
from text_file_indexer_demo import index_text_file

data=[]
word_list=[]
class estateDetails:
	estateName =""
	estateAddress =""
	estateSize =""
	estatePrice =""
	estateOwner =""
	estateCondition =""

	def getdata( self):
		print("Enter the estate name")
		estateName= input()
		print("Enter the estate address")
		estateAddress = input()
		print("Enter the estate size")
		estateSize = input()
		print("Enter the estate price")
		estatePrice =input()
		print("Enter the estate owner")
		estateOwner = input()
		print("Enter the estate condition")
		estateCondition = input()

	def putdata(self ):
		#st="the details are %s mm %s m %s m %s n %s m %s" %(self.estateName+self.estateAddress+self.estateSize+self.estatePrice+self.estateOwner+self.estateCondition)
		st=("\nESTATE NAME -"+self.estateName+"\nESTATE ADDRESS - "+self.estateAddress+"\nESTATE SIZE -"+self.estateSize+"\nESTATE PRICE - "+self.estatePrice+"\nESTATE OWNER -"+
			self.estateOwner+"\nESTATE CONDITION -"+self.estateCondition)
		print(st)

if __name__== "__main__":
	estateObj=estateDetails()
	#fh = open("estatedetails.txt","w+")
	print("\n**************************WELCOME TO ESTATE PORTAL***************************")
	print("\nENTER YOUR CHOICE")
	while(1):
		print("\n 1-ADD AN ESTATE DETAIL \n 2-SEARCH FOR AN ESTATE\n 3-VISUALISE THE ESTATES\n 4-EXIT THE PORTAL")
		choice= input()
		if(choice=="1"):
			print("enter the following details\nestateName\nestateAddress\nestateSize\nestatePrice\nestateOwner\nestateCondition\n")
			text_file= open("estatedetails.txt","a")
			for i in range (1, 7):
			    print("Please enter data: ")
			    line = input("\n")
			    word_list.append(line + "|")
			word_list.append("\n")
			text_file.writelines(word_list)
			text_file.close()

		elif(choice=="2"):
			print("Searching...")
			index_text_file("estatedetails.txt", "index2.txt")

			# print("Enter the Name of the estate to be searched")
			# searchParam = input("\n")
			# search_file = open("estatedetails.txt","r")
			# for estates in search_file:
			# 	if searchParam in estates:
			# 		print("Estate Found!!!")
			# 		print(estates)
			# search_file.close()

			print("Do you wish to modify??\n Press Y or N Please...")
			ch=input()
			if ch=='Y':
				print("enter the modified estate details\nestateName\nestateAddress\nestateSize\nestatePrice\nestateOwner\nestateCondition\n")
				for i in range (1, 7):
				    print("Please enter data: ")
				    line = input("\n")
				    word_list.append(line + "|")

				modify_file = open("estatedetails.txt","r")
				searchParam.replace(searchParam,modify_file.writelines(word_list))
				modify_file.close()

		elif(choice=="3"):
			print("Visualising...")

		elif(choice=="4"):
			exit()



  #estateObj.getdata()
  #estateObj.putdata()
