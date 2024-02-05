import turtle

BACKGROUND_COLOR = "yellow"
TREE_COLOR = "blue"
MIN_TURTLE_SPEED = 0
DEFAULT_TREE_DEPTH = 7
MIN_DEPTH = 0
MAX_DEPTH = 9

ANGLE = 45
FRACTION = 0.82


def draw_pythagorean_tree(t, branch_length, depth):
    if depth == 0:
        return
    else:
        # Draw the trunk
        t.forward(branch_length)

        # Save the current position and heading
        pos = t.position()
        heading = t.heading()

        # Draw the first branch (right branch)
        t.left(ANGLE)
        draw_pythagorean_tree(t, FRACTION * branch_length, depth - 1)

        # Restore the position and heading
        t.penup()
        t.setpos(pos)
        t.setheading(heading)
        t.pendown()

        # Draw the second branch (left branch)
        t.right(ANGLE)
        draw_pythagorean_tree(t, FRACTION * branch_length, depth - 1)

        # Restore the position and heading
        t.penup()
        t.setpos(pos)
        t.setheading(heading)
        t.pendown()


def main():
    depth_input = input("Enter the depth of the tree: ")
    if depth_input:
        try:
            depth = int(depth_input)
        except ValueError:
            print("Invalid input. Integer is expected.")
        finally:
            if not depth:
                depth = DEFAULT_TREE_DEPTH
            elif depth < MIN_DEPTH:
                print(f"Depth {depth} is too low. Minimum depth is {MIN_DEPTH}")
                depth = MIN_DEPTH
            elif depth > MAX_DEPTH:
                print(f"Depth {depth} is too high. Maximum depth is {MAX_DEPTH}")
                depth = MAX_DEPTH
    else:
        depth = DEFAULT_TREE_DEPTH

    screen = turtle.Screen()
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Pythagorean Tree")
    tree_turtle = turtle.Turtle()
    tree_turtle.hideturtle()
    tree_turtle.speed(MIN_TURTLE_SPEED)
    tree_turtle.color(TREE_COLOR)
    tree_turtle.left(90)
    tree_turtle.penup()
    # place turtle at bottom center
    tree_turtle.goto(0, -200)
    tree_turtle.pendown()
    tree_turtle.width(3)
    draw_pythagorean_tree(tree_turtle, 100, depth)

    turtle.done()


if __name__ == "__main__":
    main()
