import helper

products = helper.get("apiproducts")
apiProducts=[]

for p in products:
    print("product=%s" %(p))
    product = helper.get("apiproducts/"+p)
    apiProducts.append(product)

helper.dumpConfig("org/apiProducts.json", apiProducts)
