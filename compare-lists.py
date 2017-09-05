# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

yesOrNo = 0
if (len(list_one) != len(list_two)):
    print "The lists are not the same"
else:
    for i in range(0, len(list_one)):
        if (list_one[i] != list_two[i]):
            yesOrNo += 1
            break
    if (yesOrNo > 0):
        print "The lists are not the same"
    else:
        print "The lists are the same"
        