#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
print ("exercise 2")
price = 24.95
so_luong_sach = 60
ship = (3 + (so_luong_sach - 1) * 0.75)
discounted_price = (price - (price * 0.4)) 
total =  discounted_price * so_luong_sach + ship
print("The total wholse cost for 60 copies are",round(total, 2),"$")
