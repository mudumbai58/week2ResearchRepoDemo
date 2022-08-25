oddMonths = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
evenMonths = ['April','June', 'September', 'November']
February ='February'
presentMonth = input('Enter the month: ')
if (presentMonth in oddMonths): print("31 days in this month")
elif (presentMonth in evenMonths): print('30 days in this month')
elif (presentMonth == February): print('28/29 days in this month')
else : print('Invalid Entry') 



 