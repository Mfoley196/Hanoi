import sys

class TowerOfHanoi:

    rings = {'blue': 1, 'purple': 2, 'green': 3, 'red': 4}
    valid_poles = ['a', 'b', 'c']

    def __init__(self):
        # initialize rings + positions
        self.poles = {
            "a": ['red', 'green', 'purple', 'blue'],
            "b": [],
            "c": []
        }
        self.solved = False

        self.run_game()

    def run_game(self):
        while not self.solved:
            valid_input = False
            valid_move = False
            raw = ''
            words = []

            while not valid_input:
                # get input
                raw = input("Enter command: ")
                # parse input
                valid_input = self.parse_input(raw)

            # Can only be here if command was validly formatted
            words = raw.split(" ")
            ring = words[0]
            target_pole = words[2].lower()
            dest_pole = words[4].lower()


            # Validate if ring can be moved
            # Check that there are rings on the target pole
            # Check that the topmost ring on the target pole is the ring
            # the user wants to move
            # Check the user isn't moving the ring to the same pole
            if (self.poles[target_pole] and 
                self.poles[target_pole][-1] == ring and
                target_pole != dest_pole):
                # If the destination pole is not empty, and doesn't have a 
                # smaller ring on it already
                if (self.poles[dest_pole] and 
                    self.rings[self.poles[dest_pole][-1]] > self.rings[ring]):
                    #print("ring can be moved") 
                    valid_move = True
                elif not self.poles[dest_pole]:
                    # If the destination pole is empty, no need to check
                    #print("ring can be moved - empty pole") 
                    valid_move = True
                else:
                    # There is a smaller ring on the destination pole 
                    # Show error message
                    valid_move = False
                    print("Error: illegal move - smaller disk on pole")
            else:
                valid_move = False
                print("Error: illegal move.")

            # move rings if valid
            if valid_move:
                ring_to_move = self.poles[target_pole].pop()
                self.poles[dest_pole].append(ring_to_move)
                print("Moved " + ring + " ring from pole " + target_pole.upper() +
                    " to pole " + dest_pole.upper())

            # check if game is solved
            if (self.poles['c'] and 
                self.poles['c'] == ['red', 'green', 'purple', 'blue']):
                self.solved = True

        if self.solved:
            print("Congratulations! You solved the puzzle!")

    # Checks if the input is a valid ring move command
    # if so, returns True, otherwise performs the command and returns False
    def parse_input(self, raw):
        raw = raw.strip().lower()
        words = raw.split(" ")

        try:
            # If display command is entered
            if 'display' in words:
                if words[1] in self.valid_poles:
                    self.display(words[1])
                    return False
                else:
                    raise TypeError

            # If command is formatted properly
            if (len(words) == 5 and words[0] in self.rings.keys() and 
                words[1] == 'from' and words[2] in self.valid_poles and
                words[3] == 'to' and words[4] in self.valid_poles):
                return True

            # Secret debug commands
            if "solved" in words:
                self.solved = True
                return True

            if "all" in words:
                print(self.poles)
                return False

            if "quit" in words:
                print("Goodbye!")
                sys.exit(0)

            # If no if statement has run, raise exception to show 
            # error message and return false
            raise TypeError

        except (IndexError, TypeError):
            print("Incorrect command. Please try again.")
            return False

    # Display the requested pole
    def display(self, pole):
        print("From bottom of pole " + pole.upper() + " to top: ")
        print(self.poles[pole])

if __name__ == "__main__":
    TowerOfHanoi()