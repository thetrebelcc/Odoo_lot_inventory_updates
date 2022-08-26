
lotty = 'thisisalot1234'

lotty_product_location = models.execute_kw(db, uid, password, 'stock.quant', 'search_read', [['&', ['lot_id', '=', lotty],['on_hand','=',True]]])

for i in lotty_product_location:
        print("{0} - {1} - {2}".format(i['location_id'][1],i['product_id'][1],i['quantity']))
        update_qty = models.execute_kw(db, uid, password, 'stock.quant', 'write', [[product_location[0]['id']], {'available_quantity': '0','quantity': '0'}])
        print(update_qty)
        
print('done')
