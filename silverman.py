#Silverman Score Guide


#The purpose of this program is to assist in the scoring of a newborn infant
#and to determine if it is necessary to wean respiratory support based
#on their respiratory effort, oxygen requirements, and blood gas analysis.


import random


def main():
    
    print("\nSILVERMAN SCORE GUIDE\n")


    answer = input("Do you want to assess a patient? Enter y for yes n for no: ")
    

    while answer.lower() not in ('y', 'n'):
        print()
        answer = input("Incorrect input, please try again. \nDo you want to assess a patient? Enter y for yes n for no.")

    if answer.lower() == 'y': 
        pt_example()
    else:
        print ("Thank you, goodbye.")
        quit()

    main()
    


def pt_example():
    #chest movement
    
    print("\nChest Movement:\n")
    print("Equal = 0"
          "\nProlonged Expiration = 1"
          "\nSeesaw = 2\n")
    chest_movement = silverman_score()
    print("Score Given: " + str(chest_movement))
    while(chest_movement < 0 or chest_movement > 2):
        
        print("Incorrect value; please enter a value from 0 to 2.\n")
        
        chest_movement = silverman_score()
        print("Score Given: " + str(chest_movement) + "\n")
    print("*" *70)

    
    #intercostal retractions
        
    print("\nIntercostal Retractions:\n")
    print("None = 0"
          "\nMinimal = 1"
          "\nMarked = 2\n")
    int_retract = silverman_score()
    print("Score Given: " + str(int_retract))
    while(int_retract < 0 or int_retract > 2):
        
        print("Incorrect value; please enter a value from 0 to 2.\n")
        
        int_retractions = silverman_score()
        print("Score Given: " + str(int_retractions)+ "\n")
    print("*" *70)


    #xiphoidal retractions
        
    print("\nXiphoid Retractions:\n")
    print("None = 0"
          "\nMinimal = 1"
          "\nMarked = 2\n")
    xi_retract = silverman_score()
    print("Score Given: " + str(xi_retract))
    while(xi_retract < 0 or xi_retract > 2):
        
        print("Incorrect value; please enter a value from 0 to 2.\n")
        
        xi_retract = silverman_score()
        print("Score Given: " + str(xi_retract) + "\n")
    print("*" *70)

    #nasal flaring
        
    print("\nNasal Flaring:\n")
    print("None = 0"
          "\nMinimal = 1"
          "\nMarked = 2\n")
    nasal_flare = silverman_score()
    print("Score Given: " + str(nasal_flare))
    while(nasal_flare < 0 or nasal_flare > 2):
        
        print("Incorrect value; please enter a value from 0 to 2.\n")
        
        nasal_flare = silverman_score()
        print("Score Given: " + str(nasal_flare) + "\n")
    print("*" *70)

    #expirtatory grunting
    
    print("\nExpiratory Grunt:\n")
    print("None = 0"
          "\nAudible w/stethescope = 1"
          "\nAudible = 2\n")
    exp_grunt= silverman_score()
    print("Score Given: " + str(exp_grunt))
    while(exp_grunt < 0 or exp_grunt > 2):
        
        print("Incorrect value; please enter a value from 0 to 2.\n")
        
        exp_grunt = silverman_score()
        print("Score Given: " + str(exp_grunt) + "\n")
    print("*" *70)

    
    total = total_score(chest_movement, int_retract, xi_retract, nasal_flare, exp_grunt)

    print()
    print(" >>> SILVERMAN SCORE: " + str(total) + " <<<\n")
    action_req(total)
    print()


def silverman_score():
            
    return random.randint(0,2)
    
        
def total_score(chest_movement, int_retract, xi_retract, nasal_flare, exp_grunt):
    
    total = (chest_movement + int_retract + xi_retract 
            + nasal_flare + exp_grunt)

    return total

def action_req(total):

    if total <=3:
        print("If FIO2 < 30% and BCPAP > 5, wean by 1cmH2O.\n")
        print("If FIO2 > 30%, maintain BCPAP level, reassess in 6 hours.")

    elif total == 4 or total == 5:
        print("Maintain BCPAP level if FIO2 < 30%, consider prone positioning.\n")
        print("If FIO2 > 30% observe x-ray for proper expansion, consider increasing BCPAP by 1, position infant prone.")

    else:
        print("Notify physician, prepare for possible intubation and surfactant delivery.")
 
                        

main()
