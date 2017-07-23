#I'll add in the actual silly values:
import time
import random


part1 = ("women are", "Mexico is", "America is", "@FOXANDFRIENDS is", "@CNN is", "Russia is",  "Hillary's emails are", " Obamacare is", "Covfefe is",  "fake news media is", "Jobs are", "Dems are")
#len at 12
part2 = ("bad", "fake", "nasty", "crooked", "rigged", "great", "dumb", "dishonest", "phony", "stupid", "lousy", "lies", "sick", "useless", "loser", "pointless",  "loony", "idiotic", "Crazy", "weak", "dangerous", "huge", "tremendous", "classy", "failing", "mean", "little", "incredible", "unbeleivable", "overrated", "ugly")
# new count at 31 despite strange formatting
part3 = ("it is sad!", "Phony hypocrites!", "make America great again!", "fake media!", "Obamacare is in a death spiral!", "jobs, jobs, jobs!", "such dishonesty!", "much higher ratings at Fox", "a total scam!", "I have tremendous respect for women", "a new low!", "see you in court!", "big trouble!", "get smart US", "a horrible mess", "we will build the wall!", "little credibility", "enjoy!", "not good!", "really bad television", "media is fake!", "NOT!", "drain the swamp!", "a great honor!", "whatever!")
#len 25
p1 = random.randint(0, 11)
p2 = random.randint(0, 30)
p3 = random.randint(0, 24)


jokes = int(input("How many jokes?   \n>>>"))  #my newline worked!!
while True:
    foo = print(part1[random.randint(0, 11)], part2[random.randint(0, 30)], part3[random.randint(0, 24)])
    #print(part1[random.randint(0, 11)], part2[random.randint(0, 30)], part3[random.randint(0, 24)])
    foo #since a print command is nested in foo, I don't need to say print foo
    time.sleep(.7)
    jokes = jokes - 1 #how can I revert so it counts up and not down?
    if jokes <= 0:
        print("...")
        time.sleep(1.5)
        print("Bye!")
        time.sleep(2)
        break
