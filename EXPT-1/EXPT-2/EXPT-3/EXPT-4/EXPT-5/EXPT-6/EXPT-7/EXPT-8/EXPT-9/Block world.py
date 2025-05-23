class BlocksWorld:
    def __init__(self, num_blocks):
        self.state = [[block] for block in range(num_blocks)]
        self.num_blocks = num_blocks

    def display_state(self):
        for i, stack in enumerate(self.state):
            print(f"Stack {i}: {stack}")

    def find_block(self, block):
        for stack in self.state:
            if block in stack:
                return stack
        return None

    def move(self, block, destination):
        source_stack = self.find_block(block)
        destination_stack = self.find_block(destination)

        if source_stack is None:
            print(f"Invalid source block {block}.")
            return
        if destination_stack is None:
            print(f"Invalid destination block {destination}.")
            return

        source_stack.remove(block)
        destination_stack.append(block)
        self.display_state()

    def goal_state(self, goal):
        self.state = goal
        print("Goal state set.")
        self.display_state()

def main():
    blocks_world = BlocksWorld(3)
    print("Initial state:")
    blocks_world.display_state()

    goal = [[0, 1], [2]]
    blocks_world.goal_state(goal)

    print("\nPerforming Moves:")
    blocks_world.move(0, 2)
    blocks_world.move(1, 2)
    blocks_world.move(2, 0)

if __name__ == "__main__":
    main()
