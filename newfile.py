


import pandas as pd
import time
import sys
import matplotlib.pyplot as plt
path='/home/world_population.csv'
df=pd.read_csv(path)
a=pd.DataFrame(df)
print('                                      WELCOME TO PROJECT')
print('                                       WORLD POPULATION')
user='''For getting a overview about this project(Press1)-
For seeing all records(Press2)-
TO view population of particular columns or rows(Press3)-
To view mathematical expressions of population(Press4)-
For seeing data in vizualised form(Press5)-
For exit(Press6)-'''
print(user)
while True:
  a=int(input('Enter your choice -'))
  if a==1:
    print('''                                  INTRODUCTION ''')
    print('''This project tells us about change in the population of all countries in the world from 1980 to 2022 and help us to know about population of
different countries by the help of DataFrame and other python programming aspects.''')
    a1='''\n\n To go back to home(Enter1):-
To exit(Enter2):-'''
    print(a1)
    a2=int(input('Enter your choice :-'))
    if a2==1:
      print(user)
    elif a2==2:
      print('''               THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
      break

  elif a==2:
    cc='''To view Population of all countries(Enter1):-
To view Population of all countries in ascending order(Enter2):-
To view Population in of all countries indescending order(Enter3):-'''
    print(cc)

    c=int(input('Enter you choice:-'))
    if c==1:
      print(df)
      print('\n\nTo go back to menu(Enter1):-')
      print('To go back to home (Enter2):-')
      print('To Exit(Enter3):-')
      c8=int(input('Enter your choice :-'))
      if c8==1:
        print(cc)
      elif c8==2:
        print(user)
      elif c8==3:
        print('''              THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
        break

    elif c==2:
       c1='''To see population in ascending order according to country ranking(Enter1):-
To see population in ascending order according to country name(Enter2):-
To go back to menu(Enter3):-
To go back to home(Enter4):-
To exit(Enter5):-'''
       print(c1)
       d=int(input('Enter your choice:-'))
       if d==1:
        print('Population according To Country Ranking :-')
        print(df.sort_values('Rank'))
        print('To go back to menu (Enter1):-')
        print('To go back to home(Enter2):-')
        print('To exit(Enter3):-')
        d10=int(input('Enter your choice:-'))
        if d10==1:
          print(cc)
        elif d10==2:
          print(user)
        elif d10==3:
          print('''             THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
        break

       elif d==2:
          print('Population according to Country Name :-')
          print(df.sort_values('Country/Territory'))
          print('\n\nTo go back to menu(Enter1):-')
          print('To go back to home(Enter2):-')
          print('To exit(Enter3):-')
          d2=int(input('Enter your choice:-'))
          if d2==1:
            print(cc)
          elif d2==2:
            print(user)
          elif d2==3:
             print('''              THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
          break

       elif d==3:
          print(cc)
       elif d==4:
          print(user)
       elif d==5:
          print('''THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
       break
    elif c==3:
       c2='''To see population in descending order according to country ranking(Enter1):-
To see population in descending order according to country name(Enter2):-
To go back to menu(Enter3):-
To exit(Enter4):-'''

       if d1==1:
         print('Population in descending order according to Country Ranking :-')
         print(df.sort_values('Rank',ascending=False))
         print('\n\nTo go back to menu(Enter1):-')
         print('To go back to home(Enter2):-')
         print('To exit(Enter3):-')
         d20=int(input('Enter your choice:-'))
         if d20==1:
           print(cc)
         elif d20==2:
           print(user)
         elif d20==3:
            print('''              THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
         break

       elif d1==2:
          print('Population in descending order according to Country Name :-')
          print(df.sort_values('Country/Territory',ascending=False))
       elif d1==3:
          print(user)
       elif d1==4:
          print('''          THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
       break

  elif a==3:
    e='''To view population of top ranking countries(Enter1):-
To view population of least ranking countries(Enter2):-
To view population of countries in particular year(Enter3):-
To view only particular column(Enter4):-
To go back to home(Enter5):-
To exit(Enter6):-'''
    print(e)

    e1=int(input('Enter your choice :-'))
    if e1==1:
      n1=int(input('Enter the number of countries :-'))
      df1=df.sort_values('Rank')
      print('Population of top ranking countries :-')
      print(df1.head(n1))
      print('''To go back to menu(Enter1):-
To go back to home(Enter2):-
To exit(Enter3):- ''')

      e2=int(input('Enter your choice:-'))
      if e2==1:
        print(e)
      elif e2==2:
          print(user)
      elif e2==3:
          print('''              THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
      break
    elif e1==3:
        e2=int(input('Enter the year :-'))

        if e2==1970:
          print(df.loc[:,'Rank','Country/Territory','1970 Population'])
        elif e2==1980:
           print(df.loc[:,'Rank','Country/Territory','1980 Population'])
        elif e2==1990:
            print(df.loc[:,'Rank','Country/Territory','1990 Population'])

        elif e2==2000:
            print(df.loc[:,'Rank','Country/Territory','2000 Population'])

        elif e2==2010:
            print(df.loc[:,'Rank','Country/Territory','2010 Population'])

        elif e2==2015:
            print(df.loc[:,'Rank','Country/Territory','2015 Population'])

        elif e2==2020:
            print(df.loc[:,'Rank','Country/Territory','2020 Population'])

        elif e2==2022:
            print(df.loc[:,'Rank','Country/Territory','2022 Population'])

            print('''To go back to menu(Enter1):-
To go back to home (Enter2):-
To exit (Enter3):-''')
            e3=int(input('Enter your choice :-'))
            if e3==1:
              print(e)
            elif e3==2:
              print(user)
            elif e3==3:
              print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
            break
    elif e1==4:
      e4=str(input('Enter column name:-'))
      print(df.loc[:,e4])
      print('''To go back to menu(Enter1):-
To go back to home(Enter2):-
T exit(Enter3):-''')
      e5=int(input('Enter your choice :-'))
      if e5==1:
       print(e)
      elif e5==2:
        print(user)
      elif e5==3:
         print('THANK YOU')
      break
    elif e1==5:
       print(user)
    elif e1==6:

       print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
    break
  elif a==4:
    g='''Mathematical operations on population data :-
1. To show minimum populated country(Enter1):-
2. To show maximum populated country(Enter2):-
3. To show average of all population(Enter3):-
4. To count all records(Enter4):-
5. To calculate median of population (Enter5):-
6. To go back to menu (Enter6):-
7. To exit(Enter7):-'''
    print(g)
    b=int(input('Enter your choice :-'))
    if b==1:
      print('Minimum popul:-')
      print(df.min(axis=1))

      print('\n\nTo go back to menu(Enter1):-')
      print('To go back to home (Enter2):-')
      print('To exit(Enter3):-')
      vv=int(input("Enter your choice"))

      if vv==1:
        print(g)
      elif vv==2:
        print(user)
      elif vv==3:
        print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
      break
    elif b==2:
        print('Maximum population is :-')
        print(df.max(axis=1))
        print('To go back to menu(Enter1):-')
        print('To go back to home (Enter2):-')
        print('To exit(Enter3):-')
        bb=int(input("Enter your choice"))

        if bb==1:
          print(g)
        elif bb==2:
          print(user)
        elif bb==3:
            print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
        break


    elif b==3:
        print('Average population is :-')
        print(df.average(axis=1))
        print('\n\nTo go back to menu(Enter1):-')
        print('To go back to home (Enter2):-')
        print('To exit(Enter3):-')
        gg=int(input("Enter your choice"))

        if gg==1:
          print(g)
        elif gg==2:
            print(user)
        elif gg==3:
            print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
        break



    elif b==4:
        print('Counted records :-')
        print(df.count(axis=1))
        print('To go back to menu(Enter1):-')
        print('To go back to home (Enter2):-')
        print('To exit(Enter3):-')
        hh=int(input("Enter your choice"))

        if hh==1:
          print(g)
        elif hh==2:
           print(user)
        elif hh==3:
            print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
        break


    elif b==5:
        print('Median is :-')
        print(df.median(axis=1))
        print('To go back to menu(Enter1):-')
        print('To go back to home (Enter2):-')
        print('To exit(Enter3):-')
        ff=int(input("Enter your choice"))

        if ff==1:
            print(menu)
        elif ff==2:
            print(user)
        elif ff==3:
            print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
        break


    elif b==6:
        print(user)
    elif b==7:
       print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
    break
  elif a==5:
     ab='''1. To view population in line chart(Enter1):-
2. To view population in bar chart (Enter2):-
3. To go back to home(Enter3):-
4. To exit(Enter4):-'''
     print(ab)
     a4 = int(input("Enter the choice: "))

     if a4 == 1:
       df.plot(linestyle="-.", linewidth=2, label="world population record")
       plt.show()
       print('''To go back to menu(Enter1):-
To go back to home(Enter2):-
To exit(Enter3):-''')
       a5=int(input('Enter your choice :-'))
       if a5==1:
         print(ab)
       elif a5==2:
          print(user)
       elif a5==3:
          print('TH')
          print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
       break


     elif a4 == 2:
           # Added missing parenthesis
        df.bar( color="pink", width=0.8,label='WORLD POPULATION')
        plt.show()
        print('''To go back to menu(Enter1):-
To go back to home(Enter2):-
To exit(Enter3):-''')
        a6=int(input('Enter your choice :-'))
        if a6==1:
          print(ab)
        elif a6==2:
           print(user)
        elif a6==3:
           print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
        break



     elif a4 == 3:
        print(user)
     elif a4==4:
        print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
     break
  elif a==6:
    print('''                THANKYOU FOR VISITING
                                                                                                             MADE BY :-
                                                                                                               CLASS :-
                                                                                                            ROLL NO. :-''')
  break