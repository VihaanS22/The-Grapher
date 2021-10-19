import pandas as pd
import plotly.express as px

print("")
print("The Covid Grapher")
print("")
print("Hello. What type of graph would you want to analyze for the covid cases from the spreadout? :-")
print("")
print("Bar Graph")
print("Line Graph")
print("Scatter Graph")
print("")

graph = input("Please enter your choice according to the options given :-")

if(graph == "Bar Graph"):
    
    #bar graph
    df = pd.read_csv("data.csv")
    fig = px.bar(df, x='Cases', y='Dates', color="Countries")
    fig.show()


elif(graph == "Line Graph"):
    
    #line graph
    df = pd.read_csv("data.csv")

    fig = px.line(df, x="Dates", y="Cases", color="Countries")

    fig.show()


elif(graph == "Scatter Graph"):

    #scatter graph
    df = pd.read_csv("data.csv")
    fig = px.scatter(df, x="Dates", y="Cases",
                color="Countries")
    fig.show()


else:
    print("You haven't chosen anything. We'll show you the best graph from these.")
   
    df = pd.read_csv("data.csv")

    fig = px.line(df, x="Dates", y="Cases", color="Countries")

    fig.show()
