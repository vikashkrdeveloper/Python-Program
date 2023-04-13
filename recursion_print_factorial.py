# n=5
# product=1#product default value
# for i in range(n):
#     product=product*(i+1)
# print(product)
def factorial_iter(n):
    product=1#product default value
    for i in range(n):
        product=product*(i+1)
    return product
print(factorial_iter(89889))