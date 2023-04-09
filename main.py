import cv2  
import numpy as np
from DBHelper import Operation
from pyzbar.pyzbar import decode

def cam():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    print('Scan your Product Id.')
    
    while(True):
        
        ret, img = cap.read()
        for barcode in decode(img):
            # draw the ractangle around the barcode
            points=np.array([barcode.polygon],np.int32)
            points=points.reshape((-1,1,2))
            cv2.polylines(img,[points],True,(255,0,255),3)
            
            # read data from barcode
            myData=barcode.data.decode('utf-8')
            # print(myData)
            
            if myData!=None:
                cv2.imshow('frame', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    exit()
                
                id=myData
                db=Operation()
                print("********************* WELCOME *********************")
                print()
                print('PRESS 1 to show all Products')
                print('PRESS 2 to show Product by Id')
                print('PRESS 3 to add Product')
                print('PRESS 4 to delete Product')
                print('PRESS 5 to update Product')
                print('PRESS 6 to Exit Program!')
                print()
                try:
                    choice=int(input('Enter your choice: '))
                    if choice==1:
                        db.showAllProducts()
                        print('Scan your Product Id.')
                        
                        
                        
                        
                    elif choice==2:
                        if id=="":
                            set_id=None
                        else:
                            set_id=int(id)
                        db.showOneProduct((set_id))
                        print('Scan your Product Id.')
                        
                        
                        
                        
                    elif choice==3:
                        check=(db.addProduct(id,None))
                        if check==False:
                            print('Update this product details ! if required.')
                            name=input('new Product Name : ')
                            colour=input('new Colour  : ')
                            desc=input('new Description : ')
                            quantity=(input('new Quantity  : '))
                            if name=="":
                                set_name=None
                            else:
                                set_name=name 
                            if desc=="":
                                set_desc=None
                            else:
                                set_desc=desc      
                            if colour=="":
                                set_colour=None
                            else:
                                set_colour=colour
                            if quantity=="":
                                set_quantity=None
                            else:
                                set_quantity=int(quantity)           
                            db.updateProduct(id,newProductName=set_name,newDescription=set_desc,newColour=set_colour,newQuantity=set_quantity) 
                        else:
                            name=input('Product Name : ')
                            colour=input('Colour  : ' ) 
                            desc=input('Description : ')
                            quantity=(input('Quantity  : '))
                            if colour=='':
                                set_colour=None
                            else:
                                set_colour=colour    
                            if desc=="":
                                set_desc=None
                            else:
                                set_desc=desc  
                            if quantity=="" or quantity==0:
                                set_quantity=1  
                            else:
                                set_quantity=int(quantity )
                            db.addProduct(id,name,set_colour,set_desc,set_quantity)
                        print('Scan your Product Id.')

                    
                        
                    elif choice==4:
                        db.deleteProduct(id)
                        print('Scan your Product Id.')
                        
                        
                        
                    elif choice==5:
                        check=db.updateProduct(id)
                        if check==False:
                            print('Are you want to add Product with this Id. "y" for YES and "(any other key)" for NO.')
                            choice=(input('Enter your choice: '))
                            if choice=='y':
                                name=input('Product Name : ')
                                colour=input('Colour  : ')
                                desc=input('Description : ')
                                quantity=(input('Quantity  : '))
                                if colour=='':
                                    set_colour=None
                                else:
                                    set_colour=colour    
                                if desc=="":
                                    set_desc=None
                                else:
                                    set_desc=desc  
                                if quantity=="" or quantity==0:
                                    set_quantity=1  
                                else:
                                    set_quantity=int(quantity )
                                db.addProduct(id,name,set_colour,set_desc,set_quantity)
                            else:
                                print("That's fine.")
                        else:    
                            name=input('new Product Name : ')
                            colour=input('new Colour  : ')
                            desc=input('new Description : ')
                            quantity=(input('new Quantity  : '))
                            if name=="":
                                set_name=None
                            else:
                                set_name=name 
                            if desc=="":
                                set_desc=None
                            else:
                                set_desc=desc      
                            if colour=="":
                                set_colour=None
                            else:
                                set_colour=colour
                            if quantity=="":
                                set_quantity=None
                            else:
                                set_quantity=int(quantity)           
                            db.updateProduct(id,newProductName=set_name,newDescription=set_desc,newColour=set_colour,newQuantity=set_quantity)
                        print('Scan your Product Id.')

                        
                    elif choice==6:
                        exit()
                    else:
                        print('Invalid Input ! Try Again.')
                        
                            
                except Exception as e:
                    print(e)
                    print('Invalid Details ! Try Again')   


        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit()
    cap.release()
    cv2.destroyAllWindows()




def main():
    while True:
        cam()

if __name__=="__main__":
    main()

