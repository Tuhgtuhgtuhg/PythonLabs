from  modulesPROKOPENKO import quickSort,findElem, findFiveMax, findFiveMin, findListInList, average,deleteClone
mainList = [13,9,8,4,5,6,6,7,8,9]
listForFind = [6,6,7]


print("Відсортований список " + str(mainList) + ": " + str(quickSort(mainList)))
print("Пошук елемента зі значенням \" 5 \" у списку " + str(mainList))
print("Індекс цього елемента у списку: " + str(findElem(5,mainList)))
print("Пошук елемента зі значенням \" 666 \" у списку " + str(mainList) )
print("Індекс цього елемента у списку: " + str(findElem(666,mainList)))
print("Пошук cписку "+str(listForFind)+ " у списку " + str(mainList))
print("Індекс початку шуканого списку  у головному списку: " + str(findListInList(mainList,listForFind)))
print("Пошук cписку "+str([65,54,78])+ " у списку " + str(mainList))
print("Індекс початку шуканого списку  у головному списку: " + str(findListInList(mainList,[65,54,78])))
print("5 максимальних елементів із списку"+str(mainList)+": "+ str(findFiveMax(mainList)))
print("5 максимальних елементів із списку"+str(listForFind)+": "+ str(findFiveMax(listForFind)))
print("5 мінімальних елементів із списку"+str(mainList)+": "+ str(findFiveMin(mainList)))
print("5 мінімальних елементів із списку"+str(listForFind)+": "+ str(findFiveMin(listForFind)))
print("Середнє арифметичне списку" +str(mainList)+": " + str(average(mainList)))
print("Середнє арифметичне списку" +str([])+": " + str(average([])))
print("Список" + str(mainList)+" без \"повторів\": "+str(deleteClone(mainList)))

