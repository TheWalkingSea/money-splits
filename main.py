import pandas as pd
import numpy as np
SHEETNAME = "Bad Bunny 05-24"



class Person:
    """ Describes a person that money is being split with """
    df: pd.DataFrame = None
    def __init__(self, name: str):
        self.name = name
        self.bal = 0
    
    def add_personals(self) -> None:
        """ Adds profits for personals to self.bal """
        personals = self.df.loc[self.df['Full Name'] == self.name, 'Sale']
        self.bal += np.sum(personals)
    
    def add_expenses(self) -> None:
        """ Adds the expenses to the balance (this is later split in 3 and deducted from self.bal) """
        expenses = self.df.loc[self.df['Cashed Out by'] == self.name, 'Cost']
        self.bal += np.sum(expenses)
    
    def deduct_sales(self) -> None:
        """ Deducts any money made in sales (adds to a pot) and then later it will add the split """
        sales = self.df.loc[self.df['Account Holder'] == self.name, 'Sale']
        self.bal -= np.sum(sales)
    
    def add_split(persons: list['Person']) -> None:
        """ This will add the split from sales and expenses given n Person classes
        
        Parameters:
        (list[Persons])persons: The people that the money is being split between
        
        """
        personsNames: list[str] = [i.name for i in persons]
        notPersonals = ~Person.df['Full Name'].isin(personsNames)
        total_sales = np.sum(Person.df.loc[notPersonals, 'Sale'])
        total_expenses = np.sum(Person.df.loc[notPersonals, 'Cost'])
        for person in persons:
            person.bal += total_sales/len(persons)
            person.bal -= total_expenses/len(persons)



def main():
    xlsx = pd.ExcelFile(r"C:\Users\austi\OneDrive\Documents\profit\tickytickys.xlsx")
    df = pd.read_excel(xlsx, SHEETNAME)
    Person.df = df
    persons = [Person("Vishnu"), Person("Rohit"), Person("Austin")]
    Person.add_split(persons)
    for person in persons:
        person.add_personals()
        person.add_expenses()
        person.deduct_sales()
        print(person.name, "$%s" % (person.bal.round(2)))
    s = sum([i.bal for i in persons])
    if (abs(s) > 1):
        print(f"An error occurred. The sum of balances do not add up\nTotal Sum: ${s}")


if __name__ == "__main__":
    main()