import pandas as pd

#import forecast2024.csv from directory

past_present = pd.read_csv("forecast2024.csv")

#conversion function
def convert_to_celsius(faren_temp: int) -> int:
    return round(((faren_temp-32) * 5.0/9.0), 2)

def main():

    active = True
    while active:
        # Ask user for Month, then Day in MM:DD format

        user_date = input("Enter a date in 'MM-DD' format: ")

        user_date = "2024-"+user_date

        if user_date in past_present["ds"].values:
            predicted_temp = past_present[past_present["ds"]==user_date]["yhat"].values[0]
            predicted_temp = round(predicted_temp, 2)
            format_decided = False
            format = ""
            while format_decided == False:
                temp_format = input("Which do you prefer (Type 'F' or 'C'): ")
                if temp_format.upper() == 'F' or temp_format.upper() == 'C':
                    format = temp_format
                    format_decided = True
            
            if format == 'C':
                predicted_temp = convert_to_celsius(predicted_temp)
            print(f"Prediction for {user_date}: {predicted_temp} {format} ")
        else:
            print("Invalid Date! Are you sure your formatting is correct?")
    
        user_continue = input("Continue predicting?: ('y' or 'n')")
        if user_continue == 'n':
            active = False
    
    print("Thanks For a Wonderful Opportunity to Showcase My Skills!\nHave a great rest of your day!")
    
        
if __name__ == "__main__":
    main()

