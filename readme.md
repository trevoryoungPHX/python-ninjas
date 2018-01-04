# Python OOP Game

Complete all the challenges below!

## Ninja
- Add a new method to the Ninja class called "Meditate". When it's called add 5 health to your character.
- Add a new method to the Ninja class called "Backstab". This method should take in another object as a parameter and should remove 10 health from that object.


## Wizard
- Create a new class called "Wizard". The class should inherit from the `Human` class.
- Wizards should have a starting health of 25.
- Wizards should have a additional attribute called "magicPower" that should start at 0 by default.
- Add a new method to the Wizard class called "Study". When it's called add a random number between 1-3 to magicPower.
- Add a new method to the Wizard class called "Fireball". This method should take in another object as a parameter and should remove health from the target equal to the wizards magicPower.
- STRETCH - Add a burn effect to the Fireball method that will remove an additional 1 health from the target a second for 3 seconds.

## Warrior
- Create a new class called "Warrior". The class should inherit from the `Human` class.
- Warriors should have a starting health of 40.
- Warriors should have an additional attribute called "armor" that should start at 10 by default.
- Add a method to the Warrior class called "armorUp". When it's called add 5 armor to the warrior.
- Add a method to the Warrior class called "shieldAlly". This method should take in another object as a parameter and should add 5 health to the object. It should also remove 5 armor from the Warrior. If the Warrior has less than 5 armor this method should print out an error msg.
