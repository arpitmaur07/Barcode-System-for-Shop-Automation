import mysql.connector as connector

class Operation:
    
    def __init__(self) :
        self.con=connector.connect(host='localhost',port='3306',user='root',password='root',database='barcode')

        query='create table if not exists Products(ProductID int primary key, ProductName varchar(150),Colour varchar(50),Description varchar(300),Quantity int)'
        
        cur=self.con.cursor()
        cur.execute(query)
        # print('Table Created.')
        
        
    
    # Function for add new Products in database.    
    def addProduct(self,productID,productName,colour=None,description=None,quantity=1):
        if productID!=None:
            query=f'SELECT COUNT(ProductID) FROM Products WHERE ProductID = {productID}'
            cur=self.con.cursor()
            cur.execute(query) 
            records = cur.fetchall()
            if records[0][0]>0:
                print('This Id is already exist.')
                return False
            else:  
                if productName!=None:
                    query=f"insert into Products(ProductID,ProductName,Colour,Description,Quantity) values({productID},'{productName}','{colour}','{description}',{quantity})"
                    cur=self.con.cursor()
                    cur.execute(query)
                    self.con.commit()
                    print(f'Product {productName} with {quantity} quantity is saved in Database.')
        else:
            print('Product Id is required.')
        
        
    
    # Function for access the Product details from database.    
    def showAllProducts(self):
        query='select * from Products'  
        cur=self.con.cursor()
        cur.execute(query)
        for count,row in enumerate(cur,1):
            print('No.',count)
            print('Product ID   :', row[0])
            print('Product Name :', row[1])
            print('Colour       :', row[2])
            print('Description  :', row[3])
            print('Quantity     :', row[4])
            print('')
            
            
    
    # Function for access Product details in database using Id.
    def showOneProduct(self,productID=None):
        if productID!=None:
            query=f'SELECT COUNT(ProductID) FROM Products WHERE ProductID = {productID}'
            cur=self.con.cursor()
            cur.execute(query) 
            records = cur.fetchall()
            if records[0][0]>0:
                query=f'select * from Products where ProductID={productID}' 
            else:
                print('This Id is not found.')   
                return 
        else:
            query=f'select * from Products ' 
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print('Product ID   :', row[0])
            print('Product Name :', row[1])
            print('Colour       :', row[2])
            print('Description  :', row[3])
            print('Quantity     :', row[4])
            print('')
            
          
          
    # Function for delete Product from database using Id.        
    def deleteProduct(self,productID):
        query=f'SELECT COUNT(ProductID) FROM Products WHERE ProductID = {productID}'
        cur=self.con.cursor()
        cur.execute(query) 
        records = cur.fetchall()
        if records[0][0]>0:
            query=f'delete from Products where ProductID={productID}'   
            cur=self.con.cursor()
            cur.execute(query)     
            self.con.commit()
            print(f'Product ID {productID} is deleted.')
        else:
            print('Error! ID not found.')    
            
            
          
    # Function for update the Product details in database.
    def updateProduct(self,productID,newProductName=None,newColour=None,newDescription=None,newQuantity=None):
        query=f'SELECT COUNT(ProductID) FROM Products WHERE ProductID = {productID}'
        cur=self.con.cursor()
        cur.execute(query) 
        records = cur.fetchall()
        if records[0][0]>0:
            query=f'select * from Products where ProductID={productID} ' 
            cur=self.con.cursor()
            cur.execute(query)
            for row in cur:
                oldProductName=row[1]
                oldColour=row[2]
                oldDescription=row[3]
                oldQuantity=row[4]  
            if (newProductName !=None)  :
                productName=newProductName
            else:
                productName=oldProductName      
            if (newColour !=None):
                Colour=newColour
            else:
                Colour=oldColour          
            if (newDescription !=None) :
                Description=newDescription
            else:
                Description=oldDescription            
            if (newQuantity !=None) :
                Quantity=newQuantity
            else:
                Quantity=oldQuantity  
            if ((newDescription!=oldDescription and newDescription!=None) or (newProductName!=oldProductName and newProductName!=None) or (newColour!=oldColour and newColour!=None) or (newQuantity!= oldQuantity and newQuantity!=None) ) :
                print(f'{productName} updated successfully!!!')     
            query=f"update Products set ProductName='{productName}',Colour='{Colour}',Description='{Description}',Quantity={Quantity} where ProductID={productID}"
            cur=self.con.cursor()
            cur.execute(query)     
            self.con.commit()
        else:
            print('Thid Id is not found in Database.') 
            return False   