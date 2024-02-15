from flask import Flask, render_template
import turtle

app = Flask(__name__)

@app.route('/')
def index():
    # Create a turtle object
    t = turtle.Turtle()
    
    # Draw the body of the turtle
    t.fillcolor("green")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
    # Draw the head of the turtle
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    # Draw the eyes of the turtle
    t.penup()
    t.goto(-15, 60)
    t.pendown()
    t.dot(10)
    t.penup()
    t.goto(15, 60)
    t.pendown()
    t.dot(10)
    
    # Draw the legs of the turtle
    t.penup()
    t.goto(-25, 40)
    t.pendown()
    t.goto(-50, 20)
    t.goto(-50, 0)
    t.goto(-25, 20)
    t.penup()
    t.goto(25, 40)
    t.pendown()
    t.goto(50, 20)
    t.goto(50, 0)
    t.goto(25, 20)
    
    # Hide the turtle and display the result
    t.hideturtle()
    turtle.done()
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
