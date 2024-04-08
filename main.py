import qiskit
import numpy as np
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition
import tkinter
from tkinter import LEFT, END, DISABLED

# Define Window
root = tkinter.Tk()
root.title('Quantum Visualzier')

# set the logo
# root.iconbitmap(default='safety-glasses.ico')
root.geometry('399x427')
root.resizable(0,0) # Blocking the resizing feature

# Define the colors and fonts
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font = ('Arial', 18)
display_font = ('Arial', 32) 

# Initialize the Quantum Circuit
def initialize_circuit():
    """
    Initialize the Quantum Circuit
    """
    global circuit
    circuit = QuantumCircuit(1)

initialize_circuit()
theta = 0
# Define functions

# Define the gate display function
# def display_gate(gate_input):
#     """
#     Add a corresponding gate notation in the display to track the operation:
#     if the number of operation reach ten, all gate buttons are disabled.
#     """
#     # Insert the defined gate
#     display.insert(END,gate_input)

#     # check if the number of operations has reached ten, if yes,
#     # disable all the gate buttons
#     input_gates = display.get()
#     num_gates_pressed = len(input_gates)
#     list_input_gates = list(input_gates)
#     search_word = ["R","D"]
#     count_double_values_gates = [list_input_gates.count(i) for i in search_word]
#     num_gates_pressed = sum(count_double_values_gates)
#     if num_gates_pressed==10:
#         gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, handamard]
#         for gate in gates:
#             gate.config(state=DISABLED)

def display_gate(gate_input):
                """
                Adds a corresponding gate notation in the display to track the operations.
                If the number of operation reach ten, all gate buttons are disabled.
                """
                # Insert the defined gate
                display.insert(END,gate_input)

                # Check if the number of operations has reached ten, if yes,
                # disable all the gate buttons
                input_gates = display.get()
                num_gates_pressed = len(input_gates)
                list_input_gates = list(input_gates)
                search_word = ["R","D"]
                count_double_valued_gates = [list_input_gates.count(i) for i in search_word]
                num_gates_pressed-=sum(count_double_valued_gates)
                if num_gates_pressed==10:
                    gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, handamard]
                    for gate in gates:
                        gate.config(state=DISABLED)

def clear(circuit):
    """
    Clears the display!
    Reinitializes the Quantum Circuit for fresh calculation!
    Checks if the gate buttons are disabled, if so, enables the buttons
    """
    # Clear the display
    display.delete(0,END)

    # reset the circuit to initial state |0>
    initialize_circuit()

    # Check if the buttons are disabled and if so, Enable the gate buttons
    if x_gate['state']==DISABLED:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, handamard]
        for gate in gates:
            gate.config(state=tkinter.NORMAL)

# Define functions for about Button
def about():
    """
    Displays the info about the project!
    """
    info = tkinter.Tk()

    # specify size of window.
    info.geometry("700x500")
    info.title('About')
    info.resizable(0,0)

    # Create text widget and specify size.
    T = tkinter.Text(info, height = 700, width = 702)

    # Create label
    label = tkinter.Label(info, text= "About Quantum Visualizer")
    label.config(font =("Courier", 14))

    Fact = """
    About: Visualization tool for single Qubit Rotation on Bloch Sphere
        
    Created by: Jagjeet Singh Chauhan
    Created Using: Python,  Thinter, Qiskit
        
    Info about the gate buttons and corresponding qiskit commands:
        
    x = flips the state of qubit -                                 circuit.x()
    y = rotate the state vector about Y-axis -                     circuit.y()
    z = flips the phase by PI radians -                            circuit.z()
    Rx = parameterized rotation about X-axis -                     circuit.rx()
    Ry = parameterized rotation about Y-axis -                     circuit.ry()
    Rz = parameterized rotation about Z-axis -                     circuit.rz()
    S = rotates the state vector about z axis by PI/2 radians -    circuit.s()
    SD = rotates the state vector about z axis by -PI/2 radians -  circuit.sdg()
    T = rotates the state vector about z axis by PI/4 radians -    circuit.t()
    TD = rotates the state vector about z axis by -PI/4 radians -  circuit.tdg()
    H = Hadamard gate - creates the state of superposition -       circuit.h()

    For Rx, Ry and Rz,
    theta(roation_angle) allowed range in the app is [-2*PI,2*PI]

    In case of a visualization error, the app closes automatically.
    This indicates that visualixation of your circuit is not possible."""

    label.pack()
    T.pack()

    # Insert The Fact.
    T.insert(tkinter.END, Fact)

    info.mainloop()

def visualize_circuit(circuit,window):
    """
    Visualizes the single qubit rotations corresponding to applied gates in a separate tkinter window.
    Handles any possible error.
    """
    try:
        visualize_transition(circuit=circuit)
    except qiskit.visualization.exceptions.visualizationError:
        window.destroy()

