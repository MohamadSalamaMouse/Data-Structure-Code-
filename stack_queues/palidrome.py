from deque import dequee
def palindrome_check(sample):
    d1=dequee()
    still_equal=True

    for i in sample:
        d1.add_rear(i)
    while d1.size()>1 and still_equal:
        first=d1.remove_front()
        last=d1.remove_rear()
        if last !=first:
            still_equal=False
        return still_equal
print(palindrome_check('mohamed'))
