#ATM....
n=1
m=1234 
b=50000
print("You have already inserted the card.\n1. English       2. Hindi")
a=int(input('\nChoose the language: '))
if a==1:
    print('\nWelcome to this ATM.\n\n')
    while n>0:
        print('1. Withdraw      2. Deposite\n3. Balance inq   4. Change Pin\n5. Exit')
        cho=int(input('Choose the option: '))
        if cho==1:
            amt=int(input('\nEnter the Amt: '))
            pas=int(input('\nEnter Pin No.'))
            if pas==m :
                if amt<=b :
                        print('Rs',amt,'has been successfully withrawn from your Bank A/C.','Rs',b-amt,'updated balance.','\n\nDo you want to continue the transaction? 1. Yes or 2. No.')
                        bac=int(input('Enter the option: '))
                        if bac==1:
                                b-=amt
                                n+=1
                        else:
                                break
                else:
                        print("You don't have enough balance!\nTry again.\n")
            else:
                print("\nInvalid Pin!")
                bac=int(input('\n\nDo you want to continue the transaction? 1. Yes or 2. No.'))
                if bac==1:
                    n+=1
                else:
                    break    
        if cho==2:
           amt=int(input('\nEnter the Amt: '))
           pas=int(input('\nEnter Pin No.'))
           if pas==m:
               print('Rs',amt,'has been successfully deposited  in your Bank A/C.', 'Rs', b+amt,'updated balance.', '\n\nDo you want to continue the transaction? 1. Yes or 2. No.')
               bac=int(input('\nEnter the option: '))
               if bac==1:
                   b+=amt
                   n+=1
               else:
                    break
           else:
                print("\nInvalid Pin!")
                bac=int(input('\n\nDo you want to continue the transaction? 1. Yes or 2. No.'))
                if bac==1:
                    n+=1
                else:
                    break   
        if cho==3:
            pas=int(input('\nEnter Pin No.'))
            if pas==m:
                print('Your Bank balance is Rs',b)
                bac=int(input('\n\nDo you want to continue the transaction? 1. Yes or 2. No.'))
                if bac==1:
                    n+=1
                else:
                    break
            else:
                print("\nInvalid Pin!")
                bac=int(input('\n\nDo you want to continue the transaction? 1. Yes or 2. No.'))
                if bac==1:
                    n+=1
                else:
                    break    
        elif cho==4:
            pas=int(input('\nEnter Current Pin No.'))
            if pas==m:
                pas=int(input('\nEnter New Pin No.'))
                if len(str(pas))==4:
                    print('Your Pin No. has been changed successfully.')
                    m=pas
                    bac=int(input('\n\nDo you want to continue the transaction? 1. Yes or 2. No.'))
                    if bac==1:
                        n+=1
                    else:
                        break
            else:
                print("\nInvalid Pin!")
                bac=int(input('\n\nDo you want to continue the transaction? 1. Yes or 2. No.'))
                if bac==1:
                    n+=1
                else:
                    break        
        elif cho==5:
            break
elif a==2:
    print('\nIs ATM mein aapka svaagat hai.\n\n')
    while n>0:
        print('1. Nikaalye      2. Jamaa Kijye\n3. Shesh Janye   4. Pin Badalye\n5. Baahar Jaen')
        cho=int(input('Vikalp Chunye: '))
        if cho==1:
            amt=int(input('\nRaashi Darj Karye: '))
            pas=int(input('\nPin No. Darj Krye: '))
            if pas==m :
                if amt<=b :
                        print('Rs',amt,'Aapake Bank Khaate Se Saphalataapoorvak Rupai Nikaal Lya Gaya Hai.','Rs',b-amt,'Shesh Hai.','\n\nKya Aap Len-Den Jaari Rakhanaa Chaahte Hain? 1. Haan or 2. Naa.')
                        bac=int(input('Vikalp Chunye: '))
                        if bac==1:
                                b-=amt
                                n+=1
                        else:
                                break
                else:
                        print("Aapake Pass Paryaaptp Rupai Nahin Hai!\nPunah Prayaas Karen.\n")
            else:
                print("\nAmaanye Pin No.!")
                bac=int(input('\n\nKya Aap Len-Den Jaari Rakhanaa Chaahte Hain? 1. Haan or 2. Naa.'))
                if bac==1:
                    n+=1
                else:
                    break    
        if cho==2:
           amt=int(input('\nRaashi Darj Karye: '))
           pas=int(input('\nPin No. Darj Krye: '))
           if pas==m:
               print('Rs',amt,'Aapake Bank Khaate Mein Saphalataapoorvak Rupai Jamaa Ho Gaya Hai', 'Rs', b+amt,'Shesh Hai.', '\n\nKya Aap Len-Den Jaari Rakhanaa Chaahte Hain? 1. Haan or 2. Naa..')
               bac=int(input('\nVikalp Chunye: '))
               if bac==1:
                   b+=amt
                   n+=1
               else:
                    break
           else:
                print("\nAmaanye Pin No.!")
                bac=int(input('\n\nKya Aap Len-Den Jaari Rakhanaa Chaahte Hain? 1. Haan or 2. Naa.'))
                if bac==1:
                    n+=1
                else:
                    break   
        if cho==3:
            pas=int(input('\nPin No. Darj Krye: '))
            if pas==m:
                print('Aapaka Bank Shesh Hai Rs',b)
                bac=int(input('\n\nKya Aap Len-Den Jaari Rakhanaa Chaahte Hain? 1. Haan or 2. Naa.'))
                if bac==1:
                    n+=1
                else:
                    break
            else:
                print("\nAmaanye Pin No.!")
                bac=int(input('\n\nKya Aap Len-Den Jaari Rakhanaa Chaahte Hain? 1. Haan or 2. Naa.'))
                if bac==1:
                    n+=1
                else:
                    break    
        elif cho==4:
            pas=int(input('\nPin No. Darj Krye: '))
            if pas==m:
                pas=int(input('\nNayaa Pin No. Darj Krye: '))
                if len(str(pas))==4:
                    print('Aapaka Pin No. Saphalataapoorvak Badal Gaya Hai.')
                    m=pas
                    bac=int(input('\n\nKya Aap Len-Den Jaari Rakhanaa Chaahte Hain? 1. Haan or 2. Naa..'))
                    if bac==1:
                        n+=1
                    else:
                        break
            else:
                print("\nAmaanye Pin No.!")
                bac=int(input('\n\nKya Aap Len-Den Jaari Rakhanaa Chaahte Hain? 1. Haan or 2. Naa.'))
                if bac==1:
                    n+=1
                else:
                    break
        else:
            break
            