import pandas as pd
import numpy as np
SHEETNAME = "Sheet1"



class Person:
    df: pd.DataFrame = None
    def __init__(self, name: str):
        self.name = name
        self.bal = 0
    
    def add_personals(self):
        """ Adds profits for personals to self.bal """
        personals = self.df.loc[self.df['Name'] == self.name, 'Profit']
        self.bal += np.sum(personals)
    
    def add_expenses(self):
        """ Adds the expenses to the balance (this is later split in 3 and deducted from self.bal) """


def main():
    xlsx = pd.ExcelFile("splits.xlsx")
    df = pd.read_excel(xlsx, SHEETNAME)
    Person.df = df
    persons = [Person("Vishnu"), Person("Rohit"), Person("Austin")]
    for person in persons:
        person.add_personals()


if __name__ == "__main__":
    main()