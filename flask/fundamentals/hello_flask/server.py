from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app" -- basically these just say "get Flask from whatever location, and that this app is gonna use Flask" Think of this as like an opening tab for the whole server file. It's needed to activate the project.





@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a (basic http) response 


@app.route("/hello") #every method you define in a server had to have its own unique name
def hello():
    return "Well, Hi!"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' inside of the carrots <> gets passed as a variable 'name'. It MUST gets passed into the function below it, or else it will create an error
def hello_name(name):
    print(name) #this is just printing to the console
    return f"Hello, {name}" #this is sending the string to the broswer

@app.route("/math/<int:num>") #int is typecasting num to be an integer and not a string. You could typecast to be a string using str, though there isn't really a need to do it.
def do_math(num):
    newArr = []
    for i in range(0, num+1, 1):
        newArr.append(i)
    return f"{newArr}"





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module. Think of this as like the closing tag for the project. It's needed to deactivate the project. It's saying, "when you run it, run it with debugging turned on." 
    app.run(debug=True, port=5001)    # Run the app in debug mode. The default port on a mac is port5000, and Mac decided with their new OS to occupy that port... so you have to pack on a manual port. It's fine to just do this pre-emptively.



