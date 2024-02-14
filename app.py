import gradio as gr
import pandas as pd 
import numpy as np
import sqlite3
#conn= sqlite3.connect("test.db")
#c =conn.cursor()
#c.execute('''CREATE TABLE my_table(id INTEGER,nome TEXT, cognome TEXT, eta INTEGER, PRIMARY KEY(id AUTOINCREMENT))''')
#c.execute("INSERT INTO my_table(nome,cognome,eta) VALUES (?,?,?)",("Mario","Rossi",25))
#conn.commit()
#conn.close()
def insert_data_to_sqlite(nome,cognome,eta):
    conn= sqlite3.connect("test.db")
    c =conn.cursor()
    c.execute("INSERT INTO my_table(nome,cognome,eta)VALUES(?,?,?)",(nome,cognome,eta))
    conn.commit()
    conn.close()
def visualizza_data():
    conn = sqlite3.connect("test.db")
    df= pd.read_sql_query("SELECT*FROM my_table",conn)
    conn.close()
    return df
insert_interface= gr.Interface(fn=insert_data_to_sqlite,
                                inputs=["text","text","number"],
                                outputs=None,
                                title="SQLite Data Insert Interface",
                                description="Insert data into sqlite",
                                allow_flagging="never",
    )   
#insert_interface.launch()
visualize_interface= gr.Interface(fn=visualizza_data,
                                inputs=None,
                                outputs=gr.DataFrame(visualizza_data()),
                                title="SQLite Data Insert Interface",
                                description="Insert data into sqlite",
                                allow_flagging="never",
    )
#visualize_interface.launch()
app=gr.TabbedInterface(interface_list= [insert_interface,visualize_interface],
                       tab_names=["Insert","Visualize"])

if __name__ =="_main_":
    app.launch()
