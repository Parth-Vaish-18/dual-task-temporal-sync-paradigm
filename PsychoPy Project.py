from psychopy import visual, core, event
import random
import statistics

win = visual.Window(size=[800, 600], color='black', units='pix')
inst = visual.TextStim(win, text="Welcome to The Temporal Sync Test.\n\n"
                                 "BLUE CIRCLE = JUDGE the time.\n"
                                 "GREEN CIRCLE = GUESS the time.\n\n"
                                 "CRITICAL RULE: You will see text inside the circles.\n"
                                 "You MUST read this text OUT LOUD continuously.\n"
                                 "Do NOT count the seconds in your head!\n\n"
                                 "Press SPACE to start the green circle.\n"
                                 "Press SPACE again to stop it.\n\n"
                                 "Press any key to begin.", height=24, wrapWidth=700)
inst.draw()
win.flip()
event.waitKeys()
target_times = [9.5, 12.0, 15.5, 18.0]
random.shuffle(target_times)

distractor_sentences = [
    "Have you ever noticed how geese act like they own the entire planet? They will literally stand in the middle of a busy intersection and stare down a minivan as if they have premium insurance. Meanwhile, ducks are just out there vibing, asking for bread and doing little synchronized swimming routines. It really makes you wonder what happened in the evolutionary timeline to make one bird a cute park feature and the other a terrifying neighborhood gang leader.",
    "It is completely wild that our brains decided the best way to rest is to paralyze our bodies and force us to watch unhinged, heavily edited movies for eight hours. Like, you will literally have a dream where you are taking a math test inside a grocery store, your high school gym teacher is the cashier, and instead of money, you have to pay with a handful of wet spaghetti. And your brain just accepts this as completely normal.",
    "Imagine trying to explain the concept of a pet dog to an alien species. You would have to be like, 'Yeah, so there is this tiny wolf living in my house. It doesn't pay rent, it sleeps on my nicest pillows, and if the doorbell rings, it completely loses its mind.' And the alien would probably ask what its job is, and you would just have to admit that its only job is to occasionally look at you and wag its tail.",
    "The microwave is the most dramatic appliance in the entire kitchen. You put a bowl of soup in there for exactly two minutes, and it comes out with the bowl hotter than the surface of the sun, but the middle of the soup is still somehow ice cold. And then, if you do not open the door within three seconds of it finishing, it will beep loudly enough to wake up everyone in a three-mile radius.",
    "History timelines are incredibly weird when you actually look at them closely. For example, the university of Oxford is older than the Aztec Empire. That means there were kids complaining about their college finals in England before the city of Tenochtitlan was even founded. Also, woolly mammoths were still casually walking around on Earth while the Egyptians were building the Great Pyramids. Time makes absolutely no sense when you put it all into perspective like that.",
    "Grocery shopping is basically a psychological experiment to see how much random stuff you can fit into a cart before you remember you only came for milk. You walk in with a clear mission, but then you see a weird new flavor of chips, a ridiculously large bottle of hot sauce, and a scented candle. Suddenly, you are at the register spending eighty dollars and you completely forgot the one thing you actually needed to buy.",
    "I respect spiders for eating mosquitoes, but they really need to work on their boundaries. If a spider is chilling up in the corner of the ceiling minding its own business, we have an understanding. But the second it lowers itself down like a tiny eight-legged secret agent right over my bed, the peace treaty is officially canceled. They have the whole house to build a web, yet they always choose the exact spot where I walk.",
    "The ocean is basically an alien planet right here on Earth, and we just casually go swimming in it. There are fish down there with built-in flashlights on their heads, giant squids the size of a school bus, and crabs that look like they hit the gym seven days a week. And yet, the thing that scares me the most at the beach is when a piece of mysterious, slimy seaweed touches my ankle while I am standing in the shallow water."
]
random.shuffle(distractor_sentences)

stim_circle = visual.Circle(win, radius=250, fillColor='blue')
reproduce_circle = visual.Circle(win, radius=250, fillColor='green')
prompt_text = visual.TextStim(win, text="", pos=(0, -260), height=30)
trial_text = visual.TextStim(win, text="", height=40, bold=True)
distractor_text = visual.TextStim(win, text="", height=20, wrapWidth=450, color='white', bold=True)
results = []
timer = core.Clock()

