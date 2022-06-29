import pandas as pd
import numpy as np
import ghhops_server as hs
from flask import Flask

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component( 
    "/addition", 
    name="add",    
    description="adding two number",        
    inputs=[        
        hs.HopsNumber("first number", "F", "Floor Number"),       
        hs.HopsNumber("second number", "S", "186"),
        ],    
    outputs=[        
        hs.HopsNumber("result", "R", "result")
        ]
    )

def pointat(first_number, second_number):
    result_final = first_number * second_number
    return result_final

if __name__ == "__main__":
    app.run()