# -*- coding: utf-8 -*-
"""
Created on Thu May  2 01:24:40 2019

@author: yasser
"""
# # Import tkinter for GUI creation

import tkinter
from tkinter import *


# Define a function to handle the main input process
def  takeinput():
    # Function to switch the visible frame

    def sit_open(frame):
        frame.tkraise() # Bring the specified frame to the top
        if frame==output_frame:
            TakeInput() # Call TakeInput if the output frame is selected
    # Function to process input and generate drawings
    def TakeInput():
        # Function to display the drawing based on inputs M and V

        def showing_the_drawing(M,V):
            import random
            # Initialize lists for processing
            L=[]
            m=[]
            # Filter and prepare data from input M

            for i in M:
                if i[2]!='':
                    m.append(i)
             # Further process data to create a list L with specific structure
                   
            for i in m:
                if len(i[2])>1:
                    for j in i[2]:
                        L.append([j,i[0]])
                else:
                    L.append([i[2],i[0]])
            # Function to draw a circle on canvas
            def circle(canvas, x, y, r, width, Color):
                return canvas.create_oval(x+r, y+r, x-r, y-r, width=width, fill=Color)
            
            # Function to draw a circular arc
            def circular_arc(canvas, x, y, r, t0, t1, width):
                return canvas.create_arc(x-r, y-r, x+r, y+r, start=t0, extent=t1-t0, style='arc', width=width)
            
            # Function to draw an ellipse
            def ellipse(canvas, x, y, r1, r2, width):
                return canvas.create_oval(x+r1, y+r2, x-r1, y-r2, width=width)
            
            # Function to draw an elliptical arc
            def elliptical_arc(canvas, x, y, r1, r2, t0, t1, width, s):
                return canvas.create_arc(x-r1, y-r2, x+r1, y+r2, start=t0, extent=t1-t0, style='arc', width=width, outline=s)
            
            # Function to draw a line with optional arrows
            def line(canvas, x1, y1, x2, y2, width, Color, start_arrow=0, end_arrow=0):
                arrow_opts = start_arrow << 1 | end_arrow  # Determine arrow configuration
                arrows = {0b10: 'first', 0b01: 'last', 0b11: 'both'}.get(arrow_opts, None)  # Map binary to arrow option
                return canvas.create_line(x1, y1, x2, y2, width=width, arrow=arrows, fill=Color)
            
            # Function to add text to the canvas
            def text(canvas, x, y, text):
                return canvas.create_text(x, y, text=text, font=('bold', 20))
            
            # Function to get count, min, and max values from list L
            def get_count(L):
                m = []
                for i in L:
                    for j in i[0:len(i)]:
                        if ord(j)-65 in m:
                            pass
                        else:
                            m.append(ord(j)-65)
                return (max(m)+1, m, min(m))

            # Initialize variables for the drawing
            v = []
            Q = get_count(L)  # Get the count, unique elements, and min value from L
            for i in range(len(V) - 1):
                v.append(V[i:i+2])  # Process V for drawing
            
            q = []  # Initialize a list to store processed values
            l = Q[0]  # The total count of unique elements
            c = Q[2]  # The minimum value among elements
            M = []  # List to store X-coordinates for drawing
            N = []  # List to store Y-coordinates for drawing
            
            # Initialize M, N, and other lists with default values based on 'c'
            for i in range(c):
                M.append(0)
                N.append(0)
                q.append(0)
            
            # Populate 'q' with sorted unique elements for drawing logic
            for j in sorted(Q[1]):
                q.append(j)

            # Draw circles for each unique element in the processed list
            for j in range(3):  # Iterate over a fixed range for drawing rows
                for i in range(0, (l // 4) + 1):  # Iterate to draw within each row based on 'l'
                    if chr(c + 65) in V:  # Check if element needs a specific color
                        if c in q:  # Draw circle with specific attributes if condition met
                            circle(w, 150 + 100 * i, 100 + j * 150, 20, 3, '#127563')  # Custom circle call
                            text(w, 150 + 100 * i, 100 + j * 150, chr(c + 65))  # Add text label
                            M.append(150 + 100 * i)  # Store X-coordinate
                            N.append(100 + j * 150)  # Store Y-coordinate
                            c += 1  # Increment 'c' for next iteration
                        else:
                            # Similar logic applied for different cases with specific conditions
                            M.append(150 + 100 * i)
                            N.append(100 + j * 150)
                            c += 1

                        
            # Final loop to handle elements outside the main drawing logic
            for i in range(l - 3 * ((l // 4) + 1)):
                # Conditional drawing based on character checks and list membership
                if chr(c + 65) in V:
                    if c in q:
                        circle(w, 150 + 100 * i, 550, 20, 3, '#127563')
                        text(w, 150 + 100 * i, 550, chr(c + 65))
                        M.append(150 + 100 * i)
                        N.append(550)
                        c += 1
                    else:
                        M.append(150 + 100 * i)
                        N.append(550)
                        c += 1
                # Additional conditions and drawing logic follow a similar pattern
                
            # Process V to remove processed elements
            for i in v:
                L.remove(i)

            for i in range (len(L)):
                if ((abs(ord(L[i][0])-ord(L[i][1])-1))>(l//4)+2 and (M[ord(L[i][0])-65]==M[ord(L[i][1])-65] )) or (( abs(ord(L[i][0])-ord(L[i][1]))-1>=1 )  and (N[ord(L[i][0])-65])==N[ord(L[i][1])-65]) :
                    if (M[ord(L[i][0])-65]==M[ord(L[i][1])-65] ):
                        midx, midy =  (M[ord(L[i][0])-65]+M[ord(L[i][1])-65] )/2, ((N[ord(L[i][0])-65])+N[ord(L[i][1])-65])/2
                        r1, r2 = M[ord(L[i][1])-65]-midx+40,N[ord(L[i][1])-65]-midy
                        elliptical_arc(w,midx,midy,r1,r2, 90,270 , 3,'red')
                        line(w, M[ord(L[i][1])-65]-20, N[ord(L[i][1])-65]-20, M[ord(L[i][1])-65]-15,N[ord(L[i][1])-65]-15, 5,'red', end_arrow=1)
            
                    elif ((N[ord(L[i][0])-65])==(N[ord(L[i][1])-65])):
                        midx, midy =  (M[ord(L[i][0])-65]+M[ord(L[i][1])-65] )/2, ((N[ord(L[i][0])-65])+(N[ord(L[i][1])-65]))/2
                        r1, r2 = M[ord(L[i][1])-65]-midx,(N[ord(L[i][1])-65])-midy+40
                        elliptical_arc(w,midx,midy,r1,r2, 0,180 , 3,'red')
                        line(w, M[ord(L[i][1])-65]-5, (N[ord(L[i][1])-65])-20, M[ord(L[i][1])-65]-10,(N[ord(L[i][1])-65])-15, 5,'red', end_arrow=1)
            
                else:
                    line(w, M[ord(L[i][0])-65],(N[ord(L[i][0])-65]),M[ord(L[i][1])-65],(N[ord(L[i][1])-65])-22, 3,'red', end_arrow=1)
            for i in range (len(v)):
                if ((abs(ord(v[i][0])-ord(v[i][1])-1))>(l//4)+2 and (M[ord(v[i][0])-65]==M[ord(v[i][1])-65] )) or (( abs(ord(v[i][0])-ord(v[i][1]))-1>=1 )  and (N[ord(v[i][0])-65])==N[ord(v[i][1])-65]) :
                    if (M[ord(v[i][0])-65]==M[ord(v[i][1])-65] ):
                        midx, midy =  (M[ord(v[i][0])-65]+M[ord(v[i][1])-65] )/2, ((N[ord(v[i][0])-65])+N[ord(v[i][1])-65])/2
                        r1, r2 = M[ord(v[i][1])-65]-midx+40,N[ord(v[i][1])-65]-midy
                        elliptical_arc(w,midx,midy,r1,r2, 90,270 , 3,'#127563')
                        line(w, M[ord(v[i][1])-65]-20, N[ord(v[i][1])-65]-20, M[ord(v[i][1])-65]-15,N[ord(v[i][1])-65]-15, 5,'#127563', end_arrow=1)
            
                    elif ((N[ord(v[i][0])-65])==(N[ord(v[i][1])-65])):
                        midx, midy =  (M[ord(v[i][0])-65]+M[ord(v[i][1])-65] )/2, ((N[ord(L[i][0])-65])+(N[ord(L[i][1])-65]))/2
                        r1, r2 = M[ord(L[i][1])-65]-midx,(N[ord(L[i][1])-65])-midy+40
                        elliptical_arc(w,midx,midy,r1,r2, 0,180 , 3,'#127563')
                        line(w, M[ord(L[i][1])-65]-5, (N[ord(L[i][1])-65])-20, M[ord(L[i][1])-65]-10,(N[ord(v[i][1])-65])-15, 5,'#127563', end_arrow=1)
            
                else:
                    line(w, M[ord(v[i][0])-65],(N[ord(v[i][0])-65]),M[ord(v[i][1])-65],(N[ord(v[i][1])-65])-22, 3,'#127563', end_arrow=1)
            c=Q[2]
            for j in range(3):
                for i in range (0,(l//4)+1):
                    if chr(c+65) in V:
                        if c in q:
                                circle(w, 150+100*i, 100+j*150, 20, 3,'#127563') # 1 outer edge
                                text(w,150+100*i , 100+j*150, chr(c+65))
                                c+=1
                        else:

                            c+=1
                    else:
                        if c in q:
                                circle(w, 150+100*i, 100+j*150, 20, 3,'red') # 1 outer edge
                                text(w,150+100*i , 100+j*150, chr(c+65))
                                c+=1
                        else:
                            c+=1
            for i in range(l-3*((l//4)+1)):
                if chr (c+65)in V:
                    if c in q:
                      circle(w, 150+100*i, 550, 20, 3,'#127563') # 1 outer edge
                      text(w,150+100*i , 550, chr(c+65))
                      c+=1
                    else:
                            c+=1
                
            # Define function for handling user inputs and updating the drawing configuration
        def sit_open(frame):
                frame.tkraise()  # Brings the specified frame to the top of the window stack
                if frame == drawing_frame:  # Check if the drawing frame is the target
                    showing_the_drawing(L, V)  # Call the function to display the drawing based on input lists L and V

            # Extract and process activity data from user input for drawing
        L = []  # Initialize list to hold processed activity data
        for i in entries:  # Loop through user entries
                sub_L = []  # Temporary list to hold individual activity data
                n = 0  # Counter for processing each entry
                for j in i:  # Iterate through each field in an entry
                    n += 1  # Increment counter
                    if n == 2:  # If processing duration field
                        sub_L.append(int(j.get()))  # Convert input to integer and append to sub_L
                    else:  # For activity name or precedence fields
                        if len(j.get()) > 1:  # If input is more than one character
                            sub_L.append(list(j.get()[0:len(j.get()):2]))  # Process and store as list
                        elif len(j.get()) == 1:  # If input is a single character
                            sub_L.append(j.get())  # Directly append the input
                        else:  # If input field is empty
                            pass  # Do nothing
                L.append(sub_L)  # Append processed activity data to main list

        def get_search(M,N):
            for j in N:
                if M==j[0]:
                    return N.index(j)
        def get_search_backword(M,N):
            y = []
            for j in N:
                if type(j[2]) == list:
                    for x in j[2]:
                        if M ==x:
                            y.append(N.index(j))
                else:
                    if M==j[2]:
                        y.append(N.index(j))
            return(y)
            
        def forword_path(L):
            for i in L:
                if len(i)==2:
                    i.append('')
                    i.append(0)
                    i.append(i[1])
                else:
                    if type(i[2])== list:
                        m = []
                        for x in i[2]:
                            m.append(L[get_search(x,L[0:L.index(i)+1])][4])
                        i.append(max(m))
                        i.append(max(m)+i[1]) 
                    else:
                        y=L[get_search(i[2],L[0:L.index(i)+1])][4]
                        i.append(y)
                        i.append(y+i[1])
            return L
        def get_project_ccompletion_time(L):
            T=[]
            for i in L:
                T.append(i[4])
            return (max(T),L)
        def backword_path(P,L):
            for i in L:
                m = get_search_backword(i[0],L[0:L.index(i)+1])
                if len(m)== 0:
                    i.append(P-i[1])
                    i.append(P)
                else:
                    k =[]
                    for j in m:
                        k.append(L[j][5])
                    n = min(k)
                    i.append(n-i[1])
                    i.append(n)
            return L
        def get_slack(L):
            k =[]
            L=forword_path(L)
            L=get_project_ccompletion_time(L)
            m=L[0]
            L[1].reverse()
            L=backword_path(L[0],L[1])
            L.reverse()
            for i in L:
                i.append(i[6]-i[4])
            for j in L:
                if j[7]==0:
                    k.append(j[0])
            return (k,L,m)
        def get_critical_path(L):
            k = get_slack(L)
            Label1=Label(output_frame,text='Activities',background="#127563",foreground="white", font=("bold", 14,))
            Label1.place(x=200,y=10,anchor=CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=i[0],background="#127563",foreground="white", font=("bold", 14,))
                Label1.place(x=200,y=30+20*j,anchor=CENTER)
                j+=1
            Label2=Label(output_frame,text='Duration',background="#127563",foreground="white", font=("bold", 14,))
            Label2.place(x=350,y=10,anchor=CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[1]),background="#127563",foreground="white", font=("bold", 14,))
                Label1.place(x=350,y=30+20*j,anchor=CENTER)
                j+=1
            Label3=Label(output_frame,text='precedence',background="#127563",foreground="white", font=("bold", 14,))
            Label3.place(x=500,y=10,anchor=CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=i[2],background="#127563",foreground="white", font=("bold", 14,))
                Label1.place(x=500,y=30+20*j,anchor=CENTER)
                j+=1
            Label4=Label(output_frame,text='Earlest Start',background="#127563",foreground="white", font=("bold", 14,))
            Label4.place(x=650,y=10,anchor=CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[3]),background="#127563",foreground="white", font=("bold", 14,))
                Label1.place(x=650,y=30+20*j,anchor=CENTER)
                j+=1
            Label5=Label(output_frame,text='Latest Start',background="#127563",foreground="white", font=("bold", 14,))
            Label5.place(x=800,y=10,anchor=CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[4]),background="#127563",foreground="white", font=("bold", 14,))
                Label1.place(x=800,y=30+20*j,anchor=CENTER)
                j+=1
            Label6=Label(output_frame,text='Earlest Finish',background="#127563",foreground="white", font=("bold", 14,))
            Label6.place(x=950,y=10,anchor=CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[5]),background="#127563",foreground="white", font=("bold", 14,))
                Label1.place(x=950,y=30+20*j,anchor=CENTER)
                j+=1
            Label7=Label(output_frame,text='Latest Finish',background="#127563",foreground="white", font=("bold", 14,))
            Label7.place(x=1100,y=10,anchor=CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[6]),background="#127563",foreground="white", font=("bold", 14,))
                Label1.place(x=1100,y=30+20*j,anchor=CENTER)
                j+=1
            Label8=Label(output_frame,text='Slack',background="#127563",foreground="white", font=("bold", 14,))
            Label8.place(x=1250,y=10,anchor=CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[7]),background="#127563",foreground="white", font=("bold", 14,))
                Label1.place(x=1250,y=30+20*j,anchor=CENTER)
                j+=1
            Label8=Label(output_frame,text='The project completion time is ',background="#127563",foreground="white", font=("bold", 14,))
            Label8.place(x=400,y=45+20*j,anchor=CENTER)
            Label9=Label(output_frame,text=str(k[2])+'   unit time' ,background="#127563",foreground="white", font=("bold", 14,))
            Label9.place(x=650,y=45+20*j,anchor=CENTER)
            Label10=Label(output_frame,text='The critical path is          ',background="#127563",foreground="white", font=("bold", 14,))
            Label10.place(x=400,y=75+20*j,anchor=CENTER)
            g=[]
            m=[]
            for i in k[1]:
                if i[2]=='':
                    m.append(i[0])
            g.append(m)
            def F(j,x):
                for i in x:
                    if i ==j:
                        return True
                return False
            def G(x,h):
                for i in g:
                    for j in i:
                        if F(j,x)==True:
                            return True
                return False
                
            for i in k[1][1:len(k[1])]:
                if i[-1]==0:
                    if G(i[2],g)==True:
                        g.append(m)
                        m=[]
                        m.append(i[2])
                        m.append(i[0])
                    else:
                        m.append(i[0])
            g.append(m)
            g.remove(g[0])
            g.remove(g[0])
            D=0
            b=0
            i=0
            for J in g:                    
                D=30*i+D
                if J!=g[0]:
                    Label11=Label(output_frame,text='OR',background="#127563",foreground="white", font=("bold", 14,))
                    Label11.place(x=500+30*i+D,y=75+20*j,anchor=CENTER)
                    b+=1
                for i in range(len(J)):

                    if i!=len(J)-1:
                        Label11=Label(output_frame,text=str(J[i])+'--->',background="#127563",foreground="white", font=("bold", 14,))
                        Label11.place(x=500+30*i+D+75*b,y=75+20*j,anchor=CENTER)
                    else:
                        Label11=Label(output_frame,text=str(J[i]),background="#127563",foreground="white", font=("bold", 14,))
                        Label11.place(x=500+30*i+D+75*b,y=75+20*j,anchor=CENTER)
                drawing_button = Button(output_frame,text="Showing the Drawing",command=lambda:sit_open(drawing_frame),background="#127563",foreground="white", font=("bold", 16,))
                drawing_button.place(x=400,y=115+20*j,anchor=CENTER)
            return k[0]
        W=get_critical_path(L)
    Label_1=Label(input_frame,text='Activity',background='#146054',foreground="white", font=("bold", 16,))
    Label_3=Label(input_frame,text='precedence',background='#146054',foreground="white", font=("bold", 16,))
    Label_2=Label(input_frame,text='Duration',background='#146054',foreground="white", font=("bold", 16,))
    Label_1.place(x=500,y=0,anchor=NW)
    Label_2.place(x=600,y=0,anchor=NW)
    Label_3.place(x=700,y=0,anchor=NW)
    e= int(entry_0.get())
    entries=[]
    for i in range(0,e):
        subentries=[]
        for j in range(3):
            subentries.append(Entry(input_frame))
        entries.append(subentries)
    for i in range(0,e):
        for j in range(3):
            entries[i][j].place(x=500+j*100,y=25*i+40,anchor=NW)
    b=Button(input_frame,text="Start Calculations",command=lambda:sit_open(output_frame),background='#146054',foreground="white", font=("bold", 16,))
    b.place(x=550,y=25*i+100,anchor=NW)
def AOAinput():
    def sit_open(frame):
        frame.tkraise()
        if frame==output_frame:
            TakeInput()
    def TakeInput():
        def showing_the_drawing(M,V):
            v=[]
            L=[]
            for i in M:
                L.append([i[0],i[1]])
            for i in V:
                for j in i:
                    if j in v:
                        pass
                    else:
                        v.append(j)
            def circle(canvas, x, y, r, width,Color):
                            return canvas.create_oval(x+r, y+r, x-r, y-r, width=width,fill=Color)
                        
            def elliptical_arc(canvas, x, y, r1, r2, t0, t1, width,s):
                            return canvas.create_arc(x-r1, y-r2, x+r1, y+r2, start=t0, extent=t1-t0,
                                                     style='arc', width=width,outline = s)
                        
            def line(canvas, x1, y1, x2, y2, width,Color, start_arrow=0, end_arrow=0):
                            arrow_opts = start_arrow << 1 | end_arrow
                            arrows = {0b10: 'first', 0b01: 'last', 0b11: 'both'}.get(arrow_opts, None)
                            return canvas.create_line(x1, y1, x2, y2, width=width, arrow=arrows,fill=Color)
                        
            def text(canvas, x, y, text):
                            return canvas.create_text(x, y, text=text, font=('bold', 20))
                        
                        
            def get_count(L):
                k=[]
                for i in L:
                    if i[0] in k:
                        pass
                    else:
                        k.append(i[0])
                    if i[1] in k:
                        pass
                    else:
                        k.append(i[1])
                return (len(k),k,min(k))
            Q=get_count(L)
            q=[]
            l=Q[0]
            c=Q[2]
            M=[]
            N=[]
            for i in range(c):
                M.append(0)
                N.append(0)
                q.append(0)
                for j in sorted(Q[1]):
                    q.append(j)
            for j in range(3):
                for i in range (0,(l//4)+1):
                    if c in v:
                        if c in q:
                            circle(w, 150+100*i, 100+j*150, 20, 3,'#127563') # 1 outer edge
                            text(w,150+100*i , 100+j*150, str(c))
                            M.append(150+100*i)
                            N.append(100+j*150)
                            c+=1
                        else:
                            c+=1
                    else:
                        if c in q:
                            circle(w, 150+100*i, 100+j*150, 20, 3,'red') # 1 outer edge
                            text(w,150+100*i , 100+j*150, str(c))
                            M.append(150+100*i)
                            N.append(100+j*150)
                            c+=1
                        else:
                            c+=1
                        
            for i in range(l-3*((l//4)+1)):
                if  c in v:
                    circle(w, 150+100*i, 550, 20, 3,'red') # 1 outer edge
                    text(w,150+100*i , 550, str(c))
                    M.append(150+100*i)
                    N.append(550)
                    c+=1
                else:
                    circle(w, 150+100*i, 550, 20, 3,'#127563') # 1 outer edge
                    text(w,150+100*i , 550, str(c))
                    M.append(150+100*i)
                    N.append(550)
                    c+=1
            for i in V:
                L.remove(i)
            for i in range (len(L)):
                if (abs(L[i][0]-L[i][1]-1)>(l//4+2) and (M[L[i][0]]==M[L[i][1]]) ) or (( abs(L[i][0]-L[i][1])-1>=1 )  and (N[L[i][0]]==N[L[i][1]])) :
                    if (M[L[i][0]]==M[L[i][1]]):
                        midx, midy =  (M[L[i][0]]+M[L[i][1]])/2, (N[L[i][0]]+N[L[i][1]])/2
                        r1, r2 = M[L[i][1]]-midx+40,N[L[i][1]]-midy
                        elliptical_arc(w,midx,midy,r1,r2, 90,270 , 3,'red')
                        line(w, M[L[i][1]]-20, N[L[i][1]]-20, M[L[i][1]]-15,N[L[i][1]]-15, 5,'red', end_arrow=1)
                    
                    elif (N[L[i][0]]==N[L[i][1]]):
                        midx, midy =  (M[L[i][0]]+M[L[i][1]])/2, (N[L[i][0]]+N[L[i][1]])/2
                        r1, r2 = M[L[i][1]]-midx,N[L[i][1]]-midy+40
                        elliptical_arc(w,midx,midy,r1,r2, 0,180 , 3,'red')
                        line(w, M[L[i][1]]-20, N[L[i][1]]-25, M[L[i][1]]-15,N[L[i][1]]-20, 5,'red', end_arrow=1)
                        
                else: 
                        line(w, M[L[i][0]],N[L[i][0]],M[L[i][1]],N[L[i][1]]-22, 3,'red', end_arrow=1)
                        
            for i in range (len(V)):
                if (abs(V[i][0]-V[i][1]-1)>(l//4+2) and (M[V[i][0]]==M[V[i][1]]) ) or (( abs(V[i][0]-V[i][1])-1>=1 )  and (N[V[i][0]]==N[V[i][1]])) :
                    if (M[V[i][0]]==M[V[i][1]]):
                        midx, midy =  (M[V[i][0]]+M[V[i][1]])/2, (N[V[i][0]]+N[V[i][1]])/2
                        r1, r2 = M[V[i][1]]-midx+40,N[V[i][1]]-midy
                        elliptical_arc(w,midx,midy,r1,r2, 90,270 , 3,'#127563')
                        line(w, M[V[i][1]]-20, N[V[i][1]]-20, M[V[i][1]]-15,N[V[i][1]]-15, 5,'#127563', end_arrow=1)
                    
                    elif (N[V[i][0]]==N[V[i][1]]):
                        midx, midy =  (M[V[i][0]]+M[V[i][1]])/2, (N[V[i][0]]+N[V[i][1]])/2
                        r1, r2 = M[V[i][1]]-midx,N[V[i][1]]-midy+40
                        elliptical_arc(w,midx,midy,r1,r2, 0,180 , 3,'#127563')
                        line(w, M[V[i][1]]-20, N[V[i][1]]-25, M[V[i][1]]-15,N[V[i][1]]-20, 5,'#127563', end_arrow=1)
                        
                else: 
                        line(w, M[V[i][0]],N[V[i][0]],M[V[i][1]],N[V[i][1]]-22, 3,'#127563', end_arrow=1)
        
            c=Q[2]
            for j in range(3):
                for i in range (0,(l//4)+1):
                    if c in v:
                        if c in q:
                            circle(w, 150+100*i, 100+j*150, 20, 3,'#127563') # 1 outer edge
                            text(w,150+100*i , 100+j*150, str(c))
                        c+=1
                    else:
                        if c in q:
                            circle(w, 150+100*i, 100+j*150, 20, 3,'red') # 1 outer edge
                            text(w,150+100*i , 100+j*150, str(c))
                        c+=1
                        
            for i in range(l-3*((l//4)+1)):
                if  c in v:
                    circle(w, 150+100*i, 550, 20, 3,'red') # 1 outer edge
                    text(w,150+100*i , 550, str(c))
                else:
                    circle(w, 150+100*i, 550, 20, 3,'#127563') # 1 outer edge
                    text(w,150+100*i , 550, str(c))
                c+=1
        def sit_open(frame):
            frame.tkraise()
            if frame ==drawing_frame:
                showing_the_drawing(L,k)
        L=[]
        for i in entries:
            sub_L=[]
            n=0
            for j in i:
                sub_L.append(int(j.get()))
            L.append(sub_L)
        def get_search(M,N):
            k =[]
            for j in N:
                if M==j[1]:
                    k.append(N.index(j))
            return k
        def get_search_backword(M,N):
            k =[]
            for j in N:
                if M==j[0]:
                    k.append(N.index(j))
            return k
        def forword_path(L):
            for i in L:
                m=get_search(i[0],L[0:L.index(i)+1])
                if len(m) ==0:
                    i.append(0)
                    i.append(i[2])
                else:
                    k = []
                    for b in m:
                        k.append(L[b][4])
                    y=max(k)
                    i.append(y)
                    i.append(y+i[2])
            return L
        def get_project_ccompletion_time(L):
            T=[]
            for i in L:
                T.append(i[4])
            return (max(T),L)
        def backword_path(P,L):
            for i in L:
                m = get_search_backword(i[1],L[0:L.index(i)+1])
                if len(m) ==0:
                    i.append(P-i[2])
                    i.append(P)
                else:
                    k = []
                    for b in m:
                        k.append(L[b][5])
                    y=min(k)
                    i.append(y-i[2])
                    i.append(y)
            return L
        def get_slack(L):
            k =[]
            L=forword_path(L)
            L=get_project_ccompletion_time(L)
            m=L[0]
            L[1].reverse()
            L=backword_path(L[0],L[1])
            L.reverse()
            for i in L:
                i.append(i[6]-i[4])
            for j in L:
                if j[7]==0:
                    k.append([j[0],j[1]])
            return (k,L,m)
        def get_critical_path(L):
            k = get_slack(L)
            Label1=Label(output_frame,text='Activities',background='#146054',foreground="white", font=("bold", 14,))
            Label1.place(x=200,y=10, anchor= CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=i[0],background='#146054',foreground="white", font=("bold", 14,))
                Label1.place(x=200,y=30+20*j,anchor= CENTER)
                j+=1
            Label2=Label(output_frame,text='Duration',background='#146054',foreground="white", font=("bold", 14,))
            Label2.place(x=350,y=10, anchor= CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[1]),background='#146054',foreground="white", font=("bold", 14,))
                Label1.place(x=350,y=30+20*j,anchor= CENTER)
                j+=1
            Label3=Label(output_frame,text='precedence',background='#146054',foreground="white", font=("bold", 14,))
            Label3.place(x=500,y=10, anchor= CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=i[2],background='#146054',foreground="white", font=("bold", 14,))
                Label1.place(x=500,y=30+20*j,anchor= CENTER)
                j+=1
            Label4=Label(output_frame,text='Earlest Start',background='#146054',foreground="white", font=("bold", 14,))
            Label4.place(x=650,y=10,anchor= CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[3]),background='#146054',foreground="white", font=("bold", 14,))
                Label1.place(x=650,y=30+20*j,anchor= CENTER)
                j+=1
            Label5=Label(output_frame,text='Latest Start',background='#146054',foreground="white", font=("bold", 14,))
            Label5.place(x=800,y=10,anchor= CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[4]),background='#146054',foreground="white", font=("bold", 14,))
                Label1.place(x=800,y=30+20*j,anchor= CENTER)
                j+=1
            Label6=Label(output_frame,text='Earlest Finish',background='#146054',foreground="white", font=("bold", 14,))
            Label6.place(x=950,y=10,anchor= CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[5]),background='#146054',foreground="white", font=("bold", 14,))
                Label1.place(x=950,y=30+20*j,anchor= CENTER)
                j+=1
            Label7=Label(output_frame,text='Latest Finish',background='#146054',foreground="white", font=("bold", 14,))
            Label7.place(x=1100,y=10, anchor= CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[6]),background='#146054',foreground="white", font=("bold", 14,))
                Label1.place(x=1100,y=30+20*j,anchor= CENTER)
                j+=1
            Label8=Label(output_frame,text='Slack',background='#146054',foreground="white", font=("bold", 14,))
            Label8.place(x=1250,y=10, anchor= CENTER)
            j=1
            for i in k[1]:
                Label1=Label(output_frame,text=str(i[7]),background='#146054',foreground="white", font=("bold", 14,))
                Label1.place(x=1250,y=30+20*j,anchor= CENTER)
                j+=1
            Label8=Label(output_frame,text='The project completion time is ',background='#146054',foreground="white", font=("bold", 14,))
            Label8.place(x=400,y=45+20*j, anchor= CENTER)
            Label9=Label(output_frame,text=str(k[2])+'   unit time',background='#146054',foreground="white", font=("bold", 14,))
            Label9.place(x=600,y=45+20*j, anchor= CENTER)
            Label10=Label(output_frame,text='The critical path is',background='#146054',foreground="white", font=("bold", 14,))
            Label10.place(x=400,y=75+20*j, anchor= CENTER)
            def get_substrings(s):
                 global l
                 if s not in l:
                     l.append(s)
                 if len(s)>1:
                     for j in range(len(s)-1):
                         get_substrings(s[0:len(s)-j-1]+s[len(s)-j:len(s)])
                         get_substrings(s[1:len(s)])
            global l
            print(k[0])
            l = []
            M=[]
            S=[]
            for f in k[0]:
                if f[0] in S:
                    pass
                else:
                    S.append(f[0])
                if f[1] in S:
                    pass
                else:
                    S.append(f[1])
            S = sorted(S)
            s=''
            for f in S:
                s+=str(f)
            
            get_substrings(s)
            def is_valid(K,x):
                for i in range (len(x)-1):
                    if [int(x[i]),int(x[i+1])] in K:
                        pass
                    else:
                        return False
                return True
                   
            for f in l:
                if is_valid(k[0],f)==True and(len(f)>1):
                    M.append(f)
            ends_point_list =S.copy()
            start_point_list = S.copy()
            for f in k[0]:
                if str(f[0]) in s and f[0] in ends_point_list:
                    ends_point_list.remove(f[0])
            
            for f in k[0]:
                if str(f[1]) in s and f[1] in start_point_list:
                    start_point_list.remove(f[1])    
            N=[]
            for f in M:
                if int(f[-1]) in ends_point_list and int(f[0]) in start_point_list:
                    N.append(f)
                                                
            print(N)
            D=0
            for i in N:
                y = 0
                Q=0
                for n in range(len(i)):
                    if n!=0 and n!=len(i)-1:
                        Label41=Label(output_frame,text=i[n]+'--->',background='#146054',foreground="white", font=("bold", 14,))
                        Label41.place(x=600+50*n+D*75*len(i),y=75+20*j, anchor= CENTER)
                    elif n==0:
                        Label11=Label(output_frame,text=i[n]+'--->',background='#146054',foreground="white", font=("bold", 14,))        
                        Label11.place(x=600+50*n+D*75*len(i),y=75+20*j, anchor= CENTER)
                    elif n==len(i)-1:
                        Label31=Label(output_frame,text=i[n],background='#146054',foreground="white", font=("bold", 14,))
                        Label31.place(x=600+50*n+D*75*len(i)-20,y=75+20*j, anchor= CENTER)
                if i !=N[-1]:
                    Label31=Label(output_frame,text='OR',background='#146054',foreground="white", font=("bold", 14,))
                    Label31.place(x=600+50*n+10+D*75*len(i),y=75+20*j, anchor= CENTER)
                    D+=1
                        
                

            
            drawing_button = Button(output_frame,text="Showing the Drawing",command=lambda:sit_open(drawing_frame),background='#146054',foreground="white", font=("bold", 16,))
            drawing_button.place(x=400,y=115+20*j, anchor= CENTER)
            return k[0]
        k=get_critical_path(L)
    e= int(entry_00.get())
    Label_1=Label(AOA_frame,text='FROM NODE',background='#146054',foreground="white", font=("bold", 12,))
    Label_3=Label(AOA_frame,text='Duration',background='#146054',foreground="white", font=("bold", 12,))
    Label_2=Label(AOA_frame,text='TO NODE',background='#146054',foreground="white", font=("bold", 12,))
    Label_1.place(x=500,y=0,anchor=NW)
    Label_2.place(x=620,y=0,anchor=NW)
    Label_3.place(x=740,y=0,anchor=NW)
    entries=[]
    for i in range(0,e):
        subentries=[]
        for j in range(3):
            subentries.append(Entry(AOA_frame))
        entries.append(subentries)
    for i in range(0,e):
        for j in range(3):
            entries[i][j].place(x=500+j*100,y=25*i+40,anchor=NW)
    b=Button(AOA_frame,text="Start Calculations",command=lambda:sit_open(output_frame),background='#146054',foreground="white", font=("bold", 16,))
    b.place(x=550,y=25*i+100,anchor=NW)
def Crashinput():
    def sit_open(frame):
        frame.tkraise()
        if frame==output_frame:
            TakeInput()
    def TakeInput():
        L=[]
        for i in entries:
            sub_L=[]
            n=0
            for j in i:
                sub_L.append(int(j.get()))
            L.append(sub_L)
        import itertools
        def get_slope(L):
            for i in L:
                if (i[2]-i[4])!=0:
                    i.append((i[5]-i[3])/(i[2]-i[4]))
                else:
                    i.append(0)
        def get_search(M,N):
            k =[]
            for j in N:
                if M==j[1]:
                    k.append(N.index(j))
            return k
        def get_search_backword(M,N):
            k =[]
            for j in N:
                if M==j[0]:
                    k.append(N.index(j))
            return k
            
            
        def forword_path(L):
            for i in L:
                m=get_search(i[0],L[0:L.index(i)+1])
                if len(m) ==0:
                    i.append(0)
                    i.append(i[2])
                else:
                    k = []
                    for b in m:
                        k.append(L[b][8])
                    y=max(k)
                    i.append(y)
                    i.append(y+i[2])
            return L
        def get_project_ccompletion_time(L):
            M=forword_path(L)
            T=[]
            for i in M:
                T.append(i[8])
            return (max(T),M)
        def backword_path(P,L):
            for i in L:
                m = get_search_backword(i[1],L[0:L.index(i)+1])
                if len(m) ==0:
                    i.append(P-i[2])
                    i.append(P)
                else:
                    k = []
                    for b in m:
                        k.append(L[b][9])
                    y=min(k)
                    i.append(y-i[2])
                    i.append(y)
            return L
        def get_slack(L):
            k =[]
            L=get_project_ccompletion_time(L)
            L[1].reverse()
            L = backword_path(L[0],L[1])
            L.reverse()
            for i in L:
                i.append(i[10]-i[8])
            for j in L:
                if j[11]==0:
                    k.append(L.index(j))
            return (k,L)
        def get_find(n,L):
            for i in L:
                if i[0]==n:
                    return i[1]
        def duplicate2dList(oldList):
            newList = []
        
            for l in oldList:
                newList.append(l[:])
        
            return newList
        def get_crossponding_k(i,k):
            m = []
            for j in k:
                if j[0]==i:
                    m.append(j[1])
            return m
        def get_crossponding_ulist(u,k):
            m = []
            for i in k:
                if i[0] ==u:
                    m.append(i[2])
            return m
        def is_still_exist(b,L):
            exist = True
            for i in b:
                if L[i][2]<L[i][4]:
                    return False
            return exist
                
        def get_the_Crashed_schedual(L):
            t=1
            Q=[]
            while t==1:
                t=-1
                M = duplicate2dList(L)
                P = get_project_ccompletion_time(M)
                M = duplicate2dList(L)
                s = get_slack(M)
                M = duplicate2dList(L)
                k =[]
                K = []
                H = []
                for h in range(1, len(s[0])+1):
                    for subset in itertools.combinations(s[0], h):
                        H.append(subset)
                for i in H:
                    u = 0
                    y= []
                    u_list=[]
                    for j in i:
                        u+=L[j][6]
                        u_list.append((L[j][6]))
                        y.append(j)        
                    k.append([u,y,u_list])
                    K.append(u)
                K.sort()
                for i in K:
                    n = get_crossponding_k(i,k)
                    for b in n:
                        for j in b:
                            L[j][2]=L[j][2]-1
                        M = duplicate2dList(L)
                        p = get_project_ccompletion_time(M)
                        if p[0] ==P[0]-1 and is_still_exist(b,M)==True:
                            for j in b:
                                    L[j][3]=L[j][3]+ L[j][6]
                            M = duplicate2dList(L)
                            break
                        else:
                            for j in b:
                                L[j][2]=L[j][2]+1
                            M = duplicate2dList(L)
                            b=-1
                    if b!= -1:
                        sub_Q=[]
                        for j in b:
                            sub_Q.append((M[j][0],M[j][1]))
                            sub_Q.append(get_project_ccompletion_time(M)[0])  
                        sub_Q.append(M)
                        Q.append(sub_Q)
                        t=1
                        break
            
            m=-1
            for i in range(len(Q)):
                if i%25 ==0:
                    m+=1
                    Label1=Label(output_frame,text='Crashed Activities',background="#127563",foreground="white", font=("bold", 12,))
                    Label1.place(x=600*m,y=0,anchor=NW)
                    j=1
                if len(Q[i])>3:
                    for b in range (0,len(Q[i])-1,2):

                        if b ==len(Q[i])-3:
                            Label1=Label(output_frame,text=str(Q[i][b][0])+'--->'+str(Q[i][b][1]),background="#127563",foreground="white", font=("bold", 12,))
                            Label1.place(x=600*m,y=30+20*j,anchor=NW)
                            j=j+1
                        else:
                            Label1=Label(output_frame,text=str(Q[i][b][0])+'--->'+str(Q[i][b][1])+'  and',background="#127563",foreground="white", font=("bold", 12,))
                            Label1.place(x=600*m,y=30+20*j,anchor=NW)
                            j=j+1
                else:
                        Label1=Label(output_frame,text=str(Q[i][0][0])+'--->'+str(Q[i][0][1]),background="#127563",foreground="white", font=("bold", 12,))
                        Label1.place(x=600*m,y=30+20*j,anchor=NW)
                        j+=1
            m=-1
            for i in range (len(Q)):
                if i%25 ==0:
                    m+=1
                    Label2=Label(output_frame,text='Number of weeks\nthat crashed',background="#127563",foreground="white", font=("bold", 12,))
                    Label2.place(x=150+600*m,y=0,anchor=NW)
                    j=1
                    n=Q[0][1]+1
                if len(Q[i])>3:
                        if i ==0:
                            Label1=Label(output_frame,text=str(1),background="#127563",foreground="white", font=("bold", 12,))
                            Label1.place(x=150+600*m,y=30+20*j,anchor= NW)
                            j=j+(1+((len(Q[i])-3)/2))
                        else:
                            Label1=Label(output_frame,text=str(Q[i-1][1]-Q[i][1]),background="#127563",foreground="white", font=("bold", 12,))
                            Label1.place(x=150+600*m,y=30+20*j,anchor= NW)
                            j=j+(1+((len(Q[i])-3)/2))
                else:
                        if i ==0:
                            Label1=Label(output_frame,text=str(1),background="#127563",foreground="white", font=("bold", 12,))
                            Label1.place(x=150+600*m,y=30+20*j,anchor= NW)
                            j=j+(1+((len(Q[i])-3)/2))
                        else:
                            Label1=Label(output_frame,text=str(Q[i-1][1]-Q[i][1]),background="#127563",foreground="white", font=("bold", 12,))
                            Label1.place(x=150+600*m,y=30+20*j,anchor= NW)
                            j+=1
            m=-1
            for i in range(len(Q)):
                    if i%25 ==0:
                        m+=1
                        Label3=Label(output_frame,text='Total Duration',background="#127563",foreground="white", font=("bold", 12,))
                        Label3.place(x=300+600*m,y=0,anchor=NW)
                        j=1

                    if len(Q[i])>3:
                        Label1=Label(output_frame,text=str(Q[i][1]),background="#127563",foreground="white", font=("bold", 12,))
                        Label1.place(x=300+600*m,y=30+20*j,anchor=NW)
                        j=j+(1+((len(Q[i])-3)/2))
                    else:
                        Label1=Label(output_frame,text=str(Q[i][1]),background="#127563",foreground="white", font=("bold", 12,))
                        Label1.place(x=300+600*m,y=30+20*j,anchor=NW)
                        j+=1
            m=-1
            for i in range(len(Q)):
                if i%25 ==0:
                    m+=1
                    Label4=Label(output_frame,text='Direct Cost',background="#127563",foreground="white", font=("bold", 12,))
                    Label4.place(x=450+600*m,y=0,anchor=NW)
                    j=1
                if len(Q[i])>3:
                    Sum=0
                    for b in Q[i][-1]:
                        Sum+=b[3]
                    Label1=Label(output_frame,text=str(Sum),background="#127563",foreground="white", font=("bold", 12,))
                    Label1.place(x=450+600*m,y=30+20*j,anchor=NW)
                    j=j+(1+((len(Q[i])-3)/2))
                else:
                    Sum=0
                    for b in Q[i][-1]:
                        Sum+=b[3]
                    Label1=Label(output_frame,text=str(Sum),background="#127563",foreground="white", font=("bold", 12,))
                    Label1.place(x=450+600*m,y=30+20*j,anchor=NW)
                    j+=1
        get_slope(L)
        Q=get_the_Crashed_schedual(L)
    e= int(entry_000.get())
    Label_1=Label(Crash,text='FROM NODE',background='#146054',foreground="white", font=("bold", 12,))
    Label_3=Label(Crash,text='NORMAL TIME',background='#146054',foreground="white", font=("bold", 12,))
    Label_2=Label(Crash,text='TO NODE',background='#146054',foreground="white", font=("bold", 12,))
    Label_4=Label(Crash,text='NORMAL COST',background='#146054',foreground="white", font=("bold", 12,))
    Label_5=Label(Crash,text='CRASH TIME',background='#146054',foreground="white", font=("bold", 12,))
    Label_6=Label(Crash,text='CRASH COST',background='#146054',foreground="white", font=("bold", 12,))
    Label_7=Label(Crash,text='         ')
    Label_1.place(x=300,y=0,anchor=NW)
    Label_2.place(x=420,y=0,anchor=NW)
    Label_3.place(x=540,y=0,anchor=NW)
    Label_4.place(x=660,y=0,anchor=NW)
    Label_5.place(x=780,y=0,anchor=NW)
    Label_6.place(x=900,y=0,anchor=NW)
    Label_7.place(x=1020,y=0,anchor=NW)
    entries=[]
    for i in range(0,e):
        subentries=[]
        for j in range(6):
            subentries.append(Entry(Crash))
        entries.append(subentries)
    for i in range(0,e):
        for j in range(6):
            entries[i][j].place(x=300+j*120,y=25*i+40,anchor=NW)
    b=Button(Crash,text="Start Calculations",command=lambda:sit_open(output_frame),background='#146054',foreground="white", font=("bold", 16,))
    b.place(x=580,y=25*i+100,anchor=NW)

# Initialize the main window using Tkinter with a specific geometry
window = Tk()
window.geometry('1366x768')



def site_open(frame):
    frame.tkraise()
    if frame==input_frame:
        takeinput()
    elif frame==AOA_frame:
        AOAinput()
    elif frame==Crash:
        Crashinput()
def close():
    window.destroy()
# Define multiple frames for different parts of the application
start_frame = Frame(window)
setting_frame = Frame(window)
input_frame = Frame(window)
output_frame = Frame(window)
drawing_frame = Frame(window)
# Additional frames for different settings and input methods
setting_frame_2 = Frame(window)
AOA_frame = Frame(window)
setting_frame_3 = Frame(window)
Crash = Frame(window)
# Stacking all frames on top of each other, where only one is visible at a time
for frame in (start_frame, setting_frame, input_frame, output_frame, setting_frame_2, AOA_frame, Crash, setting_frame_3, drawing_frame):
    frame.grid(row=0, column=0, sticky='news')
from PIL import ImageTk
canvas = Canvas(start_frame,width = 1366, height =768 , bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file = 'path\proj3.png')
canvas.create_image(0, 0, image = image, anchor =NW)
canvas_2 = Canvas(setting_frame,width = 1366, height =768 , bg = 'blue')
canvas_2.pack(expand = YES, fill = BOTH)
image_2 = ImageTk.PhotoImage(file = 'path\proj3.png')
canvas_2.create_image(0, 0, image = image_2, anchor =NW)
canvas_3 = Canvas(setting_frame_2,width = 1366, height =768 , bg = 'blue')
canvas_3.pack(expand = YES, fill = BOTH)
image_3 = ImageTk.PhotoImage(file = 'path\proj3.png')
canvas_3.create_image(0, 0, image = image_3, anchor =NW)
canvas_4 = Canvas(setting_frame_3,width = 1366, height =768 , bg = 'blue')
canvas_4.pack(expand = YES, fill = BOTH)
image_4 = ImageTk.PhotoImage(file = 'path\proj3.png')
canvas_4.create_image(0, 0, image = image_4, anchor =NW)
canvas_0 = Canvas(input_frame,width = 1366, height =768 , bg = 'blue')
canvas_0.pack(expand = YES, fill = BOTH)
image_0 = ImageTk.PhotoImage(file = 'path\proj3.png')
canvas_0.create_image(0, 0, image = image_0, anchor =NW)
canvas_5 = Canvas(AOA_frame,width = 1366, height =768 , bg = 'blue')
canvas_5.pack(expand = YES, fill = BOTH)
image_5 = ImageTk.PhotoImage(file = 'path\proj3.png')
canvas_5.create_image(0, 0, image = image_5, anchor =NW)
canvas_6 = Canvas(Crash,width = 1366, height =768 , bg = 'blue')
canvas_6.pack(expand = YES, fill = BOTH)
image_6 = ImageTk.PhotoImage(file = 'path\proj3.png')
canvas_6.create_image(0, 0, image = image_6, anchor =NW)
canvas_7 = Canvas(output_frame,width = 1366, height =768 , bg = 'blue')
canvas_7.pack(expand = YES, fill = BOTH)
image_7 = ImageTk.PhotoImage(file = 'path\proj3.png')
canvas_7.create_image(0, 0, image = image_7, anchor =NW)
w = Canvas(drawing_frame, width=1366, height=768, bg='white')
w.pack(expand = YES, fill = BOTH)
image_w = ImageTk.PhotoImage(file = 'path\proj3.png')
w.create_image(0, 0, image = image_w, anchor =NW)
button_1=Button(canvas,text='  ACTIVITY ON NODE',width=20,height=2,command=lambda:site_open(setting_frame),background='#127563',foreground="white", font=('bold',16,))
button_2=Button(canvas,text='  ACTIVITY ON ARC',width=20,height=2,command=lambda:site_open(setting_frame_2),background='#127563',foreground="white", font=("bold", 16,))
button_3=Button(canvas,text='  PROJECT CRASHING',width=20,height=2,command=lambda:site_open(setting_frame_3),background='#127563',foreground="white", font=("bold", 16,))
button_4=Button(canvas,text='  Exit',width=20,height=2, command=close,background='#127563',foreground="white", font=("bold", 16,))
button_1.place(x=2, y=367, anchor=SW)
button_2.place(x=2, y=434, anchor=SW)
button_3.place(x=2, y=501, anchor=SW)
button_4.place(x=2, y=568, anchor=SW)
Label_0=Label(setting_frame,text='Please enter number of activities',background='#127563',foreground="white", font=("bold", 16, ))
Label_0.place(x=485,y=588,anchor=SW)
Label_00=Label(setting_frame_2,text='Please enter number of activities',background='#127563',foreground="white", font=("bold", 16, ))
Label_00.place(x=485,y=588,anchor=SW)
Label_000=Label(setting_frame_3,text='Please enter number of activities',background='#127563',foreground="white", font=("bold", 16, ))
Label_000.place(x=485,y=588,anchor=SW)
entry_0=Entry(setting_frame)
entry_0.place(x=585,y=618,anchor=SW)
entry_00=Entry(setting_frame_2)
entry_00.place(x=585,y=618,anchor=SW)
entry_000=Entry(setting_frame_3)
entry_000.place(x=585,y=618,anchor=SW)
button_0=Button(setting_frame,text='Lets Go',command=lambda:site_open(input_frame),background='#127563',foreground="white", font=("bold", 16,))
button_0.place(x=600,y=678,anchor=SW)
button_00=Button(setting_frame_2,text='Lets Go',command=lambda:site_open(AOA_frame),background='#127563',foreground="white", font=("bold", 16,))
button_00.place(x=600,y=678,anchor=SW)
button_000=Button(setting_frame_3,text='Lets Go',command=lambda:site_open(Crash),background='#127563',foreground="white", font=("bold", 16,))
button_000.place(x=600,y=678,anchor=SW)
site_open(start_frame)
# Main loop to run the GUI application
window.mainloop()
