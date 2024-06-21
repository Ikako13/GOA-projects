#python list
supercarlist1 = ["mercedes," "aston martin," "nissan," "porsche."]
hypercarlist2 = ["koenigsegg," "buggati," "ferrari," "rimac nevera."]
overall3 = print(supercarlist1 + hypercarlist2)

boxingstylelist1 = ["hawk style," "hitman style," "peekaboo style."]
print (len (boxingstylelist1))

mylist = ["ikako", 14, True, 2010, "shuladze"]
print (mylist)

musiclist = ["happy music", "sad music", "hype music"]
print(type(musiclist))

redfruitlist = ["strawberries", "cherries", "red apple", "watermelon"]
yellowfruitlist = ["banana", "yellow watermelon", "mango", "pineapple"]
bluefruitlist = ["blue berry", "grape", "passion fruit"]
print(yellowfruitlist, redfruitlist, bluefruitlist)

#accees list item
fruitlist = ["strawberrie", "watermelon", "pineapple"]
print(fruitlist[1])

georgianfoodlist = ["khinkali", "xachapuri", "lobiani", "kubdari"]
print(georgianfoodlist[-1])

swordlist = ("longsword", "katana", "cavalry sabre", "mini katana")
print(swordlist[2:4])

bestcountrylist = ["georgia", "switcerland", "sweden", "japan", "canada", "australia", "spain"]
print(bestcountrylist[-3:-1])

sportlist = ("football", "basketball", "hockey", "baseball", "rugby")
print(sportlist[3:])

#change list item
biggestcountrylist = ["russia", "canada" "usa" "china",]
biggestcountrylist[1:2] = ("brazil", "sweden")
print(biggestcountrylist)

smallestcountrylist = ["vatican" "armenia" "azerbaijan" "georgia"]
smallestcountrylist[-1:2] = ("San marino", "monaco", "Liechtenstein",)
print (smallestcountrylist)

biggestwarlist = ["WW2", "WW1", "chinese civil war"]
biggestwarlist.insert (2, "taping rebelion",)
print (biggestwarlist)

georgiankinglist = ["tamar king", "david fourth", "david firs"]
georgiankinglist.insert (-3, "michael third" "bagration")
print (georgiankinglist)