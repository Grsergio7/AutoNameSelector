# import json
# import random
import os.path

check_file = os.path.exists('names.json')

print(check_file)

# # open json
# try:
#     with open('./names.json') as name_list:
#         data = json.load(name_list)
# except IOError:
#     print("File not found. Please check the path.")
# finally:
#     print("Exit")
  

# def assign_week(w, d, x_names):
#   # Set variables
#   complete_list_video = data['Video']
#   complete_list_all = data['Audio'] + complete_list_video
#   complete_list_av = data['A/V'] + complete_list_video
  
#   # Make local copies of lists
#   video = complete_list_video.copy()
#   all = complete_list_all.copy()
#   av = complete_list_av.copy()
    
#   def rand_choice(group):
#     n = random.randint(0,(len(group) - 1))
#     return group[n]
    
#   # Remove chosen names from all lists
#   if x_names != [""]:
#     for name in x_names:
#       for v in video:
#         if name == v:
#           video.remove(name)
#       for a in all:
#         if name == a:
#           all.remove(name)
#       for c in av:
#         if name == c:
#           av.remove(name)

#   week = []
#   # Assign video
#   vid = rand_choice(video)
#   week.append(vid)
  
#   # Assign audio by checking for duplicates
#   aud = rand_choice(all)
#   if aud in week:
#       while aud in week:
#         aud = rand_choice(all)
#         if aud not in week:
#           week.append(aud)
#           break
#   else:
#     week.append(aud)
  
#   # Assign A/V by checking for duplicates
#   attnt = rand_choice(av)
#   if attnt in week:
#     while attnt in week:
#       attnt = rand_choice(av)
#       if attnt not in week:
#         week.append(attnt)
#         break
#   else:
#     week.append(attnt)

#   # Assign Platform
#   plat = rand_choice(all)
#   if plat in week:
#     while plat in week:
#       plat = rand_choice(all)
#       if plat not in week:
#         week.append(plat)
#         break
#   else:
#     week.append(plat)
    
#   # Assign Mic1 by checking for duplicates
#   mic1 = rand_choice(all)
#   if mic1 in week:
#     while mic1 in week:
#       mic1 = rand_choice(all)
#       if mic1 not in week:
#         week.append(mic1)
#         break
#   else:
#     week.append(mic1)
    
#   # Assign Mic2 by checking for duplicates
#   mic2 = rand_choice(all)
#   if mic2 in week:
#     while mic2 in week:
#       mic2 = rand_choice(all)
#       if mic2 not in week:
#         week.append(mic2)
#         break
#   else:
#     week.append(mic2)
  
#   # Print out results
#   print("Semana",w, d)
#   print("video:      ", week[0])
#   print("audio:      ", week[1])
#   print("a/v:        ", week[2])
#   print("Plataforma: ", week[3])
#   print("Mic1:       ", week[4])
#   print("Mic2:       ", week[5])

#   week = []


# assign_week(1, "Domingo", [""])
# print("")
# assign_week(1, "Jueves", ["Sergio Ruiz Jr","Alex Mancilla","Alex Romero","Jaime Ojeda"])
# print("")
# assign_week(2, "Domingo", [""])
# print("")
# assign_week(2, "Jueves", ["Adam Nuñez","Sergio Ruiz Jr","Alex Romero"])
# print("")
# assign_week(3, "Domingo", [""])
# print("")
# assign_week(3, "Jueves", ["Alex Romero","Jahaziel Sanchez","James Franco"])
# print("")
# assign_week(4, "Domingo", [""])
# print("")
# assign_week(4, "Jueves", ["Mariano Curiel","Antonio Landeros","Adam Nuñez"])