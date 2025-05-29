> Describe the steps for comprehensively testing of a pencil with an eraser on one
end. \
Cases for all types of testing (such as functional, usability, performance, load,
stress, security, etc.) are expected here.

<h3>Let's start with research and requirements gathering.</h3>

1. Product:
Let's decide that we're testing:
> wood pencil where core is graphite mixed with clay
>
> we have a pencil without packaging or smth like this
> 
> color of pencil is black
> 
> eraser is a part of the pencil and can't be ejected.
> 
> our pencil has standard size 19 cm x 6 mm
> 
> the pencil is initially sharpened

2. Audience:
Our pencils can be used by anyone (teacher, student, accountant) and we don't have requirements for any specific area of usage (like special pencils for artists or pencils for NASA space station)

3. Functional requirements:

- A pencil should leave black color on white paper
- The core must not break easily
- An eraser can erase graphite marks without damaging the paper.
- A pencil can be sharpened

4. Non-functional requirements:
- Pencil and eraser should be comfortable and convenient for writing and erasing.
- Pencil and eraser should be able to handle daily usage.
- Usage of pencil and eraser should be safe.
___________________________________
<h3>Cases:</h3>

1. Functional Testing
- Verifying that the pencil can draw on simple white paper
- Verifying that the pencil can draw on alternative materials—newspaper, wall, etc.

- Verifying that we can draw a straight line on the paper (2mm) and a pencil will not leave unnecessary marks on paper or hand
- Verifying that we can draw a curvy line on the paper (2mm), objects like circles, squares, etc. and a pencil will not leave unnecessary marks

- Verifying that a pencil leaves a black mark of good quality depends on the hardness and the applied force (pressing on the paper)
- Verifying that after some time (hours/days) the quality of marks remains the same

- Verifying that a pencil won't break when we press it more than usual. Graphite core shouldn't crumble or break
- Verifying that a pencil core can't be ejected 
- Verifying that dropping a pen from a height of 1m wouldn't break it
- Verifying that tapping the pencil on the table wouldn't break it

- Verifying that the eraser can erase previously drawn lines (drawn a few seconds ago and drawn few hours/days ago)
- Verifying that the eraser didn't leave "dirty" parts after using, or that they can be removed easily without affecting paper quality. 
- Verifying that an eraser shouldn't lose its effectiveness after each usage.
- Verifying that the pencil can write on paper where eraser was used before, and the quality of the marks is the same

2. Usability Testing
- Verifying that the pencil is comfortable to hold in the hand
- Verifying that the pencil is comfortable to hold in the hand during drawing straight and curvy lines
- Verifying the ergonomics of pencil for holding/drawing situations for left-hand and right-hand users
- Verifying the ergonomics of pencil for people with different hand/ finger sizes (adults, kids, etc.)

3. Performance Testing
- Verifying how much time a pencil can be used before sharpening
- Verifying the speed of graphite core usage
- Verifying how fast user can write using pencil

4. Load Testing
- Verifying and comparing the quality of marks during normal and anticipated peak load conditions
10 seconds vs. 10 minutes vs. 60 minutes of drawing, for example
- Analyzing the degradation of drawing marks quality

- Verifying and comparing the quality of eraser usage. 
10 seconds vs. 10 minutes vs. 60 minutes of erasing, for example
- Analyzing the degradation of erasing quality

5. Stress Testing
- Verifying that dropping a pen from a height of 1m wouldn't break it (repeat many times)
- Verifying that tapping the pencil on the table wouldn't break it (repeat many times)
- Verifying that throwing the pencil into the wall wouldn't break it (repeat many times)
- Verifying that bending a pencil wouldn't damage it unless too much power is applied.

6. Security Testing
- Verifying that the pencil and the eraser comply with pencil standards (ISO?)
- Verifying that the pencil and the eraser are safe for usage (maybe we should prohibit/recommend not using a pencil for kids before 6). \
For example, chewing or using near the eyes and ears could be dangerous, and it should be inside the instructions.

7. Environmental Testing
- Verifying that the pencil and eraser work after usage/non-usage in different environments:\
cold (fridge)
heat (windowsill during the sun)
- Verifying that pencil will work after putting it into the water after some time (drying period)
- Verifying that the pencil works the same way in different meteorological conditions, high and low atmospheric pressure, low and high humidity, etc.
