hook = "You are walking through the woods with the queen's precious cargo. You hear a loud thump in the trail in front of you. " \
"What do you do? a. Run and hide, b. Turn around couragously, c. Run towards the noise as fast as possible. "

decision_a = "You hide behind a tree and fall into a reality warping rabbit hole. You land on Tatoonine. What do you do? " \
"D. Get on a pad racer, E. Call for help, F. Sit there and cry. "

decision_b = "You face a giant snaggletoothed rat. It is hungry. What do you do? " \
"G. Fight the rat, H. Run and Hide, I. Befriend the rat. "

decision_c = "You find a kind old man who tripped. You help him and he offers you a wish. What do you do? J. Run and hide, " \
"K. Ask about the conditions of the wish, L. You wish for some BYU Creamery Chocolate Milk. "

decision_d = "You are challenged to a race. What do you do? M. Win the race, N. Lose the race. "
decision_e = "Sand people come to eat you. What do you do? O. Fight, P. Run and hide "
decision_f = "You keep crying. What do you do? Q. Cry more, R.Stop crying "

decision_g = "You die from the rat. You lose. Try again."
decision_h = decision_a
decision_i = "The rat is now your bestie. You return to the cargo and both bring it back to the queen to live " \
"happily ever after with your best friend the Rat. You win."

decision_j = decision_a
decision_k = "The old man gets angry and poofs you out of exisitence. You loose. Try again."
decision_l = "You receive a nice cold glass of BYU chocolate milk. You win"

decision_m = "You win."
decision_n = "You crash badly on your racer and pass away suddenly in a flash of flames. You loose. Try again."

decision_o = "You cannot continue on like this anymore and die from dehydration. You loose. Try again"
decision_p = "You run and hide but fall down another magical rabbit hole. You land right by you cargo, deliver it to the queen, and live happily ever after. You win!"

decision_q = decision_n
decision_r = decision_m


decision = input(hook)  # Collect the decision from the user
decision = decision.upper()

decision2 = ""
if decision == "A":
    decision2 = input(decision_a)
elif decision == "B":
    decision2 = input(decision_b)
elif decision == "C":
    decision2 = input(decision_c)
else:
    print("You are dead. (Unless you enter A, B, or C next time around XP)")


if decision == "A" or decision == "B" or decision == "C":
    decision2 = decision2.upper()

    if decision2 == "D":
        decision3 = input(decision_d)
    elif decision2 == "E":
        decision3 = input(decision_e)
    elif decision2 == "F":
        decision3 = input(decision_f)
    elif decision2 == "G":
        decision3 = input(decision_g)
    elif decision2 == "H":
        decision3 = input(decision_h)
    elif decision2 == "I":
        decision3 = input(decision_i)
    elif decision2 == "J":
        decision3 = input(decision_j)
    elif decision2 == "K":
        print(decision_k)
    elif decision2 == "L":
        print(decision_l)
    else:
        print("You are dead. (Unless you enter a valid letter choice next time around XP)")

    if decision2 == "D" or decision2 == "E" or decision2 == "F" or decision2 == "G" or decision2 == "H" or decision2 == "I" or decision2 == "J" or decision2 == "K" or decision2 == "L":
        decision3 = decision3.upper()

        if decision3 == "M":
            print(decision_m)
        elif decision3 == "N":
            print(decision_n)
        elif decision3 == "O":
            print(decision_o)
        elif decision3 == "P":
            print(decision_p)
        elif decision3 == "Q":
            print(decision_q)
        elif decision3 == "R":
            print(decision_r)
        else:
            print("You are dead. (Unless you enter a valid letter choice next time around XP)")