for trial, target_time in enumerate(target_times):
    trial_text.text = f"Trial {trial + 1}"
    trial_text.draw()
    win.flip()
    core.wait(1.5)
    win.flip()
    core.wait(0.5)

    distractor_text.text = distractor_sentences.pop() 
    stim_circle.draw()
    distractor_text.draw() 
    win.flip()
    core.wait(target_time) 
    win.flip()
    core.wait(0.5)
    
    prompt_text.text = "Press SPACE to START your guess.\nPress SPACE again to STOP."
    prompt_text.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    timer.reset() 
    distractor_text.text = distractor_sentences.pop()
    reproduce_circle.draw()
    distractor_text.draw()
    win.flip()
    
    event.waitKeys(keyList=['space']) 
    reproduced_time = timer.getTime()
    win.flip()
    core.wait(1.0)

    error = reproduced_time - target_time
    ratio = reproduced_time / target_time 
    results.append({
        "target": target_time,
        "reproduced": reproduced_time,
        "error": error,
        "ratio": ratio
    })
win.close()

print("\n" + "="*55)
print("DYSCHRONOMETRIA ANALYSIS: RESULTS")
print("="*55)

errors = [res['error'] for res in results]
abs_errors = [abs(res['error']) for res in results]
ratios = [res['ratio'] for res in results]

for i, res in enumerate(results):
    t = res['target']
    r = res['reproduced']
    e = res['error']
    direction = "OVER-estimated" if e > 0 else "UNDER-estimated"
    print(f"Trial {i+1}: Target {t:>4.1f}s | Guess {r:>5.2f}s | Error: {abs(e):>5.2f}s ({direction})")

print("-" * 55)
mean_abs_error = sum(abs_errors) / len(abs_errors)
print(f"Mean Absolute Error:        {mean_abs_error:.2f} seconds")

mean_ratio = sum(ratios) / len(ratios)
ratio_pct = mean_ratio * 100
print(f"Mean Time Perception Ratio: {mean_ratio:.3f} ({ratio_pct:.1f}%)")

if len(errors) > 1:
    std_dev = statistics.stdev(errors)
    print(f"Standard Deviation:         {std_dev:.2f} seconds")
else:
    std_dev = 0
    print("Standard Deviation:         N/A")

print("\n--- CLINICAL MARKERS & ANALYSIS ---")

if 0.80 <= mean_ratio <= 1.20:
    print("Internal Clock Speed:       NORMAL (Expected human variance detected)")
elif mean_ratio < 0.80:
    print("Internal Clock Speed:       FLAG - Temporal Shortening (Consistent underestimating)")
else:
    print("Internal Clock Speed:       FLAG - Time Overestimation (Consistent over-guessing)")
    
if std_dev <= 3.0:
    print("Metronome Consistency:      NORMAL (Steady guessing pattern)")
else:
    print("Metronome Consistency:      FLAG - High Erratic Variance (Highly inconsistent)")

print("\n--- OVERALL CONCLUSION ---")
if mean_ratio < 0.80 and std_dev > 3.0:
    print("Result:  SIGNIFICANT DYSCHRONOMETRIA MARKERS DETECTED.")
    print("Profile: The data shows both severe temporal shortening and erratic variance.")
    print("         This extreme dual-profile strongly aligns with the baseline metrics")
    print("         seen in clinical time blindness and executive function research.")
elif (mean_ratio < 0.80 or mean_ratio > 1.20) or (std_dev > 3.0):
    print("Result:  SUB-CLINICAL VARIANCE DETECTED.")
    print("Profile: Your internal clock shows some drift or inconsistency, but it lacks the")
    print("         compounding factors typically associated with clinical time blindness.")
    print("         This level of variance is highly common under cognitive load.")
else:
    print("Result:  TYPICAL NEUROCOGNITIVE PROFILE.")
    print("Profile: Your temporal accuracy and trial-to-trial consistency fall squarely")
    print("         within the expected baseline for typical human performance.")

print("="*55 + "\n")
core.quit()