def change_theta(num,window,circuit,key):
    """
    Change the global variable theta and destroys the window
    """
    global theta
    theta = num*np.pi
    if key=='x':
        circuit.rx(theta,0)
        theta=0
    elif key=='y':
        circuit.ry(theta,0)
        theta=0
    else:
        circuit.rz(theta,0)
        theta=0
    window.destroy()

def user_input(circuit, key):
    """
    Take the user input for rotaion angle for parameterized 
    Rotation gates Rx, Ry, Rz.
    """

    # Initialize and define the properties of Window
    get_input = tkinter.Tk()
    get_input.title("Get Theta Value")
    get_input.geometry('360x160')
    get_input.resizable(0,0)
    
    val1 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial", 10), text="PI/4",command=lambda:change_theta(0.25,get_input,circuit,key))
    val1.grid(row=0, column=0)

    val2 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial", 10), text="PI/2",command=lambda:change_theta(0.50,get_input,circuit,key))
    val2.grid(row=0, column=1)

    val3 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial", 10), text="PI",command=lambda:change_theta(1.0,get_input,circuit,key))
    val3.grid(row=0, column=2)

    val4 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial", 10), text="2*PI",command=lambda:change_theta(2.0,get_input,circuit,key))
    val4.grid(row=0, column=3, sticky='W')

    nval1 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial", 10), text="-PI/4",command=lambda:change_theta(-0.25,get_input,circuit,key))
    nval1.grid(row=1, column=0)

    nval2 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial", 10), text="-PI/2",command=lambda:change_theta(-0.50,get_input,circuit,key))
    nval2.grid(row=1, column=1)

    nval3 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial", 10), text="-PI",command=lambda:change_theta(-1.0,get_input,circuit,key))
    nval3.grid(row=1, column=2)

    nval4 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=("Arial", 10), text="2*PI",command=lambda:change_theta(2.0,get_input,circuit,key))
    nval4.grid(row=1, column=3,sticky='W')

    text_object = tkinter.Text(get_input, height=20, width= 20, bg="light cyan")
    note = """
    Give the value for Theta
    The value has the range [-2*PI,2*PI]
    """
    text_object.grid(sticky='WE',columnspan=4)
    text_object.insert(tkinter.END, note)

    get_input.mainloop()

# Define Layout
# Define Frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both', expand=True)

# Define the Display Frame Layout
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify='left')
display.pack(padx=3, pady=4)

# Define Buttons
# Define First row Button
x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X', command=lambda:[display_gate('x'),circuit.x(0)])
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y', command=lambda:[display_gate('y'),circuit.y(0)])
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z', command=lambda:[display_gate('z'),circuit.z(0)])
x_gate.grid(row=0,column=0,ipadx=45, pady=1)
y_gate.grid(row=0,column=1,ipadx=45, pady=1)
z_gate.grid(row=0,column=2,ipadx=53, pady=1)

# Define Second row Button
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RX',command=lambda:[display_gate('Rx'),user_input(circuit,'x')])
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RY',command=lambda:[display_gate('Ry'),user_input(circuit,'y')])
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RZ',command=lambda:[display_gate('Rz'),user_input(circuit,'z')])
Rx_gate.grid(row=1,column=0,columnspan=1,sticky='WE', pady=1)
Ry_gate.grid(row=1,column=1,columnspan=1,sticky='WE', pady=1)
Rz_gate.grid(row=1,column=2,columnspan=1,sticky='WE', pady=1)

# Define Third row Button
s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='S', command=lambda:[display_gate('S'),circuit.s(0)])
sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD', command=lambda:[display_gate('SD'),circuit.sdg(0)])
handamard = tkinter.Button(button_frame, font=button_font, bg=buttons, text='H', command=lambda:[display_gate('H'),circuit.h(0)])
s_gate.grid(row=2,column=0,columnspan=1,sticky='WE', pady=1)
sd_gate.grid(row=2,column=1,sticky='WE', pady=1)
handamard.grid(row=2,column=2,rowspan=2,sticky='WENS', pady=1)

# Define fifth row Button
t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='T', command=lambda:[display_gate('T'),circuit.t(0)])
td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD', command=lambda:[display_gate('TD'),circuit.tdg(0)])
t_gate.grid(row=3,column=0,sticky='WE',pady=1)
td_gate.grid(row=3,column=1,sticky='WE',pady=1)

# Define Quit and Vistualization Button
quit = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Quit',command=root.destroy)
visualize = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Visualize', command=lambda:visualize_circuit(circuit,root))
quit.grid(row=4,column=0, columnspan=2,sticky='WE',ipadx=5, pady=1)
visualize.grid(row=4,column=2, columnspan=1,sticky='WE', ipadx=8,pady=1)

# Define Clear Button
clear_button =  tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Clear', command=lambda:clear(circuit))
clear_button.grid(row=5,column=0, columnspan=3,sticky='WE')

# Define About Button
about_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='About', command=about)
about_button.grid(row=6,column=0, columnspan=3,sticky='WE')

# Run the main loop
root.mainloop()