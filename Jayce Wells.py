print ("INSTRUCTIONS: Choose music, then movies, then sports!")

new_list=[]

category= "music", "movies","sports"
print (category)

music= "music"

movies= "movies"

hiphop= "hiphop"

rnb= "r&b"

rock= "rock"

incredibles= "incredibles"

cars= "cars"

shrek= "shrek"

yes= "yes"

basketball= "basketball"

baseball= "baseball"

football= "football"

category_choice = str(input ("music, movies or sports?: "))
if category_choice == music:
    print ("which genre?")
genre= str(input ("hiphop, r&b, or rock?: "))
if genre == hiphop:
    print ("Good choice!")
elif genre == rnb:
    print ("Not as good as hiphop")
elif genre == rock:
    print ("Rock is trash") 

category_choice_two = str(input ("movies or sports?: "))
if category_choice == movies: 
    print ("Which movie?")
movie= str(input ("cars, incredibles or shrek?: "))
if movie == cars: 
    print ("it's decent")
elif movie == incredibles: 
    print ("greatest of all time")
elif movie == shrek:
    print ("it's okay")
    
category_choice_three = str(input ("are sports entertaining?: "))
if category_choice == yes:
    print ("choose a sport")
sport= str(input ("basketball, baseball or football?: "))
if sport == basketball:
    print ("great choice!")
elif sport == baseball:
    print ("not the best")
elif sport == football:
    print ("football is the second best sport")
