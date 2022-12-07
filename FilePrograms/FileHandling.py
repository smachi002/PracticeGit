def priceCheck(products, productPrices, productSold, soldPrice):
    D = {}
    D1 = {}
    count = 0
    for i in range(0, len(products)):
        key = products[i]
        D[key] = productPrices[i]
    print(D)
    for i in range(0, len(productSold)):
        key1 = productSold[i]
        D1[key1] = soldPrice[i]
    print(D1)

    for i in range(0, len(productSold)):
        for key in D.keys():
            if key == productSold[i]:
                if soldPrice[i] == D[key]:
                    continue
                else:
                    count = count + 1
                    return count


if __name__ == '__main__':
    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.20, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29]
    result = priceCheck(products, productPrices, productSold, soldPrice)
    print(result)